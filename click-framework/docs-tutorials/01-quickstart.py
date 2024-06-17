import click


# Basic Concepts - Creating a Command
@click.command()
def hello():
    click.echo("Hello World!")


# Nesting Commands
@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo("Initialized the database")


@click.command()
def dropdb():
    click.echo("Dropped the database")


cli.add_command(initdb)
cli.add_command(dropdb)


# Registering Commands Later¶
@click.command()
def greet():
    click.echo("Hello, World!")


@click.group()
def group():
    pass


group.add_command(greet)


# Adding Parameters
# To add parameters, use the option() and argument() decorators:


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument("name")
def hi(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


# ANSI Colors
# The echo() function supports ANSI colors and styles. On Windows this uses colorama.

@click.command()
def colors():
    click.echo(click.style('Hello World!', fg='green'))
    click.echo(click.style('Some more text', bg='blue', fg='white'))
    click.echo(click.style('ATTENTION', blink=True, bold=True))


# Pager Support
#@click.command()
def less():
    click.echo_via_pager("\n".join(f"Line {idx}" for idx in range(200)))


""" 
If you want to use the pager for a lot of text, especially if generating everything in advance would 
take a lot of time, you can pass a generator (or generator function) instead of a string:
"""

def _generate_output():
    for idx in range(50000):
        yield f"Line {idx}\n"

@click.command()
def less():
    click.echo_via_pager(_generate_output())


# Showing Progress Bars
import time

@click.command()
def progress():
    with click.progressbar([1, 2, 3]) as bar:
        for x in bar:
            print(f"sleep({x})...")
            time.sleep(x)

if __name__ == "__main__":
    # hello()
    # cli()
    # group()
    #hi()
    #colors()
    #less()
    progress()
    
