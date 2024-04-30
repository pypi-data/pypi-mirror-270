import os
import pprint
from setuptools import setup, find_packages

# Define the setup parameters
setup(
    name="CC-EXPTS",
    version="0.6",
    description="CC EXPTS + SC EXPTS package",
    author="Ishannaik",
    author_email="ishannaik7@gmail.com",
    packages=find_packages(),
    package_data={
        "CC_EXPTS": ["*.pdf", "*.py", "*.rmp"],
        "SC_EXPTS": ["*.pdf", "*.py"],
    },  # Include all files in the CC_EXPTS package
)
