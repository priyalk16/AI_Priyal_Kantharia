# core/formatter.py

import json

def format_manim_data(ai_output: dict) -> dict:
    """
    Formats AI-generated content into a structured JSON for Manim.
    """
    # This is a simple example. A real-world formatter would parse
    # markdown headings, bullet points, and other elements more robustly.

    formatted = {
        "slides": [],
        "script": ai_output["script"],
    }

    lines = ai_output["slides"].strip().split('\n')
    current_slide = None
    for line in lines:
        line = line.strip()
        if line.startswith("# Slide"):
            if current_slide:
                formatted["slides"].append(current_slide)
            current_slide = {"title": line.split(":", 1)[1].strip(), "points": []}
        elif line.startswith("-"):
            if current_slide:
                current_slide["points"].append(line[1:].strip())

    if current_slide:
        formatted["slides"].append(current_slide)

    return formatted
