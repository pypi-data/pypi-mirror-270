#!/usr/bin/env python3

# Bundle class, pylint: disable=too-few-public-methods
class Bundle:

    # Names
    NAME: str = 'gitlab-projects-migrate'

    # Details
    DESCRIPTION: str = 'Migrate GitLab projects from a GitLab group to another GitLab\'s group'

    # Sources
    REPOSITORY: str = 'https://gitlab.com/AdrianDC/gitlab-projects-migrate'

    # Environment
    ENV_GITLAB_INPUT_TOKEN: str = 'GITLAB_INPUT_TOKEN'
    ENV_GITLAB_OUTPUT_TOKEN: str = 'GITLAB_OUTPUT_TOKEN'
    ENV_GITLAB_TOKEN: str = 'GITLAB_TOKEN'
