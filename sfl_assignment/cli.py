import click

@click.command()
@click.option('--option', default=None, help='click command option example')
@click.argument('command')
def run_command(option, command):
    click.echo(f"Running {command} with option {option}!")