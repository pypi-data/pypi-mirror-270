import os
import subprocess as subproc
import shlex

from .log import logger


def exec_cmd(command: str) -> int:
    """Execute a given shell command or script."""
    shell = os.getenv('SHELL', '/bin/sh')

    if os.path.exists(command):
        command_list = [command]
    else:
        safe_command = shlex.quote(command)
        command_list = [shell, '-c', safe_command]

    print("Executing command: {}".format(command))  # User feedback
    process = subproc.Popen(
        command_list,
        stdout=subproc.PIPE,
        stderr=subproc.PIPE,
        universal_newlines=True,
    )
    stdout, stderr = process.communicate()

    if stdout:
        logger.info("Output: " + stdout.strip())
    if stderr:
        logger.error("Error: " + stderr.strip())

    return process.returncode
