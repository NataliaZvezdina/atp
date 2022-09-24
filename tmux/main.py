import click


@click.group()
def cli_1():
    pass


@cli_1.command()
@click.option('-n', '--number', required=True, type=click.IntRange(min=1),
              help='Provide number of users jupyter notebooks that should be run')
def start(number):
    """Command on cli_1"""
    click.echo('Command start on cli_1')
    click.echo(f'start running {number} envs')


@click.group()
def cli_2():
    pass


@cli_2.command()
@click.option('-s', '--session-name', required=True, type=click.IntRange(min=0),
              help='Tmux-session number where environments are running')
@click.option('-n', '--number', required=True, type=click.IntRange(min=0),
              help='The sequence number of environment that can be killed')
def stop(session_name, number):
    """Command on cli_2"""
    click.echo('Command stop on cli_2')
    click.echo(f'stop env with number {number} at session {session_name}')


@click.group()
def cli_3():
    pass


@cli_3.command()
@click.option('-s', '--session-name', required=True, type=click.IntRange(min=0),
              help='Tmux-session number where environments are running')
def stop_all(session_name):
    """Command on cli_3"""
    click.echo('Command stop_all on cli_3')
    click.echo(f'stop all environments at session {session_name}')


cli = click.CommandCollection(sources=[cli_1, cli_2, cli_3])


if __name__ == '__main__':
    cli()
