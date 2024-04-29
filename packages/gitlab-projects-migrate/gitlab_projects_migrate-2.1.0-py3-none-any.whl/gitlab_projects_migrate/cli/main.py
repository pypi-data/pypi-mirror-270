#!/usr/bin/env python3

# Standard libraries
from argparse import (_ArgumentGroup, ArgumentParser, Namespace, RawTextHelpFormatter)
from os import environ
from shutil import get_terminal_size
from sys import exit as sys_exit

# Components
from ..package.bundle import Bundle
from ..package.version import Version
from ..prints.colors import Colors
from ..system.platform import Platform
from .entrypoint import Entrypoint

# Main, pylint: disable=too-many-statements
def main() -> None:

    # Variables
    group: _ArgumentGroup
    result: bool = False

    # Arguments creation
    parser: ArgumentParser = ArgumentParser(
        prog=Bundle.NAME,
        description=f'{Bundle.NAME}: {Bundle.DESCRIPTION}',
        add_help=False,
        formatter_class=lambda prog: RawTextHelpFormatter(
            prog,
            max_help_position=30,
            width=min(
                120,
                get_terminal_size().columns - 2,
            ),
        ),
    )

    # Arguments internal definitions
    group = parser.add_argument_group('internal arguments')
    group.add_argument(
        '-h',
        '--help',
        dest='help',
        action='store_true',
        help='Show this help message',
    )
    group.add_argument(
        '--version',
        dest='version',
        action='store_true',
        help='Show the current version',
    )

    # Arguments credentials definitions
    group = parser.add_argument_group('credentials arguments')
    group.add_argument(
        '-I',
        dest='input_token',
        default=environ.get(
            Bundle.ENV_GITLAB_INPUT_TOKEN,
            environ.get(
                Bundle.ENV_GITLAB_TOKEN,
                '',
            ),
        ),
        help=f'Input GitLab API token (default: {Bundle.ENV_GITLAB_INPUT_TOKEN}'
        f' or {Bundle.ENV_GITLAB_TOKEN} environments)',
    )
    group.add_argument(
        '-O',
        dest='output_token',
        action='store',
        default=environ.get(
            Bundle.ENV_GITLAB_OUTPUT_TOKEN,
            environ.get(
                Bundle.ENV_GITLAB_TOKEN,
                '',
            ),
        ), #
        help=f'Output GitLab API token (default: {Bundle.ENV_GITLAB_OUTPUT_TOKEN}'
        f', {Bundle.ENV_GITLAB_TOKEN} environments,'
        ' or INPUT_TOKEN argument)',
    )

    # Arguments migration definitions
    group = parser.add_argument_group('migration arguments')
    group.add_argument(
        '--dry-run',
        dest='dry_run',
        action='store_true',
        help='Enable dry run mode to check without saving',
    )
    group.add_argument(
        '--exclude-group',
        dest='exclude_group',
        action='store_true',
        help='Exclude parent group migration',
    )
    group.add_argument(
        '--exclude-subgroups',
        dest='exclude_subgroups',
        action='store_true',
        help='Exclude children subgroups migration',
    )
    group.add_argument(
        '--exclude-projects',
        dest='exclude_projects',
        action='store_true',
        help='Exclude children projects migration',
    )
    group.add_argument(
        '--keep-members',
        dest='keep_members',
        action='store_true',
        help='Keep input members after importing on output GitLab',
    )
    group.add_argument(
        '--overwrite',
        dest='overwrite',
        action='store_true',
        help='Overwrite existing projects on output GitLab',
    )

    # Arguments general settings definitions
    group = parser.add_argument_group('general settings arguments')
    group.add_argument(
        '--set-avatar',
        dest='set_avatar',
        action='store',
        metavar='FILE',
        help='Set avatar of GitLab output projects and groups',
    )
    group.add_argument(
        '--update-description',
        dest='update_description',
        action='store_true',
        help='Update description of GitLab output projects and groups automatically',
    )

    # Arguments positional definitions
    group = parser.add_argument_group('positional arguments')
    group.add_argument(
        dest='input_gitlab',
        action='store',
        nargs='?',
        default='https://gitlab.com',
        help='Input GitLab URL (default: https://gitlab.com)',
    )
    group.add_argument(
        dest='input_path',
        action='store',
        nargs='?',
        help='Input GitLab group or project path',
    )
    group.add_argument(
        dest='output_gitlab',
        action='store',
        nargs='?',
        default='https://gitlab.com',
        help='Output GitLab URL (default: https://gitlab.com)',
    )
    group.add_argument(
        dest='output_group',
        action='store',
        nargs='?',
        default='',
        help='Output GitLab group',
    )

    # Arguments parser
    options: Namespace = parser.parse_args()

    # Help informations
    if options.help:
        print(' ')
        parser.print_help()
        print(' ')
        Platform.flush()
        sys_exit(0)

    # Prepare colors
    Colors.prepare()

    # Version informations
    if options.version:
        print(
            f'{Bundle.NAME} {Version.get()} from {Version.path()} (python {Version.python()})'
        )
        Platform.flush()
        sys_exit(0)

    # Arguments validation
    if not options.input_token or not options.input_gitlab or not options.input_path \
            or not options.output_gitlab or not options.output_group:
        print(' ')
        parser.print_help()
        print(' ')
        Platform.flush()
        sys_exit(1)

    # Arguments adaptations
    if not options.output_token:
        options.output_token = options.input_token

    # Header
    print(' ')
    Platform.flush()

    # CLI entrypoint
    result = Entrypoint.cli(options)

    # Footer
    print(' ')
    Platform.flush()

    # Result
    if result:
        sys_exit(0)
    else:
        sys_exit(1)

# Entrypoint
if __name__ == '__main__': # pragma: no cover
    main()
