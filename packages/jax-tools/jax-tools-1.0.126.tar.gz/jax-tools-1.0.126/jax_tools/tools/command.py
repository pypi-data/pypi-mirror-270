# -*- coding: utf-8 -*-
"""
Command tool
"""
import os
import shlex
import subprocess


class Command(object):
    """
    Command tool
    """
    def __init__(self, cmd: str) -> None:
        self.cmd = cmd

    def exec_cmd_safety(self) -> None:
        """
        Execute command use safety method
        Returns:

        """
        subprocess.call(shlex.split(self.cmd))

    def get_output_safety(self) -> str:
        """
        Get command output use safety method
        Returns:

        """
        return subprocess.check_output(shlex.split(self.cmd)).decode('utf-8')

    def exec_cmd_without_safety(self) -> None:
        """
        Execute command without safety method, suggest you validate the command before use this method
        Please Ensure the command is safe
        Returns:

        """
        os.system(self.cmd)

    def get_output_without_safety(self) -> str:
        """
        Get command output without safety method, suggest you validate the command before use this method
        Please Ensure the command is safe
        Returns:

        """
        return os.popen(self.cmd).read()
