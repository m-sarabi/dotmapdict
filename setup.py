from setuptools import setup, find_packages

setup(
    name="dotmapdict",
    version="1.0.0",
    description="A dictionary that supports dot notation access",
    long_description=open("README.MD").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/m-sarabi/dotmapdict",
    author="Mohammad Sarabi",
    author_email="m.sarabi.jkd@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
