from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich import print


class EndScreenUI:
    def __init__(self):
        self.layout = Layout(name="Retrace")

    def make_layout(self):
        self.layout.split(Layout(name="top", ratio=2),
                          Layout(name="middle", ratio=3),
                          Layout(name="bottom", ratio=4))

        self.layout["top"].update(self.create_header_panel())
        self.layout["middle"].update(self.create_you_won_panel())
        self.layout["bottom"].update(self.create_user_input_panel())

    def update_layout(self):
        self.make_layout()
        print(self.layout)

    def create_user_input_panel(self) -> Panel:
        intro_text = """    
        
Amidst the dilapidated cities and desolate landscapes, your journey leads you to a chilling revelation: the [bold red]Memory Extractor[/bold red]. A device designed to erase the pain of the past. The scarred world around tells a heart-wrenching tale of chaos and downfall. Solar flares eradicated the core of our civilization, leaving behind a lawless realm where looters and warring nations reigned supreme.

The once vibrant tapestry of human life, now appears faded. The streets, once bustling with laughter and love, echo with an eerie silence. You've searched far and wide, hoping against hope, but it appears you're the last remnant of a bygone era.

With the weight of this reality pressing down, you're faced with a harrowing choice. Do you continue on, living out your days amidst the echoes of a shattered world, or do you use the Memory Extractor once more? To forget, to start afresh, to experience the puzzle of existence anew.

The decision is yours. Will you bear the burden of knowledge or choose blissful oblivion? Whatever your choice, [bold cyan]the legacy of humanity rests in your hands[/bold cyan]. 
        
        """
        return Panel(Align(intro_text, align="left", vertical="middle"), title="End Game")

    def create_header_panel(self) -> Panel:
        header_logo = """[bold cyan]╦═╗┌─┐┌┬┐┬─┐┌─┐┌─┐┌─┐       ╔═╗┌─┐┬─┐┌─┐┌─┐┌┬┐┌┬┐┌─┐┌┐┌  ╔═╗┌─┐┌┬┐┬ ┬┌─┐
╠╦╝├┤  │ ├┬┘├─┤│  ├┤   ───  ╠╣ │ │├┬┘│ ┬│ │ │  │ ├┤ │││  ╠═╝├─┤ │ ├─┤└─┐
╩╚═└─┘ ┴ ┴└─┴ ┴└─┘└─┘       ╚  └─┘┴└─└─┘└─┘ ┴  ┴ └─┘┘└┘  ╩  ┴ ┴ ┴ ┴ ┴└─┘[/bold cyan]"""
        return Panel(Align(header_logo, align="center", vertical="middle"))

    def create_you_won_panel(self):
        win_ascii = """[bold cyan]
 █████ █████                                                       ███████ 
░░███ ░░███                                                       ███░░░███
 ░░███ ███ ██████  █████ ████    █████ ███ █████ ██████  ████████░░░   ░███
  ░░█████ ███░░███░░███ ░███    ░░███ ░███░░███ ███░░███░░███░░███ ███████ 
   ░░███ ░███ ░███ ░███ ░███     ░███ ░███ ░███░███ ░███ ░███ ░███░███░░░  
    ░███ ░███ ░███ ░███ ░███     ░░███████████ ░███ ░███ ░███ ░███░░░      
    █████░░██████  ░░████████     ░░████░████  ░░██████  ████ ████████     
   ░░░░░  ░░░░░░    ░░░░░░░░       ░░░░ ░░░░    ░░░░░░  ░░░░ ░░░░░░░░      
        [/bold cyan]"""
        return Panel(Align(win_ascii, align="center", vertical="middle"))
