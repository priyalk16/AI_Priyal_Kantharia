# 🎓 Edu-Viz: AI-Powered Educational Videos

## ✨ Project Overview

Edu-Viz is an innovative project that transforms static textbook knowledge into **dynamic, AI-powered animated videos**.  
By bridging the gap between dense theory and engaging visuals, our platform offers a **personalized learning experience** for complex subjects like **Data Structures, GIS, and Space Technology**.  

Instead of reading long chapters, students can simply query a concept and watch it come to life through animations.

---

## ⚙️ How It Works

The system is an **orchestrated pipeline** of modern technologies. The workflow is as follows:

1. **User Query**  
   A student inputs a concept (e.g., "Graph Traversal").

2. **Knowledge Retrieval**  
   The system queries a **Knowledge Graph (Neo4j)** to fetch structured information, related concepts, and interconnections.

3. **Content Generation**  
   AI Layer (using **Gemini/GPT**) generates:  
   - A detailed narration script  
   - A bullet-point slide outline  

4. **Content Formatting**  
   The AI output is standardized into a **JSON/Markdown format** for consistency and machine-readability.

5. **Video Animation**  
   The **Manim Automation Layer** parses formatted content and automatically generates slides with synchronized animations.

6. **Video Output**  
   The final MP4 video is rendered and stored for future retrieval.

---

## 🚀 Key Features

- **Personalized Learning:** Provides explanations tailored to each query.  
- **Engaging Visuals:** High-quality, auto-generated animations simplify complex topics.  
- **Scalable & Efficient:** The automated pipeline enables rapid content generation across multiple domains.  
- **Structured Knowledge:** Knowledge Graph ensures accuracy and an interconnected view of concepts.

---

## 📦 Repository Structure

```plaintext
edu-viz/
├── core/
│   ├── kg_connector.py       # Logic for querying the Knowledge Graph
│   ├── llm_generator.py      # AI content generation from KG data
│   ├── formatter.py          # Standardizes AI output for Manim
│   └── manim_automator.py    # Automates Manim scene generation
├── data/
│   └── sample_kg.json        # Example Knowledge Graph data
├── manim_scenes/
│   └── quick_scene.py        # Sample Manim animation
├── assets/
│   └── architecture.png      # Visual architecture diagram
├── main.py                   # FastAPI backend application
├── requirements.txt          # Project dependencies
├── design.md                 # Detailed design document
└── pseudo_code.md            # Pseudocode for the pipeline logic

    ✅ Clear folder hierarchy separates core logic, data, visuals, and scripts for better readability and collaboration.

🛠️ Technical Stack

    Backend: FastAPI

    Knowledge Graph: Neo4j / RDF Store

    AI: Gemini / GPT API

    Video Generation: Manim Community Edition

    Databases / Caching: PostgreSQL / Redis

🚧 Trade-offs & Design Decisions

    Knowledge Graph vs Relational DB: Graph D<img width="884" height="671" alt="Screenshot from 2025-09-15 13-50-04" src="https://github.com/user-attachments/assets/267ca500-b784-4ae2-ab94-38985acf9416" />
B is used to model complex, interconnected relationships enabling semantic search; avoids costly joins in SQL.

    AI API vs Custom NLP: LLM API chosen for fast, high-quality content generation; custom NLP avoided due to time constraints and complexity.

    Manim vs PowerPoint Animations: Programmatic approach allows full automation and scalability; PowerPoint is manual and not suitable for automated pipelines.
