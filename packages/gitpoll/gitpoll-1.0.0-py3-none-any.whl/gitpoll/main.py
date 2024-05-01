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

        if has_repo_changed(repo_path):
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
            pre_cmd = CmdExec(pre_action)
            logger.info(pre_cmd.summary())

            if not args.no_pull:
                logger.info("Pulling changes from the repository.")
                pull_cmd = CmdExec("git pull")
                logger.info(pull_cmd.summary())

            post_cmd = CmdExec(post_action)
            logger.info(post_cmd.summary())
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
