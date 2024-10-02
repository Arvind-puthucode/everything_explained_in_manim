from manim import *
import random

class BrewingAnalogy(Scene):
    def construct(self):
        # Get frame dimensions
        frame_width = config.frame_width
        frame_height = config.frame_height

        # Set up the split screen
        left_side = Rectangle(width=frame_width/2, height=frame_height, stroke_width=0)
        left_side.shift(LEFT * frame_width/4)
        right_side = Rectangle(width=frame_width/2, height=frame_height, stroke_width=0)
        right_side.shift(RIGHT * frame_width/4)

        # Create coffee maker and pot
        coffee_maker = SVGMobject("data/coffee-machine-svgrepo-com.svg")  # You'll need to create or find this SVG
        coffee_pot = Rectangle(width=1, height=1.5, fill_color="#4E3524", fill_opacity=0)
        coffee_maker_group = VGroup(coffee_maker, coffee_pot).scale(0.8).move_to(left_side)

        # Create coffee can
        coffee_can = Cylinder(radius=1.5, height=3, fill_opacity=0.2, color=BLUE)
        coffee_can.move_to(right_side)

        # Create stock symbols
        stock_symbols = VGroup(*[Text("$", font_size=24) for _ in range(20)])
        for symbol in stock_symbols:
            symbol.move_to(coffee_can.get_center() + np.array([
                random.uniform(-1, 1),
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            ]))

        # Add elements to the scene
        self.play(
            FadeIn(coffee_maker_group),
            FadeIn(coffee_can),
            FadeIn(stock_symbols)
        )

        # Animate coffee brewing and stocks growing
        self.play(
            coffee_pot.animate.set_fill(opacity=1),
            stock_symbols.animate.scale(1.5).set_color(YELLOW),
            run_time=10
        )

        # Add title
        title = Text("Coffee Can Investing", font_size=48)
        subtitle = Text("Time + Patience = Growth", font_size=36)
        title_group = VGroup(title, subtitle).arrange(DOWN).to_edge(UP)

        self.play(Write(title_group))

        # Final pause
        self.wait(2)

    def create_steam(self, source):
        steam = VGroup()
        for _ in range(5):
            path = VMobject()
            path.set_points_smoothly([
                source.get_top(),
                source.get_top() + UP * random.uniform(0.5, 1) + RIGHT * random.uniform(-0.5, 0.5),
                source.get_top() + UP * random.uniform(1, 1.5) + RIGHT * random.uniform(-0.25, 0.25)
            ])
            steam.add(path)
        return steam

# Remember to add any necessary imports at the top of your file