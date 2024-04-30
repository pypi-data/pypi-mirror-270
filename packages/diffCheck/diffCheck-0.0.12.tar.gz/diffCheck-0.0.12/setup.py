from setuptools import setup, find_packages
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools


# def get_pybind_include(user=False):
#     import pybind11

#     return pybind11.get_include(user)



# ext_modules = [
#     Extension(
#         "diffCheckBindings",
#         ["../../diffCheckBindings.cc"],
#         include_dirs=[
#             get_pybind_include(),
#             "../../.",
#             "../../diffCheck/",
#             "../../../deps/eigen",
#             "../../../deps/open3d/win/0_18/include",

#         ],
#         language="c++",
#     ),
# ]

setup(
    name="diffCheck",
    version="0.0.12",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pybind11>=2.5.0"
        # other dependencies...
    ],
    description="DiffCheck is a package to check the differences between two timber structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andrea Settimi, Damien Gilliard, Eleni Skevaki, Marirena Kladeftira, Julien Gamerro, Stefana Parascho, and Yves Weinand",
    author_email="andrea.settimi@epfl.ch",
    url="https://github.com/diffCheckOrg/diffCheck",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],

    package_data={
        "diffCheck": ["*.dll", "*.pyd"]
        },

    # ext_modules=ext_modules,
    # cmdclass={"build_ext": build_ext},
    # zip_safe=False,
)
