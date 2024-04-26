import toml
import click
from pathlib import Path

from svtter_template_creator import __version__, lib, repl as r, utils as u


# create a config file.
u.create_config()


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--name",
    prompt="template name",
    help="The template need to create",
    type=click.Choice(lib.get_choice()),
)
def create(name):
    """
    create template via name
    """
    lib.create(name)


@click.command()
def version():
    """show version information"""
    click.echo(f"ttc version is: {__version__}")


@click.command(help="start a repl environment")
def repl():
    click.echo(f"ttc version is: {__version__}")
    r.repl()


@click.command(help="write version to __init__.py and pyproject.toml")
@click.option("--version", help="The new verison!", required=True)
def write(version):
    filepath = "src/ttc/__init__.py"
    with open(filepath, "w") as f:
        f.write(f'__version__ = "{version}"')

    p = Path("./pyproject.toml")
    res = toml.load(p)
    res["tool"]["poetry"]["version"] = version
    # write back
    with open(p, "w") as f:
        toml.dump(res, f)


@click.command(help="show the config file")
def config():
    click.echo("-----------------------------")
    click.echo("file path:")
    click.echo(u.get_config().path)
    click.echo("-----------------------------")
    click.echo("config content:")
    click.echo("-----------------------------")
    click.echo(u.get_config().content)


enabled_cmd = [
    create,
    version,
    write,
    repl,
    config,
]

for c in enabled_cmd:
    cli.add_command(c)
