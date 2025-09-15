# Design Document

## Problem Statement
The problem is to **reimagine education** by turning static textbook knowledge into **AI-powered animated videos**.  
Instead of reading dense chapters, students can simply query a concept (e.g., “Graph Traversal” or “Black Hole Formation”), and the system will:  
- Retrieve structured knowledge from a **Knowledge Graph**  
- Generate **slides + narration scripts** using AI  
- Convert the content into **animated videos** with Manim  

This ensures **faster learning, engaging visuals, and personalized explanations** for diverse domains like **Data Structures, GIS, and Space Tech**.

---

## Technical Approach

1. **Knowledge Graph Layer**  
   - Use Neo4j / RDF store for structured storage.  
   - Nodes = concepts, Edges = relationships.  
   - Semantic search for retrieving relevant nodes.  

2. **AI Generation Layer**  
   - Use LLMs (Gemini/GPT) for:  
     - Slide generation (bullet points, headings, examples).  
     - Narration script (detailed step-by-step explanation).  

3. **Formatter Layer**  
   - Standardize AI output → JSON or Markdown.  
   - Ensures Manim can parse structured content.  

4. **Manim Automation Layer**  
   - Auto-generate animations for slides.  
   - Synchronize with narration for video output.  

5. **Backend Orchestration**  
   - FastAPI backend manages the flow:  
     User query → Graph Retrieval → AI Generation → Formatter → Manim → Video.  

6. **Storage & Retrieval**  
   - Save slides, scripts, and final videos.  
   - Provide API for retrieving past results.  

---

## Trade-offs
- **Graph DB vs SQL** → Graph chosen for relationships; SQL discarded for scalability.  
- **AI API vs Custom NLP** → API chosen for speed, custom NLP for future precision.  
- **Manim vs PowerPoint Animations** → Manim chosen for automation and scalability.  

---

## Pseudo Code

```pseudo
function generate_video(concept):
    data = query_knowledge_graph(concept)
    slides = AI_generate_slides(data)
    script = AI_generate_script(slides)
    formatted_content = format(slides, script)
    video = manim_render(formatted_content)
    store(video)
    return video
