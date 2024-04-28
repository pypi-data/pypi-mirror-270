#!/usr/bin/env python3

# Standard libraries
from argparse import Namespace

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
        group: Group = None
        project: Project = None

        # Header
        print(' ')

        # GitLab client
        gitlab = GitLabFeature(
            options.gitlab,
            options.token,
            options.dry_run,
        )
        print(f'{Colors.BOLD} - GitLab host: '
              f'{Colors.GREEN}{gitlab.url}'
              f'{Colors.RESET}')
        Platform.flush()

        # GitLab path
        try:
            group = gitlab.group(options.path)
            print(f'{Colors.BOLD} - GitLab group: '
                  f'{Colors.GREEN}{group.full_path}'
                  f'{Colors.CYAN} ({group.description})'
                  f'{Colors.RESET}')
            print(' ')
            Platform.flush()
        except GitlabGetError:
            project = gitlab.project(options.path)
            print(f'{Colors.BOLD} - GitLab project: '
                  f'{Colors.GREEN}{project.path_with_namespace}'
                  f'{Colors.CYAN} ({project.description})'
                  f'{Colors.RESET}')
            print(' ')
            Platform.flush()

        # Handle single project
        if project:
            Entrypoint.project(
                options,
                gitlab,
                project.id,
            )

        # Handle group recursively
        elif group:

            # Handle group
            if not options.exclude_group:
                Entrypoint.group(
                    options,
                    gitlab,
                    group.id,
                )

            # Iterate through subgroups
            if not options.exclude_subgroups:
                for group_subgroup in group.descendant_groups.list(
                        get_all=True,
                        include_subgroups=True,
                        order_by='path',
                        sort='asc',
                ):
                    Entrypoint.group(
                        options,
                        gitlab,
                        group_subgroup.id,
                        True,
                    )

            # Iterate through projects
            if not options.exclude_projects:
                for group_project in group.projects.list(
                        get_all=True,
                        include_subgroups=not options.exclude_subgroups,
                        order_by='path',
                        sort='asc',
                ):
                    Entrypoint.project(
                        options,
                        gitlab,
                        group_project.id,
                    )

        # Result
        return True

    # Group
    @staticmethod
    def group(
        options: Namespace,
        gitlab: GitLabFeature,
        criteria: str,
        subgroup: bool = False,
    ) -> None:

        # Acquire group
        group = gitlab.group(criteria)

        # Acquire parent group
        parent_group: Group = None
        if group.parent_id:
            parent_group = gitlab.group(group.parent_id)

        # Get parent description
        parent_description: str = ''
        parent_name: str = ''
        if parent_group:
            parent_description = parent_group.description
            parent_name = parent_group.name

        # Show group details
        group_type = 'subgroup' if subgroup else 'group'
        print(f'{Colors.BOLD} - GitLab {group_type}: '
              f'{Colors.YELLOW_LIGHT}{group.full_path} '
              f'{Colors.CYAN}({group.description})'
              f'{Colors.RESET}')

        # Set group description
        if options.set_description:
            gitlab.group_set_description(criteria, options.set_description)
            print(f'{Colors.BOLD}   - Set description: '
                  f'{Colors.CYAN}{options.set_description}'
                  f'{Colors.RESET}')

        # Update group description
        elif options.update_description:
            parent_description_text: str = ''
            if parent_name:
                parent_description_text = ' - ' + GitLabFeature.Helper.describe(
                    parent_description,
                    parent_name,
                )
            description = f'{GitLabFeature.Helper.capitalize(group.name)}' \
                          f'{parent_description_text}'
            gitlab.group_set_description(criteria, description)
            print(f'{Colors.BOLD}   - Updated description: '
                  f'{Colors.CYAN}{description}'
                  f'{Colors.RESET}')

        # Reset group members
        if options.reset_members:
            gitlab.group_reset_members(criteria)
            print(f'{Colors.BOLD}   - Reset members: '
                  f'{Colors.GREEN}Success'
                  f'{Colors.RESET}')

        # Set group avatar
        if options.set_avatar:
            gitlab.group_set_avatar(criteria, options.set_avatar)
            print(f'{Colors.BOLD}   - Set avatar: '
                  f'{Colors.CYAN}{options.set_avatar}'
                  f'{Colors.RESET}')

        # Footer
        print(' ')
        Platform.flush()

    # Project, pylint: disable=too-many-branches
    @staticmethod
    def project(
        options: Namespace,
        gitlab: GitLabFeature,
        criteria: str,
    ) -> None:

        # Acquire project
        project = gitlab.project(criteria)

        # Acquire group
        group = gitlab.group(project.namespace['id'])

        # Show project details
        print(f'{Colors.BOLD} - GitLab project: '
              f'{Colors.YELLOW_LIGHT}{project.path_with_namespace} '
              f'{Colors.CYAN}({project.description})'
              f'{Colors.RESET}')

        # Set project description
        if options.set_description:
            gitlab.project_set_description(criteria, options.set_description)
            print(f'{Colors.BOLD}   - Set description: '
                  f'{Colors.CYAN}{options.set_description}'
                  f'{Colors.RESET}')

        # Update project description
        elif options.update_description:
            group_description = GitLabFeature.Helper.describe(
                group.description,
                group.name,
            )
            description = f'{GitLabFeature.Helper.capitalize(project.name)}' \
                          f' - {group_description}'
            gitlab.project_set_description(criteria, description)
            print(f'{Colors.BOLD}   - Updated description: '
                  f'{Colors.CYAN}{group_description}'
                  f'{Colors.RESET}')

        # Reset project features
        if options.reset_features:
            features = ', '.join(gitlab.project_reset_features(criteria))
            if features:
                print(f'{Colors.BOLD}   - Reset features: '
                      f'{Colors.CYAN}{features}'
                      f'{Colors.RESET}')
            else:
                print(f'{Colors.BOLD}   - Reset features: '
                      f'{Colors.GREEN}Already done'
                      f'{Colors.RESET}')

        # Reset project members
        if options.reset_members:
            gitlab.project_reset_members(criteria)
            print(f'{Colors.BOLD}   - Reset members: '
                  f'{Colors.GREEN}Success'
                  f'{Colors.RESET}')

        # Set project avatar
        if options.set_avatar:
            gitlab.project_set_avatar(criteria, options.set_avatar)
            print(f'{Colors.BOLD}   - Set avatar: '
                  f'{Colors.CYAN}{options.set_avatar}'
                  f'{Colors.RESET}')

        # Protect project branches
        if options.protect_branches:
            branches = ', '.join(gitlab.project_protect_branches(criteria))
            if branches:
                print(f'{Colors.BOLD}   - Protecting branches: '
                      f'{Colors.CYAN}{branches}'
                      f'{Colors.RESET}')
            else:
                print(f'{Colors.BOLD}   - Protecting branches: '
                      f'{Colors.GREEN}Already done'
                      f'{Colors.RESET}')

        # Protect project tags
        if options.protect_tags:
            tags = ', '.join(gitlab.project_protect_tags(criteria, options.protect_tags))
            if tags:
                print(f'{Colors.BOLD}   - Protecting tags: '
                      f'{Colors.CYAN}{tags}'
                      f'{Colors.GREEN} (level: {options.protect_tags})'
                      f'{Colors.RESET}')
            else:
                print(f'{Colors.BOLD}   - Protecting tags: '
                      f'{Colors.GREEN}Already done'
                      f'{Colors.RESET}')

        # Footer
        print(' ')
        Platform.flush()
