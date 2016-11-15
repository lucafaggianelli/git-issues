import gitlab

from datetime import datetime
from gitissues import GitIssues


class GitLabIssues(GitIssues):
    def __init__(self):
        super(GitLabIssues, self).__init__()

        private_token = self.repo_config.get_value('gitlab', 'token')
        self.gl = gitlab.Gitlab(self.git_server, private_token, ssl_verify=False)
        #self.gl.enable_debug()
        self.gl.auth()

    def get_issues(self):
        issues = []
        project = self.gl.projects.get(self.git_project)

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
