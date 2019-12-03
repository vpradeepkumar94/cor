import setuptools


setuptools.setup(
    name="core", # Replace with your own username
    version="0.0.1",
    author="Pradeep Kumar",
    author_email="vpradeepkumar94@gmail.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)