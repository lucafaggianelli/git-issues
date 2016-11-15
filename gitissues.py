import textwrap

from abc import ABCMeta, abstractmethod
from colorama import Fore, Style
from git import Repo
from urlparse import urlparse


class GitIssues(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.repo = Repo('.')
        self.repo_config = self.repo.config_reader()

        url = self.repo.remote().url
        if '//' not in url:
            url = '//' + url

        repo_url = urlparse(url)
        self.git_server = '{}://{}'.format(
                repo_url.scheme or 'http', repo_url.hostname)
        self.git_project = url.split(':')[-1].split('.')[0]

    @abstractmethod
    def get_issues(self): pass

    def list_issues(self):
        for issue in self.get_issues():
            print(Fore.YELLOW + 'issue #{0[id]} {0[title]}'.format(issue) + Style.RESET_ALL)
            print('Author: {0[author]} <{0[author_email]}>'.format(issue))
            print('Date: {}'.format(issue['created_at'].strftime('%a, %d %b %Y %H:%M:%S %Z')))
            if 'description' in issue:
                print('')
                print(textwrap.fill(issue['description'], initial_indent=' '*4, subsequent_indent=' '*4))
                print('')
