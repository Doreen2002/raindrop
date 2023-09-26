from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in raindrop/__init__.py
from raindrop import __version__ as version

setup(
	name="raindrop",
	version=version,
	description="Raindrop customisations",
	author="raindrop",
	author_email="doreenmwapekatebe8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
