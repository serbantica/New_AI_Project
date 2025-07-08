# Project Roadmap

This document outlines the strategic vision for this project template. The goal is to create a repository that not only provides a starting point but actively helps shape and build the project based on user needs.

### **Core Vision**

1.  **Minimal Template Structure:** Create and maintain a minimal, clean file/folder structure for a template repository that can be easily shared and forked for collaboration.
2.  **Dynamic Project Scaffolding:** Develop a system that dynamically builds out the project environment in stages.
    *   **2a. Chartering:** Generate a Python-based Streamlit application to define the use case, including all business and technical requirements.
    *   **2b. Definition:** Use the chartering tool's output to formally define the project's business case, architecture, and technical specifications.
    *   **2c. Generation:** Based on the definition, generate the next-stage project structure, including necessary components like agents, LLMs, databases, CI/CD pipelines, etc.
3.  **Scalable Operation:** Enable the project to be run, deployed, and collaborated on in a scalable way, allowing instances to be started, stopped, and restarted as needed.

---

### **Analysis of Current State vs. Vision**

| Goal | What's in Place (The Foundation) | What Needs to Be Developed (The Next Steps) |
| :--- | :--- | :--- |
| **1. Minimal Template Structure** | **SOLID:** We have a core file structure (`src`, `docs`, etc.), a `makefile` for standard commands, `pyproject.toml` for dependencies, and a `project_bootstrap.sh` script that reliably generates this structure, including the now self-contained `charter_tool`. | **REFINEMENT:** The core template is good, but we need to perfect it. The key missing piece is a robust `.gitignore` file to ensure that generated files, virtual environments, and other noise are never committed to the repository. |
| **2. Dynamic Project Scaffolding** | **PARTIALLY COMPLETE (a):** The mechanism to generate the Streamlit app's code (`charter_tool/`) exists via the bootstrap script. The environment is set up correctly. | **NEEDS DEVELOPMENT (b, c):** This is the core of the vision. <br> **b)** The `streamlit_app.py` is just a placeholder. It needs to be built into a functional tool that guides the user through the `charter_template.md` and **saves their input** (e.g., to a YAML file in `configs/`). <br> **c)** There is currently **no mechanism** to read that saved charter and generate the *next stage* of the project (agents, DBs, etc.). This is the most significant development area. |
| **3. Scalable Project Operation** | **CONCEPTUAL:** The `makefile` provides simple command aliases (`make streamlit`). The `demo_charter_tool.sh` script *mentions* `docker build`, but there is no `Dockerfile` or any deployment infrastructure yet. | **NEEDS DEVELOPMENT:** We need to build the infrastructure for running the project. This means creating a `Dockerfile` for containerization, a `docker-compose.yml` file to orchestrate multiple services (like a database), and a CI/CD pipeline (e.g., GitHub Actions) to automate testing and deployment. |

---

### **Strategic Roadmap: How We Get There**

Here is a proposed plan, moving from the most immediate task to the long-term vision.

#### **Phase 1: Implement the Charter Tool (Fulfilling Goal 2b)**

This is the most critical next step. Without a functional charter tool that captures user requirements, no further automation is possible.

1.  **Develop `streamlit_app.py`:** We will build out the Streamlit interface with input forms, text areas, and selectors that correspond directly to the sections in `charter_template.md`.
2.  **Implement Data Persistence:** We'll use the `pyyaml` library to write the user's input from the Streamlit app into a structured YAML file, for example: `configs/project_charter.yaml`. We will also implement the logic to load an existing charter file back into the app.
3.  **(Optional) AI-Powered Assistance:** We can integrate a chat component into the Streamlit app that calls a Large Language Model (LLM) to help the user answer the charter questions, providing suggestions and clarifications.

#### **Phase 2: Build the Scaffolding Engine (Fulfilling Goal 2c)**

Once we have the `project_charter.yaml`, we can build the "magic" that generates the project.

1.  **Create a Code Generator Script:** We'll develop a new script (likely in Python for better logic handling) that reads `configs/project_charter.yaml`.
2.  **Implement Conditional Logic:** This script will contain the logic to generate files and folders based on the charter's contents.
    *   *If `architecture` is `RAG`*, it will generate placeholder files for data loading, embedding, and vector search.
    *   *If `database` is `PostgreSQL`*, it will create a database connection module and add `psycopg2-binary` to the project dependencies.
    *   *If `deployment` requires `Docker`*, it will generate a `Dockerfile` and `docker-compose.yml`.
3.  **Integrate into `makefile`:** We'll add a new command like `make scaffold` to run this generator script.

#### **Phase 3: Establish Scalable Operations (Fulfilling Goal 3)**

With the project structure dynamically generated, we'll focus on making it runnable and deployable.

1.  **Containerize Everything:** Develop robust, multi-stage `Dockerfile`s for the generated services.
2.  **Orchestrate with Docker Compose:** Create and generate a `docker-compose.yml` that can spin up the entire application stack (the app, a database, an LLM server, etc.) with a single command: `docker-compose up`.
3.  **Automate with CI/CD:** Create a `.github/workflows/ci.yml` file to automatically run tests, lint code, and build Docker images whenever code is pushed to the repository.
