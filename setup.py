from setuptools import setup, find_packages

setup(
    name="easysql",
    version="0.1.0",
    author="Atul Tiwari",
    description="Simple MySQL utility library for Python",
    packages=find_packages(include=["easysql", "easysql.*"]),
    include_package_data=True,
    install_requires=[
        "pymysql"
    ],
    python_requires=">=3.8",
)