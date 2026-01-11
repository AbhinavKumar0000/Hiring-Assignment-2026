# Complex Code Samples

Below are links to the most complex code I have written, demonstrating my ability in both Machine Learning pipeline optimization and robust Backend Engineering.

---

## 1. Complex Python Code: EdgeRAG

**Project Name:** "EdgeRAG" (CPU-Optimized End-to-End RAG)
**Repository Link:** https://github.com/AbhinavKumar0000/EdgeRAG

### **Description**

EdgeRAG is a fully local Retrieval-Augmented Generation system engineered to run efficiently in **CPU-only environments** (under ~1GB total footprint) while preserving retrieval quality. It moves beyond simple API wrappers by implementing custom model fine-tuning and aggressive quantization strategies suitable for edge devices.

### **Technical Complexity:**

- **Advanced Embedding Optimization:**
  - Fine-tuned `bge-small-en` using **Contrastive Learning** (Triplet Loss) on a custom dataset to maximize semantic separation.
  - Implemented **Matryoshka Representation Learning** to truncate embeddings from 384 to **128 dimensions**, reducing retrieval computation by ~67% without retraining.
  - Converted the model to **ONNX INT8** format (final size ~32 MB).
- **Generative Model Quantization:**
  - Optimized `Qwen2.5-1.5B` using **GGUF Q5_K_M** format (mixed 5-bit precision) to balance memory footprint (~940 MB) and instruction-following capability on CPU.
- **System Architecture:**
  - Built a local retrieval index using **FAISS** (CPU) and a custom inference loop via `llama.cpp`.
  - Developed a hybrid deployment strategy supporting both local CLI execution and cloud-hosted **FastAPI** endpoints with token streaming.

### **Tech Stack**

Python, PyTorch, FAISS, ONNX Runtime, Llama.cpp, LangChain, FastAPI.

---

## 2. Complex Database Code: Marginalia

**Project Name:** "Marginalia" (Book Review API)
**Repository Link:** https://github.com/AbhinavKumar0000/fastapi-book-review-service

### **Description**

Marginalia is a high-performance, asynchronous REST API designed for a book review platform. It demonstrates enterprise-grade database patterns using **FastAPI** and **SQLModel** (SQLAlchemy + Pydantic).

### **Technical Complexity:**

- **Asynchronous Database Operations:** Utilizes `asyncpg` for non-blocking database communication, allowing the API to handle high concurrency under load.
- **Advanced Schema Design:** Implements complex relationships and strict data validation using Pydantic v2 models that map directly to PostgreSQL tables.
- **Modular Architecture:** The codebase is refactored into domain-driven modules (`src/auth`, `src/books`, `src/db`) to ensure scalability and maintainability.

### **Tech Stack**

FastAPI, PostgreSQL, SQLModel, Alembic (migrations), Asyncio.
