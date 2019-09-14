from setuptools import setup

setup(
    name='App',
    packages=['App'],
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'flask-bootstrap'
    ],
)