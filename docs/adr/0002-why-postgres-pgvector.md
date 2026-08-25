
# 2. Why PostgreSQL with pgvector

Date: 2026-08-25

## Status

Accepted

## Context

Argus needs to store traditional relational data (Users, Repos, Files, Jobs) as well as vector embeddings representing chunks of source code for Phase 2's Retrieval-Augmented Generation (RAG) chat features.

## Decision

We chose **PostgreSQL** paired with the **pgvector** and **TimescaleDB** extensions.

## Consequences

**Pros:**

- **Unified Architecture:** By keeping relational data and vector data in the same database engine, we avoid the complexity of maintaining a separate dedicated vector database (like Pinecone or Milvus) and can perform hybrid searches (e.g., "Find this semantic match, but only inside `repo_id = 5`").
- **TimescaleDB:** Useful for Phase 4 and 5 (Process Analytics and Ops Monitoring) where we will track time-series events like job runs, pings, and PR velocity.
- **Reliability:** Postgres is battle-tested, ACID compliant, and highly reliable.

**Cons:**

- Vector searches in `pgvector` can become slightly slower than dedicated vector databases at extreme scale (10s of millions of vectors), but we can utilize HNSW indexes to maintain high performance for our workload.
