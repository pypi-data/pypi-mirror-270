from setuptools import setup, find_packages

setup(
    name="gingerai",
    version="0.1.20",
    description="Ginger AI Python Library",
    url="https://github.com/ginger-ai",
    packages=find_packages(),
    install_requires=["torch", "torchsummary", "numpy", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
