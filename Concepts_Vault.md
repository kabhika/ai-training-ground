# The Concept Vault: AI Architecture Visualized

## Concept 1: The LLM POST Request Payload

This sequence diagram visualizes how a text prompt is packaged into JSON and delivered to an AI server via an HTTP POST request.

```mermaid
sequenceDiagram
    autonumber
    participant U as User (You)
    participant C as Client (Python Script)
    participant S as LLM Server (API)

    U->>C: Types Prompt: "Explain Vector Embeddings"
    Note over C: Step 1: JSON Packaging<br/>{ "prompt": "...", "temperature": 0.7 }
    C->>S: Step 2: HTTP POST Request (Network Path)
    Note over S: Step 3: LLM Processing<br/>(Neural Network generates tokens)
    S-->>C: Step 4: HTTP Response (Status 200/201)<br/>{ "response": "Generated text..." }
    Note over C: Step 5: JSON Parsing
    C->>U: Displays final plain text on screen
```