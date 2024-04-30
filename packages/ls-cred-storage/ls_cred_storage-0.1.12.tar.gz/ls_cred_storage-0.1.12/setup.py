import setuptools
import os

os.chdir(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ls-cred-storage',
     version='0.1.12',
     author="Assaf Kalinski",
     author_email="assaf@lightsolver.com",
     description="A package containing storage user credential",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://dev.lightsolver.com",
     packages=setuptools.find_packages(),
     package_data={
         "": ["*.config"]
     },
     install_requires=[
         "keyring>=23.2.1"
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )