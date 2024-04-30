# gitpoll/args.py
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Parse command line arguments for the gitpoll application."""
    parser = ArgumentParser(
        description="Monitors a Git repository for changes and executes scripts before and after pulling updates."
    )
    parser.add_argument(
        "repo_path", type=str, help="Path to the Git repository."
    )
    parser.add_argument(
        "--interval",
        type=int,
        help="Interval in seconds to check for changes.",
    )
    parser.add_argument(
        "--no-pull", action="store_true", help="Do not pull changes."
    )
    parser.add_argument(
        "--pre-action",
        type=str,
        help="Command or path to the pre-action shell script or command.",
    )
    parser.add_argument(
        "--post-action",
        type=str,
        help="Command or path to the post-action shell script or command.",
    )
    return parser.parse_args()
