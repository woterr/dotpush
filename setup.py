from setuptools import setup, find_packages

setup(
    name="DotPush",
    description="A tool that helps backup dotfiles and automatically push to a remote github repository.",
    version="1.0",
    url="https://github.com/woterr/dotpush",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dotpush = dotpush.cli:main',
        ],
    },
    packages=find_packages()
)
