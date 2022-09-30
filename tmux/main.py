import click
import libtmux
import os
from tqdm import tqdm


@click.group()
def cli_1():
    pass


@cli_1.command()
@click.option('-n', '--number', required=True, type=click.IntRange(min=1),
              help='Provide number of environments that should be run')
def start(number):
    """
    Command run in parallel N (`number`) isolated Jupyter Notebook environments using tmux. A new tmux-session with
    N windows is being created, in each of which the environment is running.
    """
    session = server.new_session()
    pane = session.attached_window.attached_pane
    progress_bar = tqdm(desc='Starting environments', total=number)
    run_commands(pane, progress_bar)

    for i in range(number - 1):
        window = session.new_window(attach=False)
        pane = window.attached_pane
        run_commands(pane, progress_bar)
    progress_bar.close()


@click.group()
def cli_2():
    pass


@cli_2.command()
@click.option('-s', '--session-id', required=True, type=click.IntRange(min=0),
              help='Tmux-session ID where environments are running')
@click.option('-n', '--number', required=True, type=click.IntRange(min=0),
              help='The sequence number of environment that should be killed')
def stop(session_id, number):
    """
    Stop the n-th (`number`) environment at given tmux-session ID (`session_id)
    """
    session = server.get_by_id(f'${session_id}')
    if session is None:
        click.echo(f'Tmux-session ${session_id} was not found')
        return

    found_pane = None

    for window in session.list_windows():
        for pane in window.list_panes():
            if pane.get('pane_id')[1:] == str(number):
                found_pane = pane
                break

    if found_pane is None:
        click.echo(f'At session {session_id} no environment with such number {number} running')
        return

    found_pane.cmd('kill-pane')


@click.group()
def cli_3():
    pass


@cli_3.command()
@click.option('-s', '--session-id', required=True, type=click.IntRange(min=0),
              help='Tmux-session ID where environments are running')
def stop_all(session_id):
    """
    Completely stop all environments at given tmux-session ID (`session_id`) by killing this session.
    """
    session_to_stop = server.get_by_id(f'${session_id}')
    if session_to_stop is None:
        click.echo(f'Tmux-session ${session_id} was not found')
        return

    os.system(f'tmux kill-session -t {session_id}')
    click.echo(f'Tmux-session ${session_id} has been stopped')


def run_commands(pane, progress_bar, base_dir='./', port=10916):
    """
    Run commands at defined tmux-pane (`pane`), execution repels by provided directory (`base_dir`). For each user
    a specific is being created using pane ID(enumerated via tmux), at these folders python virtual environment is
    being created using venv. And inside activated virtual environment Jupyter Notebook environment is being started
    on a separate network port with a separate (unique and random) token).

    :param pane: tmux-pane to run commands at
    :param progress_bar: progress bar associated with environment loading
    :param base_dir: base directory to work at pane, defaults to './'
    :param port: network port to start environment, defaults to 10916
    """
    folder_num = pane.get('pane_id')[1:]
    folder = base_dir + folder_num
    pane.send_keys(f'mkdir {folder}; cd {folder}')
    env = f'venv_{folder_num}'
    pane.send_keys(f'python3 -m venv {env}')
    pane.send_keys(f'source {env}/bin/activate')

    port += int(folder_num)
    token_ = os.urandom(24).hex()
    pane.send_keys(f'jupyter notebook --ip="*" --port {port} --no-browser\
    --NotebookApp.token="{token_}" --NotebookApp.notebook_dir="{base_dir}"')

    session_id = pane.window.session.get('session_id')[1:]
    click.echo(f'At tmux-session № {session_id} Jupyter notebook environment № {folder_num} \
    started at port {port} with token {token_}')
    progress_bar.update(1)


if __name__ == '__main__':
    server = libtmux.Server()
    cli = click.CommandCollection(sources=[cli_1, cli_2, cli_3])
    cli()
