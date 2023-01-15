from setuptools import setup, find_packages

setup(
    name="gitpraise",
    version="0.0.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points="""
    [console_scripts]
    gitpraise=gitpraise.cli:run_command
    """,
)
