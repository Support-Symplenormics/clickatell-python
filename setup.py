import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clickatell-platform",
    version="2.0.1",
    author="Chris Brand, Stephen Leibbrandt, Renier Minne",
    author_email="support@clickatell.com",
    keywords=["clickatell","sms","platform"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://github.com/clickatell/clickatell-python",
    description="Library for interacting with the Clickatell Platform SMS Gateway",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="LICENSE",
    install_requires=[
        "httplib2",
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)