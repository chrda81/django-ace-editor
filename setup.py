# -*- coding: utf-8 -*-
import json
import os

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist


# Override build command
class BuildCommand(sdist):

    def run(self):
        # Run the original build command
        sdist.run(self)
        # os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        os.system('rm -vrf ./*.egg-info')


with open('package.json') as f:
    package_json = json.load(f)


def read_requirements(requirements):
    """Parse requirements from requirements.txt."""
    with open(requirements, 'r') as f:
        reqs = [line.rstrip() for line in f]
    return reqs


setup(
    name=package_json["name"],
    version=package_json["version"],
    description=package_json["description"],
    long_description=open('README.rst').read(),

    author=package_json["author"],
    author_email=package_json["author_email"],
    license=package_json["license"],
    url=package_json["homepage"],

    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements/production.txt"),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    cmdclass={
        'sdist': BuildCommand,
    }
)
