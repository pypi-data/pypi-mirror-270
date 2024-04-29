from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="package build on top of pandas and add more convient functionality. Make your code short and easy to read",
    name="dataframe_short",
    version="0.1.2",
    packages=find_packages(),
    license="MIT",
    requires=["pandas","os_toolkit"],
    
 
)