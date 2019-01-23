import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adb-select",
    version="0.0.1",
    author="Benjamin Daschel",
    author_email="supercoffee@coffeestrike.com",
    description="Select current ADB device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supercoffee/adb-select",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

