from setuptools import setup, find_packages

setup(
    name="clickatell",
    version="2.0.0",
    author="Stephen Leibbrandt",
    author_email="stephen.leibbrandt@clickatell.com",
    keywords=["clickatell","sms"],
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/clickatell/clickatell-python",
    license="LICENSE",
    description="Library for interacting with the Clickatell Platform SMS Gateway",
    long_description=open("README.md").read(),
    install_requires=[
        "httplib2",
    ]
)
