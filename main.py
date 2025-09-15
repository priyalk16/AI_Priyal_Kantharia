import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Import the core modules you created
from core.kg_connector import KnowledgeGraphConnector
from core.llm_generator import generate_content
from core.formatter import format_manim_data
from core.manim_automator import render_manim_video

# Load environment variables from a .env file (for local development)
load_dotenv()

app = FastAPI(
    title="Edu-Viz: AI-Powered Educational Videos",
    description="An API to generate animated educational videos from a Knowledge Graph."
)

class ConceptRequest(BaseModel):
    """
    Pydantic model for the request body.
    Ensures the user provides a 'concept' as a string.
    """
    concept: str

@app.post("/generate_video", response_model=dict)
def generate_video(request: ConceptRequest):
    """
    **Endpoint to generate a video for a given concept.**

    The process involves:
    1. Retrieving data from the Knowledge Graph.
    2. Generating a script and slides using an AI.
    3. Formatting the content for Manim.
    4. Rendering the final animated video.
    """
    try:
        # Step 1: Connect to Knowledge Graph and retrieve data
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "password")
        
        kg_connector = KnowledgeGraphConnector(uri, user, password)
        kg_data = kg_connector.get_concept_data(request.concept)
        kg_connector.close()

        if not kg_data:
            raise HTTPException(
                status_code=404,
                detail=f"Concept '{request.concept}' not found in the Knowledge Graph."
            )

        # Step 2: AI Generation Layer
        generated_content = generate_content(kg_data, request.concept)
        
        # Step 3: Formatter Layer
        formatted_data = format_manim_data(generated_content)
        
        # Step 4: Manim Automation Layer
        video_path = render_manim_video(formatted_data)
        
        if not video_path:
            raise HTTPException(
                status_code=500,
                detail="Video rendering failed. Check Manim logs for details."
            )
        
        return {"message": "Video generated successfully!", "video_path": video_path}
    
    except Exception as e:
        # Catch any unexpected errors and return a 500 status code
        raise HTTPException(status_code=500, detail=str(e))
