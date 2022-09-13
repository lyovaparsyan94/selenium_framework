import os
from subprocess import call


def run_command(command, browser):
    """
    Run command in subprocess.
    :param command: pytest run command
    :param browser: Browser
    :return:
    """

    # Create os environment variable for current process
    os.environ['browser'] = browser
    command_for_subprocess = command.split(' ')

    # subprocess command expect iterable as running argument (list in that case)
    # exit_code 0 meaning success, other codes mean fail
    exit_code = call(command_for_subprocess)
    ...

    # TODO handle failed subprocess exit code
