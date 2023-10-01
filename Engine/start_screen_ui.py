from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich import print


class StartScreenUI:
    def __init__(self):
        self.layout = Layout(name="Retrace")

    def make_layout(self):
        self.layout.split(Layout(name="top", ratio=3),
                          Layout(name="bottom", ratio=5))

        self.layout["top"].update(self.create_header_panel())
        self.layout["bottom"].update(self.create_user_input_panel())

    def update_layout(self):
        self.make_layout()
        print(self.layout)

    def create_user_input_panel(self) -> Panel:
        intro_text = """
        You awaken, [bold red]head throbbing[/bold red], in a dimly lit room. [bold red]Panic[/bold red] sets in briefly as nothing seems familiar. Blinking, you push yourself up, trying to recall the [bold red]memories[/bold red] that should tether you to [bold cyan]reality[/bold cyan]. But they’re gone. All of them. There's an unsettling weight to the silence, devoid of the hum of city life or the distant chatter of people.

As you survey the room, disjointed sensations wash over you. The rustic wooden furniture, the worn-out rug underfoot, the faint aroma of old books — it's unfamiliar, and yet... something within whispers that you've been here before. Was this your home? But why does it feel like you're [bold red]intruding[/bold red]?

The world outside the window is eerily still. An ominous heaviness hangs in the air. There's a nagging feeling, a [bold red]puzzle[/bold red] waiting to be pieced together.

[bold cyan]Determination[/bold cyan] grows within. To uncover the [bold red]truth[/bold red], you need to venture out. Maybe, just maybe, if you search for [bold cyan]clues[/bold cyan], the world outside might make sense again.
        
        """
        return Panel(Align(intro_text, align="left", vertical="middle"), title="Intro")

    def create_header_panel(self) -> Panel:
        header_logo = """[bold cyan]╦═╗┌─┐┌┬┐┬─┐┌─┐┌─┐┌─┐       ╔═╗┌─┐┬─┐┌─┐┌─┐┌┬┐┌┬┐┌─┐┌┐┌  ╔═╗┌─┐┌┬┐┬ ┬┌─┐
╠╦╝├┤  │ ├┬┘├─┤│  ├┤   ───  ╠╣ │ │├┬┘│ ┬│ │ │  │ ├┤ │││  ╠═╝├─┤ │ ├─┤└─┐
╩╚═└─┘ ┴ ┴└─┴ ┴└─┘└─┘       ╚  └─┘┴└─└─┘└─┘ ┴  ┴ └─┘┘└┘  ╩  ┴ ┴ ┴ ┴ ┴└─┘[/bold cyan]"""
        return Panel(Align(header_logo, align="center", vertical="middle"))
