from pathlib import Path
from setuptools import find_packages, setup

# Read the contents of README.md for the long description
with open(Path(__file__).resolve().parent / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="autospider",
    version="1.1.1",  # Updated version number
    description="A Smart, Automatic, Fast and Lightweight Web Scraper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khulnasoft-lab/autospider",
    author="KhulnaSoft DevOps",
    author_email="info@khulnasoft.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Updated development status
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="web scraping spider scraper",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.6",
    install_requires=["requests", "beautifulsoup4", "lxml"],  # Updated dependency name
)
