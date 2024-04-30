from setuptools import setup, find_packages
setup(
    name="demo-avis",
    version="2.1.4",
    packages=find_packages(),
    install_requires=[
        #Add dependencies
    ],
    entry_points={
        "console_scripts": [
            "hello_hello = hello_hello:hello",
        ],
    }
)