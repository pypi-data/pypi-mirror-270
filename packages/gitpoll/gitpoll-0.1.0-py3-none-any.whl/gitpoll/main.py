# gitpoll/main.py
import subprocess
import os
import time
import shlex

from .args import parse_args
from .git import has_repo_changed
from .log import logger
from .shell import exec_cmd


def main():
    args = parse_args()
    while True:
        if has_repo_changed(args.repo_path):
            pre_action = (
                args.pre_action
                if args.pre_action
                else "echo No pre-action configured"
            )
            post_action = (
                args.post_action
                if args.post_action
                else "echo No post-action configured"
            )

            print("Pre-action: {}".format(pre_action))  # User feedback
            exec_cmd(pre_action)

            if not args.no_pull:
                logger.info("Pulling changes from the repository.")
                print("Pulling changes from the repository.")  # User feedback
                exec_cmd("git pull")

            print("Post-action: {}".format(post_action))  # User feedback
            exec_cmd(post_action)

            if args.interval:
                logger.info("Sleeping for {} seconds...".format(args.interval))
                print(
                    "Sleeping for {} seconds...".format(args.interval)
                )  # User feedback
                time.sleep(args.interval)
            else:
                logger.info("Monitoring stopped.")
                print("Monitoring stopped.")  # User feedback
                break


if __name__ == "__main__":
    main()
