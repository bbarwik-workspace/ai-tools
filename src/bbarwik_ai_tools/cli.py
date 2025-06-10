from typing import Annotated

import rich
import typer

from . import __version__

# Create the main Typer application
app = typer.Typer(
    name="bbarwik-ai-tools",
    help="A simple CLI that prints Hello World.",
    add_completion=False,
    invoke_without_command=True,
)


def version_callback(value: bool):
    """Prints the version of the package and exits."""
    if value:
        rich.print(f"bbarwik-ai-tools version: [bold green]{__version__}[/bold green]")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show the application's version and exit.",
        ),
    ] = False,
):
    """
    A simple CLI that prints Hello World.
    """
    rich.print("Hello World")


# This is for Hatch to run the app
if __name__ == "__main__":
    app()
