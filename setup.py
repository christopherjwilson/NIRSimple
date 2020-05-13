import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nirsimple",
    version="0.0.1",
    author="Johann Benerradi",
    author_email="@",
    description="NIRS processing made simple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HanBnrd/NIRSimple",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
