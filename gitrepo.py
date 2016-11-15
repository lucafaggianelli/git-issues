from git import Repo
from urlparse import urlparse


class GitRepo(object):

    def __init__(self, path='.'):
        self.repo = Repo(path)
        self.config = self.repo.config_reader()

        url = self.repo.remote().url
        if '//' not in url:
            url = '//' + url

        repo_url = urlparse(url)
        self.git_host = repo_url.hostname
        self.git_server = '{}://{}'.format(
                repo_url.scheme or 'http', repo_url.hostname)
        self.git_project = url.split(':')[-1].split('.')[0]
