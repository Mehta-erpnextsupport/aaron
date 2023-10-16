from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aaron/__init__.py
from aaron import __version__ as version

setup(
	name="aaron",
	version=version,
	description="Aaron",
	author="Romit Dholariya",
	author_email="erpnextsupport@mehtasoftech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
