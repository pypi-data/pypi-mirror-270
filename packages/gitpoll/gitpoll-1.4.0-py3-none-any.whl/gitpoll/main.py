#!/usr/bin/env python3
from shell import CmdExec
from args import parse_args
from git import has_repo_changed
from log import logger
import os
import time


def main():
    args = parse_args()
    repo_path = (
        os.path.abspath(args.repo_path) if args.repo_path else os.getcwd()
    )

    if not os.path.exists(repo_path):
        logger.error("Repository path '{}' does not exist.".format(repo_path))
        return 1

    logger.debug('args: {}'.format(args.__dict__))

    while True:
        logger.debug("Checking for changes in the repository.")
        logger.debug("Repository path: {} Changing to...".format(repo_path))

        os.chdir(repo_path)  # Change to the repository path

        gitcmds = has_repo_changed(repo_path)
        if gitcmds.changed:
            logger.info("Repository has new changes.")
            pre_action = (
                args.pre_action
                if args.pre_action
                else "echo 'No pre-action configured'"
            )
            post_action = (
                args.post_action
                if args.post_action
                else "echo 'No post-action configured'"
            )
            logger.debug("Pre-action: {}".format(pre_action))
            logger.debug("Post-action: {}".format(post_action))
            logger.debug("Executing pre-action.")
            pre_cmd = CmdExec(pre_action)
            logger.debug("Executed pre-action: {}".format(pre_cmd))

            if not args.no_pull:
                logger.info("Pulling changes from the repository.")
                pull_cmd = CmdExec("git pull")
                logger.info(str(pull_cmd))

            post_cmd = CmdExec(post_action)
            logger.info(str(post_cmd))
        else:
            logger.debug("No new changes in the repository.")

        if not args.interval:
            logger.debug("Monitoring stopped.")
            return 0

        logger.debug("Sleeping for {} seconds.".format(args.interval))
        time.sleep(args.interval)

    return 1


if __name__ == "__main__":
    main()
