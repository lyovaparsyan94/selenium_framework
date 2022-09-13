from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(description='Please provide running arguments.')

    parser.add_argument('--url',
                        default='https://www.google.com',
                        help='The main URL')

    parser.add_argument('-b', '--browser',
                        nargs='+',
                        choices=['chrome', 'firefox', 'safari'],
                        default=['chrome'],
                        help='Browser(s) which will run tests')

    parser.add_argument('-t', '--test',
                        default='',
                        nargs='+',
                        help='Test(s) for running. By default, all tests will run')

    parser.add_argument('-m', '--mark',
                        required=False,
                        nargs='+',
                        help='Running tests marks')

    return parser.parse_args()
