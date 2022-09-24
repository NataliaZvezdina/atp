import click


@click.group()
def cli_1():
    pass


@cli_1.command()
def start():
    """Command on cli_1"""
    click.echo('Command start on cli_1')


@click.group()
def cli_2():
    pass


@cli_2.command()
def stop():
    """Command on cli_2"""
    click.echo('Command stop on cli_2')


@click.group()
def cli_3():
    pass


@cli_3.command()
def stop_all():
    """Command on cli_3"""
    click.echo('Command stop_all on cli_3')


cli = click.CommandCollection(sources=[cli_1, cli_2, cli_3])


if __name__ == '__main__':
    cli()
