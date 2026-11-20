# Frozen effective query set (v3, 2026-11-17) — as actually run

All queries: IEEE Xplore command search, field = All Metadata, year >= 2019, English,
matchBoolean=true. These are the strings actually executed in this re-run. C1 and C7
were re-tightened from protocol_v2 (noted below) because the v2 strings were dominated
by off-topic LLM papers; the re-tightened strings were frozen before screening.

C1  ("LLM agent" OR "large language model agent" OR "LLM-based agent")           [re-tightened from v2; dropped bare "agentic AI"]
C2  ("LLM" OR "large language model") AND ("function calling" OR "tool calling" OR "tool invocation")
C3  ("agentic RAG" OR "agentic retrieval-augmented" OR "self-RAG" OR "iterative retrieval") AND ("LLM" OR "large language model")
C4  ("GraphRAG" OR "graph retrieval-augmented") AND ("knowledge graph" OR "LLM" OR "large language model")
C5  ("LLMOps" OR "LLM serving" OR "large language model operations" OR "model serving") AND ("pipeline" OR "deployment" OR "lifecycle" OR "inference")
C6  ("Kubernetes" OR "serverless" OR "cloud-native") AND ("LLM" OR "large language model") AND ("serving" OR "inference" OR "deployment")
C7  ("LLM agent" OR "LLM-based agent" OR "agentic AI system") AND ("security" OR "attack" OR "threat" OR "vulnerability")   [re-tightened from v2]
C8  ("prompt injection" OR "indirect prompt injection" OR "tool poisoning") AND ("LLM" OR "large language model" OR "agent")
C9  ("LLM-based multi-agent" OR "multi-agent LLM" OR "LLM multi-agent" OR "agent orchestration") AND ("LLM" OR "large language model")
C10 ("agent interoperability" OR "agent protocol" OR "agent communication protocol") AND ("LLM" OR "large language model" OR "agentic")
C11 ("Model Context Protocol" OR "Agent2Agent" OR "Agent Communication Protocol" OR "Agent Network Protocol")
C12 ("AI governance" OR "policy-as-code" OR "runtime policy enforcement") AND ("LLM" OR "agent" OR "agentic")
C13 ("observability" OR "distributed tracing" OR "OpenTelemetry") AND ("LLM" OR "large language model" OR "agentic")

## Expected tightened hit counts (from count sweep)
C1 563 · C2 168 · C3 70 · C4 209 · C5 292 · C6 130 · C7 117 · C8 361 · C9 423 ·
C10 21 · C11 420 · C12 202 · C13 210   (live header recorded per scrape; minor drift expected)
