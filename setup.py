from setuptools import setup, find_packages

setup(
    name="dotpush",
    version="1.0.0",
    packages=find_packages(include=["dotpush", "dotpush.*"]),
    include_package_data=True,
    install_requires=["keyring", "requests"],
    entry_points={"console_scripts": ["dotpush=dotpush.cli:main"]},
)
