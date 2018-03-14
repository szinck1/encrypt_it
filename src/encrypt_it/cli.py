import click
from encrypt_it.app import app


@click.command()
def main() -> None:
    app.run(debug=True, host='0.0.0.0')
