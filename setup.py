from setuptools import setup

setup(
    name='Jinger',
    version='0.1.0',
    author='Vineet Naik',
    author_email='naikvin@gmail.com',
    packages=['jinger', 'jinger.test'],
    license='LICENSE.txt',
    description='A Jinja2 powered static site generator',
    long_description=open('README.rst').read(),
    install_requires=["Jinja2 >= 2.6"],
    entry_points={
        'console_scripts': [
            'jinger = jinger.commands:main'
            ]
        }
)
