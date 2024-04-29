from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="useful additional string functions",
    name="py_string_tool",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    requires=["thefuzz","difflib","langdetect"],
    

)