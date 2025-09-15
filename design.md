# Design Document

## Problem Statement
Build an AI-powered system that automates the creation of educational videos from a knowledge graph using Manim. Students can request a concept, and the system generates slides, scripts, and animations.

---

## Technical Approach
1. **Knowledge Graph**  
   - Store book content and concepts in a graph database (Neo4j).  
   - Enable semantic search to retrieve related concepts.  

2. **AI Module**  
   - Use LLMs (e.g., Gemini / GPT) to generate:  
     - Explanatory slides  
     - Detailed narration script  

3. **Slide & Script Formatter**  
   - Convert AI output into structured Markdown/JSON for consistency.  

4. **Manim Automation**  
   - Automatically render animations based on slide + script data.  

5. **Backend Orchestration**  
   - Python FastAPI backend to manage the pipeline (query → retrieval → AI → Manim → video).  

6. **Storage & Retrieval**  
   - Store generated videos, slides, and scripts for reuse.  

**Trade-offs**  
- Using LLMs → faster content generation but limited control over accuracy.  
- Using Manim → professional animations but requires render time.  
- Skipped advanced DB design for 90-minute scope, but scalable later.

---

## Pseudo Code
```pseudo
function get_concept(concept):
    data = query_knowledge_graph(concept)
    slides = ai_generate_slides(data)
    script = ai_generate_script(slides)
    video = manim_render(slides, script)
    return video
