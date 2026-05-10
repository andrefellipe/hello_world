import typer
from typing_extensions import Annotated

from hello_world.core import say_hello

app = typer.Typer(
    name="hello-world",
    help="A state-of-the-art CLI boilerplate tool.",
    add_completion=False,
)

@app.command()
def main(
    name: Annotated[
        str,
        typer.Option("--name", "-n", help="The name of the person to greet.")
    ] = "World"
) -> None:
    """
    Execute the core greeting logic.
    """
    message = say_hello(name)
    # Using Typer's echo for safe, cross-platform terminal printing
    typer.echo(message)

if __name__ == "__main__":
    app()
