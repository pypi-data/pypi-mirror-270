import os
import subprocess as subproc


def has_repo_changed(repo_path: str) -> bool:
    """Check if the repository has new changes by comparing local and remote heads."""
    os.chdir(repo_path)
    subproc.call(['git', 'fetch'])
    local_head = (
        subproc.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    )
    remote_head = (
        subproc.check_output(['git', 'rev-parse', 'origin/HEAD'])
        .decode()
        .strip()
    )

    return local_head != remote_head
