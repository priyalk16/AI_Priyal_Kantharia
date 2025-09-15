# core/manim_automator.py

import subprocess
import textwrap
import os

def render_manim_video(formatted_data: dict, output_path="videos") -> str:
    """
    Programmatically generates Manim code and renders a video.
    """
    scene_name = "AutomatedVideoScene"
    file_path = f"manim_scenes/{scene_name}.py"

    # Generate the Manim scene code dynamically
    manim_code = f"""
from manim import *

class {scene_name}(Scene):
    def construct(self):
        # The formatted data from the AI
        data = {formatted_data}

        # Example animation logic
        for slide in data["slides"]:
            title = Text(slide["title"]).to_edge(UP)
            self.play(Write(title))

            points_group = VGroup()
            for i, point_text in enumerate(slide["points"]):
                point = Text(f"- {{point_text}}").scale(0.7)
                if i > 0:
                    point.next_to(points_group, DOWN, aligned_edge=LEFT)
                points_group.add(point)

            points_group.to_edge(LEFT).shift(UP*1.5)
            self.play(FadeIn(points_group))
            self.wait(3)
            self.play(FadeOut(VGroup(title, points_group)))

        # You would also add logic to sync with the narration script here.

        # Animate the final slide or conclusion
        final_text = Text("Thank you for watching!").to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)
    """

    with open(file_path, "w") as f:
        f.write(textwrap.dedent(manim_code))

    # Render the video using the Manim CLI
    # This command requires Manim to be installed
    # The -ql flag renders a low-quality video for quick testing
    command = [
        "manim", "-ql", file_path, scene_name,
        "--media_dir", os.path.abspath(output_path)
    ]

    try:
        subprocess.run(command, check=True)
        print("Video rendered successfully.")
        return f"{output_path}/{scene_name}.mp4"
    except subprocess.CalledProcessError as e:
        print(f"Manim rendering failed: {e}")
        return ""
