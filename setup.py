from setuptools import setup

setup(
    name="aws-ops",
    description="Assume Role Management Tool",
    packages=["assume_tool"],
    install_requires=["argparse","configparser","pandas","datetime","boto3"],
    entry_points={
            "console_scripts": ["aws-ops=assume_tool.main:main"],
    }
)