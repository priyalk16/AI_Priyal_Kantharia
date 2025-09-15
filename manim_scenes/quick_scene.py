from manim import *

class QuickScene(Scene):
    def construct(self):
        title = Text("Graph Traversal", font_size=56)
        subtitle = Text("Automated Learning with Edu-Viz", font_size=36).next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)

