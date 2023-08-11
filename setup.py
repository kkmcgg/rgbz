from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rgbz", 
    version="0.1.0",
    author="kevin kirkaldy mcguigan",
    author_email="kevin.mcguigan@nscc.ca",
    description="A package for manipulating and working with RGBZ color data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkmcgg/rgbz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.21.0",
        "Pillow>=8.2.0",
        "tifffile>=2021.4.8"
    ]
)
