from setuptools import setup, find_packages

with open("GreenLightPlus/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="GreenLightPlus",
    version="0.1.0",
    author="Daidai Qiu",
    author_email="qiu.daidai@outlook.com",
    description="Greenhouse Simulation and Optimization Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greenpeer/GreenLightPlus",
    packages=find_packages(where="GreenLightPlus"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "gymnasium",
        "openstudio==3.6.1",
        "gdown",
        "ray[rllib]",
    ],
    extras_require={
        "dev": [
            "pytest",
            "sphinx",
            "sphinx-rtd-theme",
            # Add more development dependencies here
        ],
    },
    package_data={
        # Include any data files here
    },
    entry_points={
        "console_scripts": [
            # Add any command-line scripts here
            "GreenLightPlus=GreenLight_Sim.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/greenpeer/GreenLightPlus/issues",
        "Source": "https://github.com/greenpeer/GreenLightPlus",
    },
)
