import os
import subprocess as subproc
from pyshared import default_repr as def_repr
from typing import Union as U, List, Dict, Optional as Opt, Tuple
from logfunc import logf

from .shell import CmdExec, CmdResult

class GitCmds:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.fetch = CmdExec('git fetch').execute()
        self.local = CmdExec('git rev-parse HEAD').execute()
        self.remote = CmdExec('git rev-parse @{u}').execute()

        self.success = (
            self.fetch.code == 0
            and self.local.code == 0
            and self.remote.code == 0
        )
        self.changed = (
            True if self.local.output != self.remote.output else False
        )

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


def has_repo_changed(repo_path: str) -> GitCmds:
    """Check if the repository has new changes by comparing local and remote heads."""
    os.chdir(repo_path)
    return GitCmds(repo_path)
