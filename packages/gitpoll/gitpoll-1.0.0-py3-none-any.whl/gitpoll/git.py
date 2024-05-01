import os
import subprocess as subproc
from shell import CmdExec, CmdResult
from pyshared import default_repr as def_repr
from typing import Union as U, List, Dict, Optional as Opt, Tuple


class GitCmds:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.fetch = CmdExec('git fetch')
        self.local = CmdExec('git rev-parse HEAD')
        self.remote = CmdExec('git rev-parse @{u}')

        self.success = (
            self.fetch.status == 0
            and self.local.status == 0
            and self.remote.status == 0
        )
        self.changed = self.local.output != self.remote.output

    def __repr__(self):
        return def_repr(self)

    def __str__(self):
        return self.__repr__()


# previous non-class version
# def has_repo_changed(
#     repo_path: str,
# ) -> U[bool, Tuple[CmdExec, CmdExec, CmdExec]]:
#     """Check if the repository has new changes by comparing local and remote heads."""
#     ...
#     fetch = CmdExec('git fetch')
#     local = CmdExec('git rev-parse HEAD')
#     remote = CmdExec('git rev-parse @{u}')
#    return git_cmds.changed, (local, remote, fetch)


def has_repo_changed(repo_path: str) -> U[bool, GitCmds]:
    """Check if the repository has new changes by comparing local and remote heads."""
    os.chdir(repo_path)
    git_cmds = GitCmds(repo_path)
    return git_cmds.changed, git_cmds
