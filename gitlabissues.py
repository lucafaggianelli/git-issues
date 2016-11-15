import gitlab

from datetime import datetime
from gitissues import GitIssues


class GitLabIssues(GitIssues):

    hosts = ['gitlab.com']
    config_key = 'gitlab'

    def __init__(self, repo):
        self.repo = repo

        private_token = repo.config.get_value('gitlab', 'token')
        self.gl = gitlab.Gitlab(repo.git_server, private_token, ssl_verify=False)
        #self.gl.enable_debug()
        self.gl.auth()

    def get_issues(self):
        issues = []
        project = self.gl.projects.get(self.repo.git_project)

        for issue in project.issues.list(state='opened'):
            issues.append({
                'id': issue.id,
                'title': issue.title,
                'author': issue.author.name,
                'author_email': self.gl.users.get(issue.author.id).email,
                'created_at': datetime.strptime(issue.created_at, '%Y-%m-%dT%H:%M:%S.%fZ'),
                'description': issue.description
            })

        return issues
