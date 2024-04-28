from setuptools import setup, find_packages

setup(
    name="sanda",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["click==8.1.7", "uvicorn[standard]==0.29.0", "fastapi==0.110.2"],
    entry_points={
        "console_scripts": [
            "sanda=sanda.cli.entry:cli",
        ],
    },
    author="DSP Field Engineering Team",
    author_email="dsp-fieldeng@broadinstitute.org",
    description="Sanda is a Python package designed as a Kubernetes-based proof-of-concept workflow runner. "
    "It streamlines the definition, execution, and management of cloud-agnostic workflows using YAML. "
    "The package features open-source extensibility, supports multiple access points, and manages tasks"
    " within containerized environments. Sanda is designed to be lightweight, flexible, and easy to use.",
    url="https://github.com/broad-institute/sanda",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
