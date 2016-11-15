import gitlab

from gitissues import GitIssues


class GitLabIssues(GitIssues):
    def __init__(self):
        super(GitLabIssues, self).__init__()

        private_token = self.repo_config.get_value('gitlab', 'token')
        self.gl = gitlab.Gitlab(self.git_server, private_token, ssl_verify=False)
        self.gl.auth()

    def list_issues(self):
        project = self.gl.projects.get(self.git_project)
        for issue in project.issues.list(state='opened'):
            print(issue.title)
