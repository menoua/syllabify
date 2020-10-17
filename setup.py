import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="syllabify",
    version="0.0.1",
    author="Kyle Gorman",
    author_email="kylebgorman@gmail.com",
    description="Python module for syllabifying ARPABET transcriptions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kylebgorman/syllabify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
	"License :: See syllabify.py for the license",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

