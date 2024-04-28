import setuptools
from setuptools.command.install import install
import sys
import warnings

warnings.warn(
    "This package is deprecated. Please use the 'best-ec2' package instead by running 'pip install best-ec2'.",
    DeprecationWarning,
)

class BlockedInstall(install):
    def run(self):
        raise Exception(
            "Installation failed: This package is deprecated. Please install 'best-ec2' using 'pip install best-ec2'."
        )

setuptools.setup(
    python_requires=">3.7.0",
    install_requires=[
        "boto3 >=1.23.10",
        "lambda-thread-pool >=0.0.2",
        "requests >= 2.30.0",
    ],
    cmdclass={
        'install': BlockedInstall,
    }
)

if __name__ == "__main__":
    if 'install' in sys.argv:
        sys.exit()
    else:
        setuptools.setup()
