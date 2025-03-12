from setuptools import setup, find_packages

setup(
    name="custom_dashboard_plugin",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",  # per effettuare chiamate a GitHub API
    ],
)
