###
# Created Date: 2024-04-29
# Author: Sebastian Lehmann
# -----
# Copyright © 2024 HQS Quantum Simulations GmbH. All Rights Reserved.
###

"""Installation of hqstage stub."""

from setuptools import setup
import os

if __name__ == "__main__":
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

    setup()
