import setuptools

with open("README.org", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as req:
    install_requires = req.read().split("\n")

setuptools.setup(
    name="ontology_visualization",
    version="0.0.1",
    author="fatestigma",
    author_email="fate_stigma@hotmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edmondchuc/ontology-visualization.git",
    packages=setuptools.find_packages(),
    license='LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)
