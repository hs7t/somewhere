import typer
from rich.console import Console
from tinydb import TinyDB
from configuration import globalConfig

console = Console()
app = typer.Typer(add_completion=False) # I don't like the clutter

globalConfig["debugMode"] = True # failsafe; not unset = something went wrong

db = TinyDB('./data/streaks.json')

@app.command()
def somewhere():
    console.print("Hello, world!")

if __name__ == "__main__":
    app()

