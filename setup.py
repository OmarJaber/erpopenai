from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpopenai/__init__.py
from erpopenai import __version__ as version

setup(
	name="erpopenai",
	version=version,
	description="Erpopenai",
	author="Omar Jaber",
	author_email="omar.ja93@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
