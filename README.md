# 🎓 Edu-Viz: AI-Powered Educational Videos

## ✨ Project Overview

Edu-Viz is a groundbreaking project that transforms static textbook knowledge into dynamic, AI-powered animated videos. By bridging the gap between dense theory and engaging visuals, our platform offers a personalized learning experience for complex subjects like **Data Structures, GIS, and Space Tech**.  

Instead of reading, students can simply query a concept and watch it come to life.

---

## ⚙️ How It Works

The system is an orchestrated pipeline of modern technologies. The flow is:

1. **User Query**  
   A student enters a concept (e.g., "Graph Traversal").

2. **Knowledge Retrieval**  
   The system queries a **Knowledge Graph (Neo4j)** to fetch structured information, concepts, and relationships.

3. **Content Generation**  
   AI Layer (using **Gemini/GPT**) generates:  
   - A detailed narration script  
   - Bullet-point slides  

4. **Content Formatting**  
   Standardizes AI output into a **structured JSON format**, ensuring consistency and machine-readability.

5. **Video Animation**  
   **Manim Automation Layer** parses the structured content and generates animations, synchronized with the narration.

6. **Video Output**  
   Final MP4 video is rendered and stored for future retrieval.

---

## 🚀 Key Features

- **Personalized Learning:** Tailored explanations for each query.  
- **Engaging Visuals:** High-quality animations simplify complex topics.  
- **Scalable & Efficient:** Rapid content creation across multiple domains.  
- **Structured Knowledge:** Knowledge Graph ensures accuracy and interconnected concepts.

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

    ✅ Clear hierarchy and folders separate functionality, data, visuals, and scripts for better organization.

🛠️ Technical Stack

    Backend: FastAPI

    Knowledge Graph: Neo4j / RDF Store

    AI: Gemini / GPT API

    Video Generation: Manim Community Edition

    Databases: PostgreSQL / Redis (for caching)

🚧 Trade-offs & Design Decisions

    Knowledge Graph vs Relational DB: Graph DB chosen for modeling complex, interconnected relationships enabling semantic search; avoids costly joins in SQL.

    AI API vs Custom NLP: LLM API chosen for fast content creation and continuous model improvements; custom NLP avoided due to time constraints.

    Manim vs PowerPoint Animations: Programmatic approach allows full automation and scalability; PowerPoint is manual and labor-intensive.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.


---

### ✅ Improvements in this version:
1. **Repo structure is visually clear** with folders and files properly indented.  
2. Added **assets/** folder for your architecture diagram.  
3. Key features and steps separated for **easy readability**.  
4. Trade-offs section is concise and readable.  
5. Overall formatting **looks professional and attractive** on GitHub.  

---

If you want, I can **also make a fully polished `pseudo_code.md`** and **update `design.md`** so that all your files **look consistent, professional, and submission-ready**.  

Do you want me to do that next?
