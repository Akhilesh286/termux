import typer
from rich import *
from rich.console import Console
console = Console()
def main(name: str,num: int ):
    console.print(name, style="bold green")
    
if __name__ == "__main__":
    typer.run(main)