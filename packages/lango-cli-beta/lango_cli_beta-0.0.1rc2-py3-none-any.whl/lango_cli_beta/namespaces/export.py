"""
CLI commands
"""

from rich import print as rich_print

from lango_cli_beta.constants import BASE_DOCKERFILE


def export_cli() -> None:
    # write a new Dockerfile using the contents above
    with open("Dockerfile", "w") as f:
        f.write(BASE_DOCKERFILE)
    rich_print("[bold]Dockerfile created [green]successfully[/green][/bold]")
