from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = ["click"]

test_requirements = ["pytest", ]

setup(
    name="iog-sdk",
    version="0.0.1",
    author="IO.net",
    author_email="iog@io.net",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="IOG SDK - Internet of GPUs - IO.net",
    keywords=(
        "iog ionet gpu ray distributed parallel machine-learning serving python "
        "hyperparameter-tuning reinforcement-learning deep-learning"
    ),
    entry_points={
        "console_scripts": [
            "iog=iog.cli:main",
        ],
    },
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    packages=find_packages(include=["iog", "iog.*"]),
    
    test_suite="tests",
    tests_require=test_requirements,
    url="https://developers.io.net/docs/",
    zip_safe=False,
    license="Apache 2.0",
)
