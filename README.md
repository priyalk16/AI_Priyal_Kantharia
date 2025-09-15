🎓 Edu-Viz: AI-Powered Educational Videos

✨ Project Overview

Edu-Viz is a groundbreaking project that transforms static textbook knowledge into dynamic, AI-powered animated videos. By bridging the gap between dense theory and engaging visuals, our platform offers a personalized learning experience for complex subjects like Data Structures, GIS, and Space Tech. Instead of reading, students can simply query a concept and watch it come to life.

<br>

⚙️ How It Works

Our system is an orchestrated pipeline of powerful, modern technologies. The process flows from a user query to a final video, managed by a robust backend.

    User Query: A student enters a concept (e.g., "Graph Traversal").

    Knowledge Retrieval: Our system queries a Knowledge Graph (built on Neo4j) to fetch structured information, concepts, and relationships.

    Content Generation: An AI Layer (using models like Gemini or GPT) takes the retrieved data and generates a detailed narration script and a bullet-point outline for a series of slides.

    Content Formatting: The raw AI output is standardized into a structured format (JSON), ensuring consistency and machine-readability.

    Video Animation: A Manim Automation Layer parses the formatted content and programmatically generates the animations and visuals for each slide, perfectly synchronized with the narration script.

    Video Output: The final MP4 video is rendered and stored for future retrieval, ready to be shared and watched.

<br>

🚀 Key Features

    Personalized Learning: Get explanations tailored to specific queries, moving beyond one-size-fits-all textbooks.

    Engaging Visuals: Utilize high-quality, auto-generated animations to simplify complex topics.

    Scalable & Efficient: The automated pipeline allows for the rapid creation of educational content for diverse domains.

    Structured Knowledge: Our Knowledge Graph foundation ensures accuracy and provides a clear, interconnected view of subjects.

<br>

📦 Repository Structure

A clear file structure helps collaborators and evaluators quickly understand the project layout and demonstrates a clean, organized approach to development.

/edu-viz
├── core/
│   ├── kg_connector.py          # Logic for querying the Knowledge Graph
│   ├── llm_generator.py         # AI content generation from KG data
│   ├── formatter.py             # Standardizes AI output for Manim
│   └── manim_automator.py       # Automates Manim scene generation
├── data/
│   └── sample_kg.json           # Example Knowledge Graph data
├── manim_scenes/
│   └── quick_scene.py           # Sample Manim animation to showcase
├── main.py                      # The main FastAPI backend application
├── requirements.txt             # Project dependencies
├── design.md                    # Detailed design document
└── pseudo_code.md               # Pseudocode for the pipeline logic

<br>

🛠️ Technical Stack

    Backend: FastAPI

    Knowledge Graph: Neo4j / RDF Store

    AI: Gemini / GPT API

    Video Generation: Manim Community Edition

    Databases: PostgreSQL / Redis (for caching)

<br>

🚧 Trade-offs & Design Decisions

    Knowledge Graph vs. Relational DB: We chose a graph database over traditional SQL for its ability to model complex, interconnected relationships between concepts, which is crucial for semantic search and content generation. This native relationship-centric model avoids performance-intensive joins, especially for deep traversals.

    AI API vs. Custom NLP: Opting for powerful LLM APIs allows us to leverage state-of-the-art models for content creation without building custom NLP models from scratch. This enables a faster development cycle and benefits from continuous model improvements, ensuring the system remains cutting-edge.

    Manim vs. PowerPoint Animations: Manim was selected for its programmatic and declarative approach to animation. This is essential for automating the video generation process at scale, as we can define animations with code, unlike manual, labor-intensive tools like PowerPoint.

<br>


📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
