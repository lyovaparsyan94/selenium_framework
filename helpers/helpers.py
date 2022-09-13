import os

from helpers.constants import DRIVERS_MAPPER


def create_run_command(arguments):
    """
    Create pytest run command.
    :param arguments: Command line arguments
    :return: pytest command
    """

    arguments.test = [f'test_{test}' for test in arguments.test]
    tests = f'-k {" ".join(arguments.test)}' if arguments.test else ''
    marks = f'-m {" ".join(arguments.mark)}' if arguments.mark else ''
    command = f'pytest -s {tests} {marks}'
    return command


def get_webdriver(**options):
    """
    Getting and configuring selenium webdriver.
    :param options: Driver options.
    :return: Webdriver object
    """

    browser = os.environ['browser']

    webdriver = DRIVERS_MAPPER[browser].get('webdriver')
    manager = DRIVERS_MAPPER[browser].get('manager')
    webdriver_options = DRIVERS_MAPPER[browser].get('options')
    service_object = DRIVERS_MAPPER[browser].get('service')

    # TODO should be implemented headless mode
    if browser != 'safari':
        service = service_object(executable_path=manager().install())
        driver = webdriver(service=service,
                           options=webdriver_options(**options))
    else:
        driver = webdriver()

    return driver
