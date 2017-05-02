#!/usr/bin/env python

import argparse
import json
import re

import pygit2
import requests


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('succeeded', type=bool, help='the flag to notify if succeeded')
    parser.add_argument('webhook_url', type=str, help='the URL for webhook')
    return parser.parse_args()


# curl -X POST --data-raw "${payload}" "${webhook_url}"
# webhook_url='https://hooks.slack.com/services/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'

def build_repo_link(remote):
    url = remote.url
    name = re.sub(r'\.git$', '', re.sub(r'^https://github.com/', '', url))
    return f'<{url}|{name}>'


class Result:
    def __init__(self, succeeded):
        self.color = 'good' if succeeded else 'danger'
        self.status = 'Succeeded' if succeeded else 'Failed'

    def toMessageText(self, path_to_repo):
        repo = pygit2.Repository(path_to_repo)
        c = repo.head.get_object()
        branch_name = '/'.join(repo.head.name.split('/')[2:])
        repo_link = build_repo_link(repo.remotes['origin'])
        message = c.message.strip()
        return f'{self.status}: {c.author.name}\'s build in {repo_link} ({branch_name})\n- {message}'


def build_message(succeeded):
    result = Result(succeeded)
    path_to_repo = '/workspace'
    message = {
        'attachments': [
            {
                'color': result.color,
                'text': result.toMessageText(path_to_repo)
            }
        ]
    }
    print(json.dumps(message))
    return message


def notify(succeeded, webhook_url):
    message = build_message(succeeded)
    r = requests.post(webhook_url, json=message)
    print(r.text)


def main():
    args = parse_args()
    print(args)
    notify(args.succeeded, args.webhook_url)


if __name__ == '__main__':
    main()
