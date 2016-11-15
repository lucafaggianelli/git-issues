import gitlab
import textwrap

from colorama import Fore, Style
from datetime import datetime
from gitissues import GitIssues


class GitLabIssues(GitIssues):
    def __init__(self):
        super(GitLabIssues, self).__init__()

        private_token = self.repo_config.get_value('gitlab', 'token')
        self.gl = gitlab.Gitlab(self.git_server, private_token, ssl_verify=False)
        #self.gl.enable_debug()
        self.gl.auth()

    def list_issues(self):
        project = self.gl.projects.get(self.git_project)
        for issue in project.issues.list(state='opened'):
            print(Fore.YELLOW + 'issue #{} {}'.format(issue.id, issue.title) + Style.RESET_ALL)
            print('Author: {} <{}>'.format(issue.author.name, self.gl.users.get(issue.author.id).email))
            print('Date: {}'.format(datetime.strptime(issue.created_at, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%a, %d %b %Y %H:%M:%S %Z')))
            print('')
            if issue.description:
                print(textwrap.fill(issue.description, initial_indent=' '*4, subsequent_indent=' '*4))
                print('')
