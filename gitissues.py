import textwrap

from abc import ABCMeta, abstractmethod, abstractproperty
from colorama import Fore, Style


class GitIssues(object):
    __metaclass__ = ABCMeta

    hosts = []
    config_key = None

    def __init__(self, repo):
        pass

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
