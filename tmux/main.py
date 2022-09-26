import click
import libtmux
import os


@click.group()
def cli_1():
    pass


@cli_1.command()
@click.option('-n', '--number', required=True, type=click.IntRange(min=1),
              help='Provide number of users jupyter notebooks that should be run')
def start(number, base_dir='./'):
    """Command on cli_1"""
    click.echo('Command start on cli_1')
    click.echo(f'start running {number} envs')

    session = server.new_session()
    pane = session.attached_window.attached_pane
    run_commands(pane)

    for i in range(number - 1):
        window = session.new_window(attach=False)
        pane = window.attached_pane
        run_commands(pane)


@click.group()
def cli_2():
    pass


@cli_2.command()
@click.option('-s', '--session-id', required=True, type=click.IntRange(min=0),
              help='Tmux-session id where environments are running')
@click.option('-n', '--number', required=True, type=click.IntRange(min=0),
              help='The sequence number of environment that can be killed')
def stop(session_id, number):
    """Command on cli_2"""
    click.echo('Command stop on cli_2')
    click.echo(f'stop env with number {number} at session {session_id}')

    session = server.get_by_id(f'${session_id}')
    found_pane = None

    for window in session.list_windows():
        for pane in window.list_panes():
            if pane.get('pane_id')[1:] == str(number):
                found_pane = pane
                pane.window.kill_window()
                break

    if found_pane is None:
        print('No environment with such id running')
        return


@click.group()
def cli_3():
    pass


@cli_3.command()
@click.option('-s', '--session-id', required=True, type=click.IntRange(min=0),
              help='Tmux-session number where environments are running')
def stop_all(session_id):
    """Command on cli_3"""
    click.echo('Command stop_all on cli_3')
    click.echo(f'find session by id {session_id} and stop it')
    session_to_stop = server.get_by_id(f'${session_id}')
    click.echo(f'{session_to_stop}')

    os.system(f'tmux kill-session -t {session_id}')
    click.echo(f'stop session {session_id}')


cli = click.CommandCollection(sources=[cli_1, cli_2, cli_3])


def run_commands(pane, base_dir='./', port=10916):
    folder_num = pane.get('pane_id')[1:]
    folder = base_dir + folder_num
    pane.send_keys(f'mkdir {folder}')
    pane.send_keys(f'cd {folder}')
    env = f'venv_{folder_num}'
    pane.send_keys(f'python3 -m venv {env}')
    pane.send_keys(f'source {env}/bin/activate')

    port += int(folder_num)
    print(port)
    token_ = os.urandom(24).hex()
    pane.send_keys(f'jupyter notebook --ip=$(hostname -i) --port {port} --no-browser --NotebookApp.token="{token_}" \
                    --NotebookApp.notebook_dir="{base_dir}"')


if __name__ == '__main__':
    server = libtmux.Server()
    cli()
