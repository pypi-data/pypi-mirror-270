#!/usr/bin/env python3

# Standard libraries
from argparse import Namespace
from tempfile import NamedTemporaryFile

# Modules libraries
from gitlab.exceptions import GitlabGetError
from gitlab.v4.objects import Group, Project

# Components
from ..features.gitlab import GitLabFeature
from ..prints.colors import Colors
from ..system.platform import Platform

# Entrypoint class, pylint: disable=too-few-public-methods
class Entrypoint:

    # CLI
    @staticmethod
    def cli(options: Namespace) -> bool:

        # Variables
        input_group: Group = None
        input_project: Project = None
        output_exists: bool = False
        output_group: Group = None

        # Header
        print(' ')

        # Input client
        input_gitlab = GitLabFeature(
            options.input_gitlab,
            options.input_token,
            options.dry_run,
        )
        print(f'{Colors.BOLD} - GitLab input: '
              f'{Colors.GREEN}{input_gitlab.url}'
              f'{Colors.RESET}')
        Platform.flush()

        # Output client
        output_gitlab = GitLabFeature(options.output_gitlab, options.output_token,
                                      options.dry_run)
        print(f'{Colors.BOLD} - GitLab output: '
              f'{Colors.GREEN}{output_gitlab.url}'
              f'{Colors.RESET}')
        print(' ')
        Platform.flush()

        # Input path
        try:
            input_group = input_gitlab.group(options.input_path)
            print(f'{Colors.BOLD} - GitLab input group: '
                  f'{Colors.GREEN}{input_group.full_path}'
                  f'{Colors.CYAN} ({input_group.description})'
                  f'{Colors.RESET}')
            Platform.flush()
        except GitlabGetError:
            input_project = input_gitlab.project(options.input_path)
            print(f'{Colors.BOLD} - GitLab input project: '
                  f'{Colors.GREEN}{input_project.path_with_namespace}'
                  f'{Colors.CYAN} ({input_project.description})'
                  f'{Colors.RESET}')
            Platform.flush()

        # Output group
        try:
            output_exists = False
            output_group = output_gitlab.group(options.output_group)
            output_exists = True
            print(f'{Colors.BOLD} - GitLab output group: '
                  f'{Colors.GREEN}{output_group.full_path}'
                  f'{Colors.CYAN} ({output_group.description})'
                  f'{Colors.RESET}')
            print(' ')
            Platform.flush()

        # Output parent group
        except GitlabGetError as exception:

            # Validate options
            if not input_group or options.exclude_group:
                raise exception

            # Missing output group
            print(f'{Colors.BOLD} - GitLab output group: '
                  f'{Colors.GREEN}{options.output_group}'
                  f'{Colors.RED} (Non-existent output group)'
                  f'{Colors.RESET}')
            print(' ')
            Platform.flush()

        # Handle single project
        if input_project:
            Entrypoint.project(
                options,
                input_gitlab,
                output_gitlab,
                input_project.id,
                input_project.namespace['id'],
                output_group.id,
            )

        # Handle group recursively
        elif input_group:

            # Handle group if missing
            if not options.exclude_group:
                Entrypoint.group(
                    options,
                    input_gitlab,
                    output_gitlab,
                    input_group.id,
                    options.output_group,
                    migration=not output_exists,
                )
                output_group = output_gitlab.group(options.output_group, optional=True)

            # Iterate through subgroups
            if not options.exclude_subgroups or not output_exists:
                for input_subgroup in sorted(
                        input_group.descendant_groups.list(
                            get_all=True,
                            include_subgroups=True,
                            order_by='path',
                            sort='asc',
                        ),
                        key=lambda item: item.full_path,
                ):
                    Entrypoint.subgroup(
                        options,
                        input_gitlab,
                        output_gitlab,
                        input_group.id,
                        input_subgroup.id,
                        output_group.id,
                        migration=output_exists,
                    )

            # Iterate through projects
            if not options.exclude_projects:
                for input_project in sorted(
                        input_group.projects.list(
                            get_all=True,
                            include_subgroups=not options.exclude_subgroups,
                            order_by='path',
                            sort='asc',
                        ),
                        key=lambda item: item.path_with_namespace,
                ):
                    Entrypoint.project(
                        options,
                        input_gitlab,
                        output_gitlab,
                        input_project.id,
                        input_group.id,
                        output_group.id,
                    )

        # Result
        return True

    # Group, pylint: disable=too-many-arguments
    @staticmethod
    def group(
        options: Namespace,
        input_gitlab: GitLabFeature,
        output_gitlab: GitLabFeature,
        criteria_input_group: str,
        criteria_output_group: str,
        migration: bool = True,
    ) -> None:

        # Acquire input group
        input_group = input_gitlab.group(criteria_input_group)

        # Detect group or subgroup
        output_group_namespace, output_group_path = GitLabFeature.Helper.split_namespace(
            criteria_output_group,
            relative=False,
        )
        output_group_name = input_group.name \
            if input_group.name != input_group.path \
            else output_group_path

        # Show group details
        print(f'{Colors.BOLD} - GitLab group: '
              f'{Colors.YELLOW_LIGHT}{input_group.full_path} '
              f'{Colors.CYAN}({input_group.description})'
              f'{Colors.RESET}')

        # Migration mode
        if not migration:
            output_subgroup = output_gitlab.group(criteria_output_group)
            print(f'{Colors.BOLD}   - Already exists in GitLab output: '
                  f'{Colors.GREEN}{output_subgroup.full_path}'
                  f'{Colors.CYAN} ({output_subgroup.description})'
                  f'{Colors.RESET}')
            print(' ')
            return

        # Export group
        print(f'{Colors.BOLD}   - Exporting from: '
              f'{Colors.GREEN}{input_group.full_path}'
              f'{Colors.RESET}')
        with NamedTemporaryFile(suffix='.tar.gz') as file_export:
            input_gitlab.group_export(
                file_export.name,
                input_group.id,
                options.keep_members,
            )

            # Import group
            print(f'{Colors.BOLD}   - Importing to: '
                  f'{Colors.GREEN}{criteria_output_group}'
                  f'{Colors.RESET}')
            output_gitlab.group_import(
                file_export.name,
                output_group_namespace,
                output_group_path,
                output_group_name,
            )

        # Acquire output group
        output_group_id: str = ''
        if not options.dry_run:
            output_group = output_gitlab.group(criteria_output_group)
            output_group_id = output_group.id

        # Set group description
        description = GitLabFeature.Helper.describe(
            input_group.description,
            output_group_name,
        )
        output_gitlab.group_set_description(
            output_group_id,
            description,
        )
        print(f'{Colors.BOLD}   - Set description: '
              f'{Colors.CYAN}{description}'
              f'{Colors.RESET}')

        # Set group avatar
        if options.set_avatar:
            output_gitlab.group_set_avatar(
                output_group_id,
                options.set_avatar,
            )
            print(f'{Colors.BOLD}   - Set avatar: '
                  f'{Colors.CYAN}{options.set_avatar}'
                  f'{Colors.RESET}')

        # Show group result
        print(f'{Colors.BOLD}   - Migrated group: '
              f'{Colors.GREEN}Success'
              f'{Colors.RESET}')

        # Footer
        print(' ')
        Platform.flush()

    # Project, pylint: disable=too-many-arguments,too-many-branches,too-many-locals
    @staticmethod
    def project(
        options: Namespace,
        input_gitlab: GitLabFeature,
        output_gitlab: GitLabFeature,
        criteria_project: str,
        criteria_input_group: str,
        criteria_output_group: str,
    ) -> None:

        # Acquire input project
        input_project = input_gitlab.project(criteria_project)

        # Acquire input group
        input_group = input_gitlab.group(criteria_input_group)

        # Acquire output group
        output_group = output_gitlab.group(criteria_output_group, optional=True)

        # Show project details
        print(f'{Colors.BOLD} - GitLab input project: '
              f'{Colors.YELLOW_LIGHT}{input_project.path_with_namespace} '
              f'{Colors.CYAN}({input_project.description})'
              f'{Colors.RESET}')

        # Ignore existing projects
        input_subpath = GitLabFeature.Helper.subpath(
            input_group.full_path,
            input_project.path_with_namespace,
        )
        if not options.overwrite and input_subpath in [
                GitLabFeature.Helper.subpath(
                    output_group.full_path,
                    output_project.path_with_namespace,
                ) for output_project in output_group.projects.list(
                    get_all=True,
                    include_subgroups=True,
                )
        ]:
            output_group_project = output_gitlab.project(
                f'{output_group.full_path}/{input_subpath}')
            print(f'{Colors.BOLD}   - Already exists in GitLab output: '
                  f'{Colors.GREEN}{output_group_project.path_with_namespace}'
                  f'{Colors.CYAN} ({output_group_project.description})'
                  f'{Colors.RESET}')
            print(' ')
            return

        # Export project
        print(f'{Colors.BOLD}   - Exporting from: '
              f'{Colors.GREEN}{options.input_path}'
              f'{Colors.CYAN} / {input_subpath}'
              f'{Colors.RESET}')
        with NamedTemporaryFile(suffix='.tar.gz') as file_export:
            input_gitlab.project_export(
                file_export.name,
                input_project.id,
                options.keep_members,
            )

            # Existing project removal
            if options.overwrite:
                output_gitlab.project_delete(f'{output_group.full_path}/{input_subpath}')

            # Import project
            print(f'{Colors.BOLD}   - Importing to: '
                  f'{Colors.GREEN}{options.output_group}'
                  f'{Colors.CYAN} / {input_subpath}'
                  f'{Colors.RESET}')
            output_namespace, output_path = GitLabFeature.Helper.split_namespace(
                input_subpath,
                relative=True,
            )
            imported_project = output_gitlab.project_import(
                file_export.name,
                f'{options.output_group}{output_namespace}',
                output_path,
                input_project.name,
                options.overwrite,
            )

            # Acquire subgroup description
            output_subgroup_description: str
            if not options.dry_run:
                output_subgroup = output_gitlab.group(
                    f'{options.output_group}{output_namespace}')
                output_subgroup_description = output_subgroup.description
            else:
                output_subgroup_description = input_project.description

            # Update project description
            if options.update_description:
                group_description = GitLabFeature.Helper.describe(
                    output_subgroup_description,
                    input_project.name,
                )
                if not imported_project.description.endswith(f' - {group_description}'):
                    description = f'{GitLabFeature.Helper.capitalize(imported_project.name)}' \
                                f' - {group_description}'
                    output_gitlab.project_set_description(
                        imported_project.id,
                        description,
                    )
                    print(f'{Colors.BOLD}   - Updated description: '
                          f'{Colors.CYAN}{description}'
                          f'{Colors.RESET}')
                else:
                    print(f'{Colors.BOLD}   - Kept description: '
                          f'{Colors.GREEN}{imported_project.description}'
                          f'{Colors.RESET}')

            # Reset project members
            if not options.keep_members:
                output_gitlab.project_reset_members(imported_project.id)
                print(f'{Colors.BOLD}   - Reset members: '
                      f'{Colors.GREEN}Success'
                      f'{Colors.RESET}')

            # Set project avatar
            if options.set_avatar:
                output_gitlab.project_set_avatar(
                    imported_project.id,
                    options.set_avatar,
                )
                print(f'{Colors.BOLD}   - Set avatar: '
                      f'{Colors.CYAN}{options.set_avatar}'
                      f'{Colors.RESET}')

        # Show project result
        print(f'{Colors.BOLD}   - Migrated project: '
              f'{Colors.GREEN}Success'
              f'{Colors.RESET}')
        print(' ')
        Platform.flush()

    # Subgroup, pylint: disable=too-many-arguments
    @staticmethod
    def subgroup(
        options: Namespace,
        input_gitlab: GitLabFeature,
        output_gitlab: GitLabFeature,
        criteria_input_group: str,
        criteria_input_subgroup: str,
        criteria_output_group: str,
        migration: bool = True,
    ) -> None:

        # Acquire input group
        input_group = input_gitlab.group(criteria_input_group)

        # Acquire input subgroup
        input_subgroup = input_gitlab.group(criteria_input_subgroup)

        # Acquire output group
        output_group = output_gitlab.group(criteria_output_group, optional=True)

        # Show subgroup details
        print(f'{Colors.BOLD} - GitLab subgroup: '
              f'{Colors.YELLOW_LIGHT}{input_subgroup.full_path} '
              f'{Colors.CYAN}({input_subgroup.description})'
              f'{Colors.RESET}')

        # Parse subgroup paths
        input_subpath = GitLabFeature.Helper.subpath(
            input_group.full_path,
            input_subgroup.full_path,
        )
        output_namespace, output_path = GitLabFeature.Helper.split_namespace(
            input_subpath,
            relative=True,
        )

        # Migration mode
        if migration:

            # Ignore existing group
            if input_subpath in [
                    GitLabFeature.Helper.subpath(
                        output_group.full_path,
                        output_subgroup.full_path,
                    ) for output_subgroup in output_group.descendant_groups.list(
                        get_all=True,
                        include_subgroups=True,
                    )
            ]:
                output_subgroup = output_gitlab.group(
                    f'{output_group.full_path}/{input_subpath}')
                print(f'{Colors.BOLD}   - Already exists in GitLab output: '
                      f'{Colors.GREEN}{output_subgroup.full_path}'
                      f'{Colors.CYAN} ({output_subgroup.description})'
                      f'{Colors.RESET}')
                print(' ')
                return

            # Export subgroup
            print(f'{Colors.BOLD}   - Exporting from: '
                  f'{Colors.GREEN}{input_subgroup.full_path}'
                  f'{Colors.RESET}')
            with NamedTemporaryFile(suffix='.tar.gz') as file_export:
                input_gitlab.group_export(
                    file_export.name,
                    input_subgroup.id,
                    options.keep_members,
                )

                # Import subgroup
                print(
                    f'{Colors.BOLD}   - Importing to: '
                    f'{Colors.GREEN}{output_group.full_path}{output_namespace}/{output_path}'
                    f'{Colors.RESET}')
                output_gitlab.group_import(
                    file_export.name,
                    f'{output_group.full_path}{output_namespace}',
                    output_path,
                    input_subgroup.name,
                )

        # Acquire subgroups
        output_subgroup_child_description: str
        output_subgroup_child_name: str
        output_subgroup_parent_description: str
        if not options.dry_run:
            output_subgroup_parent = output_gitlab.group(
                f'{output_group.full_path}{output_namespace}')
            output_subgroup_parent_description = output_subgroup_parent.description
            output_subgroup_child = output_gitlab.group(
                f'{output_group.full_path}/{input_subpath}')
            output_subgroup_child_description = output_subgroup_child.description
            output_subgroup_child_name = output_subgroup_child.name
        else:
            output_subgroup_parent_description = input_subgroup.description
            output_subgroup_child_description = input_subgroup.description
            output_subgroup_child_name = input_subgroup.name

        # Update group description
        if options.update_description:
            parent_description = GitLabFeature.Helper.describe(
                output_subgroup_parent_description,
                output_subgroup_child_name,
            )
            if not output_subgroup_child_description.endswith(f' - {parent_description}'):
                description = f'{GitLabFeature.Helper.capitalize(output_subgroup_child_name)}' \
                            f' - {parent_description}'
                output_gitlab.group_set_description(
                    f'{output_group.full_path}/{input_subpath}',
                    description,
                )
                print(f'{Colors.BOLD}   - Updated description: '
                      f'{Colors.CYAN}{description}'
                      f'{Colors.RESET}')
            else:
                print(f'{Colors.BOLD}   - Kept description: '
                      f'{Colors.GREEN}{output_subgroup_child_description}'
                      f'{Colors.RESET}')

        # Set group avatar
        if options.set_avatar:
            output_gitlab.group_set_avatar(
                f'{output_group.full_path}/{input_subpath}',
                options.set_avatar,
            )
            print(f'{Colors.BOLD}   - Set avatar: '
                  f'{Colors.CYAN}{options.set_avatar}'
                  f'{Colors.RESET}')

        # Show subgroup result
        print(f'{Colors.BOLD}   - Migrated subgroup: '
              f'{Colors.GREEN}Success'
              f'{Colors.RESET}')

        # Footer
        print(' ')
        Platform.flush()
