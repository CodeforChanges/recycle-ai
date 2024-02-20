from setuptools import setup, find_packages

requirements = []
with open("requirements.txt", "r") as file:
    # Delete the \n symbol for each line in the file
    requirements = map(lambda x: x.strip(), file.readlines())

setup(
    name="recycle_ai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    entry_points={"console_scripts": ["reai=recycle_ai.cli:app"]},
)
