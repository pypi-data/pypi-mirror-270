from setuptools import setup, find_packages

setup(
    name='desp-auth-package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'lxml',
    ],
)
