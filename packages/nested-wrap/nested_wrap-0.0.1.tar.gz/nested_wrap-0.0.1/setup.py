import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="nested_wrap",
    version="0.0.1",
    author="simplew",
    author_email="simplew@211.com",
    description="wrap_func_with_nested_access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={'': ['*.yaml', '*.csv', '*.txt', '.toml']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)