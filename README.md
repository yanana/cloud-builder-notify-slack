# cloud-builder-notify-slack

[![Docker Repository on Quay](https://quay.io/repository/yanana/cloud-builder-notify-slack/status "Docker Repository on Quay")](https://quay.io/repository/yanana/cloud-builder-notify-slack)

A rude implementation of a build step of Google Cloud Container Builder to notify build result to Slack

## What can this image do?

This build step enables you to notify the result of a build. This step is based on the premise that:

- The repository being built is a repository in GitHub. In other words, remote URL has to be something like `https://github.com/foo/bar.git`.
- The repository doesn't contain any submodules (simply ignored).

## Usage

You need to create a Incoming Webhook of Slack.
