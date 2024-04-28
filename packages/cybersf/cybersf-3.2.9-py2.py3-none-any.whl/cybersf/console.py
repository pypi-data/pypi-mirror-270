from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

# Install Traceback
install()

# Console Setup
cybersf_theme = Theme(
    {
        "command": "black on white",
        "warning": "bold yellow",
    }
)
console = Console(theme=cybersf_theme)
