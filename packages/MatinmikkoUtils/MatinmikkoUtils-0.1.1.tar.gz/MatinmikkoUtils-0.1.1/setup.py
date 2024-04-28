from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 1 - Production",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="MatinmikkoUtils",
    version="0.01.01",
    packages=find_packages(),
    url="",
    license="MIT",
    author="Jan Matinmikko",
    author_email="jan.matinmikko@gmail.com",
    description="Useful tools",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    install_requires=[""],
    python_requires=">=3.0",
)
