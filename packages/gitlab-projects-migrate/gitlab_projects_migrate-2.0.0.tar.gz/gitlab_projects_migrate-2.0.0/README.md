# gitlab-projects-migrate

<!-- markdownlint-disable no-inline-html -->

[![Build](https://gitlab.com/AdrianDC/gitlab-projects-migrate/badges/main/pipeline.svg)](https://gitlab.com/AdrianDC/gitlab-projects-migrate/-/commits/main/)

Migrate GitLab projects from a GitLab group to another GitLab's group

---

## Purpose

The migration can be performed between entirely different GitLab servers.

The following steps are required before using the tool:

- The groups need to be created manually by the user or by a GitLab administrator
- The GitLab user tokens must be created with an `api` scope (a short expiration date is recommended)

---

## Examples

<!-- prettier-ignore-start -->

```bash
# Show the helper menu
gitlab-projects-migrate

# Migrate projects from one group to another, then migrate subgroups
gitlab-projects-migrate 'https://gitlab.com' 'old/group' 'https://gitlab.com' 'new/group'
gitlab-projects-migrate 'https://gitlab.com' 'old/group/subgroup1' 'https://gitlab.com' 'new/group/subgroup1'
gitlab-projects-migrate 'https://gitlab.com' 'old/group/subgroup2' 'https://gitlab.com' 'new/group/subgroup2'

# Migrate projects from one GitLab to another GitLab
gitlab-projects-migrate 'https://old.gitlab.com' 'group/subgroup' 'https://new.gitlab.com'
```

<!-- prettier-ignore-end -->

---

## Usage

<!-- prettier-ignore-start -->
<!-- readme-help-start -->

```yaml
usage: gitlab-projects-migrate [-h] [--version] [-I INPUT_TOKEN] [-O OUTPUT_TOKEN] [--dry-run] [--exclude-group]
                               [--exclude-subgroups] [--exclude-projects] [--keep-members] [--overwrite]
                               [--set-avatar FILE] [--update-description]
                               [input_gitlab] [input_path] [output_gitlab] [output_group]

gitlab-projects-migrate: Migrate GitLab projects from a GitLab group to another GitLab's group

internal arguments:
  -h, --help            # Show this help message
  --version             # Show the current version

credentials arguments:
  -I INPUT_TOKEN        # Input GitLab API token (default: GITLAB_INPUT_TOKEN or GITLAB_TOKEN environments)
  -O OUTPUT_TOKEN       # Output GitLab API token (default: GITLAB_OUTPUT_TOKEN, GITLAB_TOKEN environments, or INPUT_TOKEN argument)

migration arguments:
  --dry-run             # Enable dry run mode to check without saving
  --exclude-group       # Exclude parent group migration
  --exclude-subgroups   # Exclude children subgroups migration
  --exclude-projects    # Exclude children projects migration
  --keep-members        # Keep input members after importing on output GitLab
  --overwrite           # Overwrite existing projects on output GitLab

general settings arguments:
  --set-avatar FILE     # Set avatar of GitLab output projects and groups
  --update-description  # Update description of GitLab output projects and groups automatically

positional arguments:
  input_gitlab          # Input GitLab URL (default: https://gitlab.com)
  input_path            # Input GitLab group or project path
  output_gitlab         # Output GitLab URL (default: https://gitlab.com)
  output_group          # Output GitLab group
```

<!-- readme-help-stop -->
<!-- prettier-ignore-end -->

---

## Dependencies

- [colored](https://pypi.org/project/colored/): Terminal colors and styles
- [python-gitlab](https://pypi.org/project/python-gitlab/): A python wrapper for the GitLab API
- [setuptools](https://pypi.org/project/setuptools/): Build and manage Python packages

---

## References

- [git-chglog](https://github.com/git-chglog/git-chglog): CHANGELOG generator
- [gitlab-release](https://pypi.org/project/gitlab-release/): Utility for publishing on GitLab
- [gitlabci-local](https://pypi.org/project/gitlabci-local/): Launch .gitlab-ci.yml jobs locally
- [mypy](https://pypi.org/project/mypy/): Optional static typing for Python
- [PyPI](https://pypi.org/): The Python Package Index
- [twine](https://pypi.org/project/twine/): Utility for publishing on PyPI
