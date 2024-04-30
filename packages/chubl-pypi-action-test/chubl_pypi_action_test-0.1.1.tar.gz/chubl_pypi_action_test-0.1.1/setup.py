from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="chubl_pypi_action_test",
    version="0.1.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],  # External packages as dependencies
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package",
    keywords="example",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
