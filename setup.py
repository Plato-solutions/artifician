from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
with open("VERSION", "r") as f:
    version = f.read().strip()
setup(
    name="artifician",
    version=version,
    description="Artifician is an event driven framework developed to simplify the process of preparation of the dataset for Artificial Intelligence models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plato-solutions/artifician",
    author="Abhijeet Gandhi",
    author_email="abhijeet@platoanalytics.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
    ],
    keywords="python artifician",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "rx>=3.2.0",
        "beautifulsoup4",
        "spacy",
        "nltk",
    ],
    project_urls={
        'Documentation': "https://plato-solutions.gitbook.io/artifician/",
        'Source': "https://github.com/Plato-solutions/artifician",
    },
)
