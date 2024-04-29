from setuptools import setup, find_packages

setup(
    name = 'First_pypi',
    version = '0.2',
    packages = find_packages(),
    install_requires = [
        # Add depenecies here.
        # e.g. `numpy>=1.11.1`
    ],

    entry_points = {
        "console_scripts" : [
            'pixegami-hello = pixegami_hello:hello'
        ],
    },
)
