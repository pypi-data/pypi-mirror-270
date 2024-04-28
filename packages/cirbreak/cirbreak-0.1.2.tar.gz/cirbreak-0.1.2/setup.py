from setuptools import setup, find_packages

setup(
    name="cirbreak",
    version="0.1.2",
    description="A Python library implementing a circuit breaker pattern",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mario-barrientos-dev/cirbreak",
    author="Mario Alfonso Barrientos Benavides",
    author_email="mariobarrientos0303@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)