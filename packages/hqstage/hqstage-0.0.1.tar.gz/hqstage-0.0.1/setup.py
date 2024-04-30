###
# Created Date: 2024-04-29
# Author: Sebastian Lehmann
# -----
# Copyright © 2024 HQS Quantum Simulations GmbH. All Rights Reserved.
###

"""Installation of hqstage stub."""

from pathlib import Path
from setuptools import Command, setup
from setuptools.command.build import build
import os


class CustomCommand(Command):
    """A custom command to let installation fail with a message."""

    def initialize_options(self) -> None: ...

    def finalize_options(self) -> None: ...

    def run(self) -> None:
        if os.getenv("HQSTAGE_STUB_INSTALL_NO_FAIL") is None:
            raise RuntimeError(
                """

--------------------------------------------------------------
  This package is a stub. Currently, hqstage can NOT be
  installed via pypi.org.

  For instructions on how to install and get started
  using the real hqstage package, please visit
  https://docs.cloud.quantumsimulations.de/.

  Thank you very much!
--------------------------------------------------------------
                """
            )


class CustomBuild(build):
    sub_commands = [("build_custom", None)] + build.sub_commands


setup(cmdclass={"build": CustomBuild, "build_custom": CustomCommand})
