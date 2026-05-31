# Lab Report: Lab 3.1 — Event-Driven Cybersecurity Pipeline

**Course:** HIT Accelerated AI Lab 5  
**Students:** [שם 1] & [שם 2]  
**Date:** May 31, 2026

---

## 1. Overview
The objective of this laboratory was to design and implement a scalable, event-driven pipeline for cybersecurity analysis. By utilizing Kafka as a message broker and OpenTelemetry for distributed tracing, we constructed a system capable of real-time event ingestion, classification, and statistical analysis.

## 2. Architecture
The pipeline follows a decoupled architecture designed to handle high-load security telemetry:
- **Producer:** Generates synthetic security events (e.g., login attempts, process executions).
- **Kafka:** Decouples the producer from the consumers, acting as a reliable event stream.
- **Consumer & Classifier:** Consumes raw events, maps them to **MITRE ATT&CK** tactics (Execution, Credential Access), and persists data to a local CSV store.
- **Analysis:** Performs offline statistical aggregation and visualization of security events.



## 3. Implementation Details
### 3.1 Ingestion & Processing
We deployed the infrastructure using `docker compose`. The system utilizes:
- **Redpanda Console** for Kafka topic inspection.
- **Jaeger** for distributed tracing of event processing latency.
- **Python-based Consumer** to apply classification logic and write results to `data/classified_packets.csv`.

### 3.2 Classification Logic
Events were classified using a mapping function:
- `powershell.exe` → Execution (T1059.001)
- `cmd.exe` → Execution (T1059.003)
- `logon_type: failure` → Credential Access (T1110)

## 4. Results
The pipeline successfully processes events asynchronously. Our analysis notebook demonstrates the distribution of detected threats over time, providing visibility into security activity trends.



## 5. Discussion & Conceptual Questions
**Why use Kafka over direct calls?** Kafka provides asynchronous decoupling. If the classification stage experiences a burst in traffic, the events are queued rather than lost, ensuring system stability.

**What happens if the consumer is slower than the producer?** Events accumulate in the Kafka topic. The system gracefully buffers the excess load until the consumer catches up, preventing data loss.

**How does tracing help debug?** Jaeger allows us to visualize the exact path of an event. By inspecting spans like `classify_and_store`, we can identify bottlenecks or failures within the processing pipeline.

**Scalability Considerations:** The consumer stage is horizontally scalable. By adding more consumer instances, we can increase the throughput of the classification stage without affecting the producer.

**Real-world SOC implications:** In a production environment, we would replace CSV storage with a scalable database (e.g., Elasticsearch), add real-time alerting, and implement robust authentication for the event stream.

---
## 6. Conclusion
This lab demonstrated the practical benefits of event-driven architectures. By separating generation, processing, and analysis, we achieved a modular and observable pipeline that forms the foundation for more advanced AI-driven security analysis.
