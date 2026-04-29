# Lab 3: Introduction to LLM Agents and Tool Usage

## 1. Agent Name
**DataExplorer Lab Agent**

## 2. Agent Purpose
This agent was developed as part of our introductory laboratory on LLM-based agents. Our primary goal was to transition from a basic prompt-based chatbot to a functional agent capable of interacting with a system state through autonomous tool calling.

The agent serves as a technical assistant for exploring and analyzing internal data structures. Instead of relying on static knowledge, the agent actively invokes Python tools to query an in-memory state, ensuring that the information provided about customers and orders is accurate and grounded in the data.

**Technical Task Specification:**
*   **Discovery:** Identify available tables and provide high-level metadata such as record counts and field names.
*   **Structural Analysis:** Inspect and explain the specific schema and data types of a selected dataset.
*   **Data Extraction:** Retrieve raw records to allow for manual review of the dataset content.
*   **System Integrity:** The agent is instructed to verify data existence via tools before responding and to maintain a professional technical tone in English.

## 3. Agent Tools
We implemented and registered three primary Python functions as tools for the agent's environment:

### `list_datasets()`
*   **Description:** Scans the internal `datasets_state` and returns a summary of all available tables.
*   **Input:** None.
*   **Output:** A dictionary containing a list of available datasets, their record counts, and field names.

### `describe_dataset(dataset_name)`
*   **Description:** Provides a detailed technical breakdown of a specific table's structure.
*   **Input:** `dataset_name` (String) – The name of the dataset to describe (e.g., 'customers' or 'orders').
*   **Output:** A JSON object containing the schema details and a sample row to demonstrate the data format.

### `show_data(dataset_name)`
*   **Description:** Fetches and returns the complete raw content of the requested dataset.
*   **Input:** `dataset_name` (String).
*   **Output:** The full list of records (raw data) representing the current state of the dataset.

## 4. Example Interaction

**User:** "Hi! What datasets are available for me to look at?"

**Agent Response:**
> *[Step: list_datasets() invoked]*
>
> "Hello! I have identified two available datasets in the system:
> 1. **customers**: Contains 2 records with fields for ID, Name, and Country.
> 2. **orders**: Contains 3 records tracking Order ID, Customer ID, Amount, and Currency.
> 
> Which one would you like to explore further?"

**User:** "Can you show me what the orders table looks like? Just an example."

**Agent Response:**
> *[Step: describe_dataset(dataset_name="orders") invoked]*
>
> "The **orders** dataset contains 4 fields. Here is an example of a typical record from this table:
> ```json
> {
>   "order_id": 100,
>   "customer_id": 1,
>   "amount": 120.5,
>   "currency": "USD"
> }
> ```
> There are currently 3 orders recorded in the system. Would you like to see the full list of raw data?"
