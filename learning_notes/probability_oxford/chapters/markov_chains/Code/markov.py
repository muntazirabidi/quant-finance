from manim import *

class MarkovConfig:
    """
    Central configuration class for our Markov chain animations.
    This class stores all shared styling, colors, and utility methods.
    Having these in one place makes it easier to maintain consistent 
    visual design across all scenes.
    """
    # Color palette
    TEXT_COLOR = '#E6D5AC'    # Warm, readable color for text
    BOX_COLOR = '#9D4EDD'     # Purple for boxes and borders
    NODE_COLOR = '#2196F3'    # Blue for state nodes
    ARROW_COLOR = '#757575'   # Gray for transitions
    PROBABILITY_COLOR = '#4CAF50'  # Green for probability values
    
    # Typography and sizing
    TITLE_FONT_SIZE = 60
    NORMAL_FONT_SIZE = 24
    NODE_RADIUS = 0.5
    
    @staticmethod
    def create_title_box(text):
        """
        Creates a consistently styled rectangular border around text elements.
        Args:
            text: The Manim Text object to be enclosed
        Returns:
            Rectangle object configured with standard styling
        """
        box = Rectangle(
            width=text.width + 1,
            height=text.height + 0.5,
            color=MarkovConfig.BOX_COLOR,
            fill_opacity=0
        )
        return box
    
    @staticmethod
    def create_state_node(label_text, position=ORIGIN):
        """
        Creates a standard state node with label for Markov chain diagrams.
        Args:
            label_text: Text for the state label
            position: Where to place the node (default: center)
        Returns:
            VGroup containing the node circle and its label
        """
        circle = Circle(
            radius=MarkovConfig.NODE_RADIUS,
            color=MarkovConfig.NODE_COLOR
        )
        label = Text(
            label_text,
            font_size=MarkovConfig.NORMAL_FONT_SIZE,
            color=MarkovConfig.TEXT_COLOR
        )
        circle.move_to(position)
        label.next_to(circle, DOWN)
        return VGroup(circle, label)


class MarkovTitleScene(Scene):
    """
    Opening scene that displays the title "Markov Chain".
    Demonstrates the basic animation sequence we'll build upon.
    """
    def construct(self):
        # Create title with configured styling
        title = Text(
            "Markov Chain",
            font_size=MarkovConfig.TITLE_FONT_SIZE,
            color=MarkovConfig.TEXT_COLOR
        )
        
        # Create enclosing box using our utility method
        box = MarkovConfig.create_title_box(title)
        
        # Animate elements in sequence
        self.play(
            Write(title),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(
            Create(box),
            run_time=1.5
        )
        self.wait(2)


# We can now easily add new scenes that use the same configuration

class MarkovHookScene(Scene):
    """
    Hook scene that presents a relatable weather prediction scenario
    to capture viewer attention and introduce Markov chains naturally.
    """
    def construct(self):
        # Create the question that sets up our hook
        hook_question = Text(
            "Can we predict tomorrow's weather?",
            font_size=MarkovConfig.NORMAL_FONT_SIZE * 1.5,
            color=MarkovConfig.TEXT_COLOR
        )
        
        # Create thought bubble using Manim shapes
        bubble_circle = Circle(radius=0.8, color=MarkovConfig.TEXT_COLOR)
        small_bubble1 = Circle(radius=0.2, color=MarkovConfig.TEXT_COLOR)
        small_bubble2 = Circle(radius=0.15, color=MarkovConfig.TEXT_COLOR)
        small_bubble3 = Circle(radius=0.1, color=MarkovConfig.TEXT_COLOR)
        
        # Position the bubbles
        bubble_circle.shift(UP * 1.5 + RIGHT * 0.5)
        small_bubble1.next_to(bubble_circle, DOWN + LEFT, buff=0.1)
        small_bubble2.next_to(small_bubble1, DOWN + LEFT, buff=0.05)
        small_bubble3.next_to(small_bubble2, DOWN + LEFT, buff=0.05)
        
        # Group all bubble elements
        thought_bubble = VGroup(
            bubble_circle,
            small_bubble1,
            small_bubble2,
            small_bubble3
        )
        
        # Create a stick figure looking up at the thought bubble
        stick_figure = VGroup(
            Circle(radius=0.2, color=MarkovConfig.TEXT_COLOR),  # head
            Line(ORIGIN, DOWN, color=MarkovConfig.TEXT_COLOR),  # body
            Line(DOWN*0.5, DOWN*0.5 + LEFT*0.3, color=MarkovConfig.TEXT_COLOR),  # left arm
            Line(DOWN*0.5, DOWN*0.5 + RIGHT*0.3, color=MarkovConfig.TEXT_COLOR),  # right arm
            Line(DOWN, DOWN + LEFT*0.3, color=MarkovConfig.TEXT_COLOR),  # left leg
            Line(DOWN, DOWN + RIGHT*0.3, color=MarkovConfig.TEXT_COLOR),  # right leg
        ).scale(0.8)
        
        # Position elements
        stick_figure.move_to(DOWN * 1.5)
        thought_bubble.next_to(stick_figure, UP + RIGHT)
        hook_question.to_edge(UP)
        
        # Create icons for sunny and rainy weather
        # Create more detailed weather symbols
        # Sun with rays
        sun_center = Circle(radius=0.2, color=YELLOW, fill_opacity=1)
        rays = VGroup(*[
            Line(
                start=RIGHT * 0.2,
                end=RIGHT * 0.4,
                color=YELLOW
            ).rotate(angle=i * PI/4, about_point=ORIGIN)
            for i in range(8)
        ])
        sun = VGroup(sun_center, rays).scale(0.6)
        
        # Raindrops in a more organized pattern
        def create_raindrop():
            drop = VGroup(
                Circle(radius=0.1, color=BLUE),
                Triangle(color=BLUE).scale(0.1).rotate(PI)
            )
            return drop.scale(0.5)
        
        rain = VGroup(*[
            create_raindrop().shift(
                RIGHT * (i % 2) * 0.3 + 
                DOWN * (i // 2) * 0.3
            )
            for i in range(4)
        ])
        
        # Position weather icons in thought bubble
        sun.move_to(thought_bubble.get_center() + LEFT * 0.5)
        rain.move_to(thought_bubble.get_center() + RIGHT * 0.5)
        
        # Position weather symbols in the thought bubble
        sun.move_to(bubble_circle.get_center() + LEFT * 0.4)
        rain.move_to(bubble_circle.get_center() + RIGHT * 0.4)
        
        # Refined animation sequence
        # Start with the question
        self.play(Write(hook_question), run_time=2)
        self.wait(0.5)
        
        # Introduce the character
        self.play(Create(stick_figure), run_time=1.5)
        self.wait(0.3)
        
        # Create thought bubble piece by piece
        for bubble in thought_bubble:
            self.play(Create(bubble), run_time=0.3)
        
        # Add weather symbols with a nice animation
        self.play(
            FadeIn(sun, shift=UP * 0.3),
            run_time=0.8
        )
        self.play(
            FadeIn(rain, shift=UP * 0.3),
            run_time=0.8
        )
        
        # Add a subtle bounce to the question to emphasize it
        self.play(
            hook_question.animate.scale(1.1),
            run_time=0.3
        )
        self.play(
            hook_question.animate.scale(1/1.1),
            run_time=0.3
        )
        
        self.wait(2)


if __name__ == "__main__":
    """
    When running the script directly, render with a black background
    """
    with tempconfig({"background_color": BLACK}):
        scene = MarkovTitleScene()