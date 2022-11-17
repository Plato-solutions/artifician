from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="artifician",
    version="0.1.7b1",
    description="Artifician is an event driven framework developed to simplify the process of preparation of the dataset for Artificial Intelligence models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plato-solutions/artifician",
    author="Abhijeet Gandhi",
    author_email="abhijeet.gandhi@platoanalytics.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
    ],
    keywords="python artifician",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.4.2",
        "rx>=3.2.0",
    ],
    # project_urls={
    #     'Documentation': "",
    #     'Source': "",
    #     'Tracker': "",
    # },
)
