from setuptools import setup, find_packages
setup(
    name="hello_avishek",
    version="0.3",
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