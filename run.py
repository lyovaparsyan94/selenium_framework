import os
from multiprocessing import Pool

from helpers.argument_parser import parse_arguments
from helpers.helpers import create_run_command
from helpers.runner_helpers import run_command


def set_environment_variables(arguments):
    os.environ['url'] = arguments.url


def run():
    arguments = parse_arguments()
    command = create_run_command(arguments=arguments)
    set_environment_variables(arguments=arguments)

    with Pool(processes=3) as pool:
        for browser in arguments.browser:
            pool.apply(run_command, kwds={'command': command, 'browser': browser})


if __name__ == '__main__':
    run()
