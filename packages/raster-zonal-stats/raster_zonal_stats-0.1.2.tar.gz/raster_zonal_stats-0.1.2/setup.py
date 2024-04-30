from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="raster-zonal-stats",
    version="0.1.2",
    package_dir={"": "src"},  # This line is added
    packages=find_packages(where="src"),  # And this line is modified
    install_requires=[],
    python_requires=">=3.6",
    description="A Python package to retrieve raster values for each pixel of a shapefile.",  # Short, concise description
    long_description=long_description,  # Detailed description
    long_description_content_type="text/markdown",  # Content type for long description, assuming it's in Markdown
)

