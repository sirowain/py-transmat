import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transmat",
    version="0.1",
    author="Riccardo Albertini",
    author_email="ssirowain@gmail.com",
    description="Upload and download file via WeTransfer from terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirowain/transmat",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'transmat = transmat.transmat:main',
        ],
    },
    install_requires=['requests', 'py3wetransfer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
