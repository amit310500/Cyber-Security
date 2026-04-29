import os
import json
from typing import Annotated, Dict

import chainlit as cl
from autogen import ConversableAgent
from autogen.events.agent_events import ExecuteFunctionEvent, ExecutedFunctionEvent

# ---------------------------
#  In-memory example datasets
# ---------------------------

datasets_state: Dict[str, list] = {
    "customers": [
        {"id": 1, "name": "Alice", "country": "US"},
        {"id": 2, "name": "Bob", "country": "UK"},
    ],
    "orders": [
        {"order_id": 100, "customer_id": 1, "amount": 120.5, "currency": "USD"},
        {"order_id": 101, "customer_id": 2, "amount": 99.9, "currency": "GBP"},
        {"order_id": 102, "customer_id": 1, "amount": 250.0, "currency": "USD"},
    ],
}

# ---------------------------
#  Tools (plain functions)
# ---------------------------

def list_datasets() -> Dict:
    """Return all available datasets with basic information about them."""
    datasets_info = []
    for name, rows in datasets_state.items():
        num_records = len(rows)
        num_fields = len(rows[0]) if num_records > 0 else 0
        field_names = list(rows[0].keys()) if num_records > 0 else []
        datasets_info.append(
            {
                "name": name,
                "num_records": num_records,
                "num_fields": num_fields,
                "field_names": field_names,
            }
        )
    return {"datasets": datasets_info}


def describe_dataset(
    dataset_name: Annotated[
        str,
        "Name of the dataset to describe. Must be one of: 'customers', 'orders'.",
    ],
) -> Dict:
    """Return detailed information for a specific dataset."""
    if dataset_name not in datasets_state:
        return {
            "ok": False,
            "error": "dataset_not_found",
            "message": f"Dataset '{dataset_name}' not found.",
        }

    rows = datasets_state[dataset_name]
    return {
        "ok": True,
        "dataset": dataset_name,
        "num_records": len(rows),
        "field_names": list(rows[0].keys()) if rows else [],
        "example_row": rows[0] if rows else None,
    }


def show_data(
    dataset_name: Annotated[
        str,
        "Name of the dataset to extract. Must be one of: 'customers', 'orders'.",
    ],
) -> Dict:
    """Return raw data for a specific dataset."""
    if dataset_name not in datasets_state:
        return {"ok": False, "error": "dataset_not_found"}

    return {"ok": True, "dataset": dataset_name, "raw_data": datasets_state[dataset_name]}


# ---------------------------
#  LLM configuration
# ---------------------------

# שליפת המפתח מהקובץ .env
api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("API_KEY is missing! Check your .env file.")

llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile", # המודל המעודכן והפעיל ביותר
            "api_key": api_key,
            "base_url": "https://api.groq.com/openai/v1", # קישור ישיר ל-Groq
        }
    ],
}

# ---------------------------
#  System prompt
# ---------------------------

SYSTEM_PROMPT = """\
You are a data analysis agent. You work with 'customers' and 'orders' datasets.
Use your tools to answer questions about data structure or content.
Always answer in English.
"""

WELCOME_MESSAGE = """\
Hello! I am your Dataset Agent. 
I can help you explore the 'customers' and 'orders' tables. 
Try asking: 'What datasets are available?'
"""

def _format_content(content: object) -> str:
    if content is None: return ""
    if isinstance(content, str): return content
    return json.dumps(content, indent=2)

# ---------------------------
#  Chainlit event handlers
# ---------------------------

@cl.on_chat_start
async def on_chat_start():
    assistant = ConversableAgent(
        name="dataset_analysis_agent",
        system_message=SYSTEM_PROMPT,
        llm_config=llm_config,
        human_input_mode="NEVER",
        functions=[list_datasets, describe_dataset, show_data],
    )
    cl.user_session.set("assistant", assistant)
    await cl.Message(content=WELCOME_MESSAGE).send()


@cl.on_message
async def on_message(message: cl.Message):
    assistant: ConversableAgent = cl.user_session.get("assistant")

    response = await assistant.a_run(
        message=message.content,
        clear_history=False,
        max_turns=6,
        summary_method="last_msg",
    )

    tool_inputs = {}

    async for event in response.events:
        if isinstance(event, ExecuteFunctionEvent):
            event_data = event.content
            tool_key = getattr(event_data, "call_id", None) or event_data.func_name
            tool_inputs[tool_key] = {
                "name": event_data.func_name,
                "input": _format_content(event_data.arguments),
            }
            continue

        if isinstance(event, ExecutedFunctionEvent):
            event_data = event.content
            tool_key = getattr(event_data, "call_id", None) or event_data.func_name
            step_data = tool_inputs.get(tool_key, {"name": event_data.func_name, "input": ""})
            
            async with cl.Step(name=step_data["name"], type="tool") as step:
                step.input = step_data["input"]
                step.output = _format_content(event_data.content)

    summary = await response.summary
    await cl.Message(content=_format_content(summary)).send()