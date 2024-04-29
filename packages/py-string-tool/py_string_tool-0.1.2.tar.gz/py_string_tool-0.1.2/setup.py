from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="useful additional string functions",
    name="py_string_tool",
    version="0.1.2",
    packages=find_packages(),
    license="MIT",
    install_requires=["thefuzz","difflib","langdetect"],

)