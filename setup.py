import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='bp_challenge',
    version='0.1',
    entry_points={
        'console_scripts': [
            'bpc = bp_challenge.main:main',
        ],
    },
    data_files=[('bin', ['bin/generator-linux-amd64'])],
    author="Haim Daniel",
    author_email="haimdaniel@gmail.com",
    description="The one with pyrx",
    packages=setuptools.find_packages(),
    install_requires=[
        'flask',
        'rx',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
