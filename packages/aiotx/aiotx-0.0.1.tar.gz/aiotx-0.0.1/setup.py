from setuptools import find_packages, setup


extras_test = (
    [
        "black",
        "flake8",
        "hypothesis",
        "isort",
        "mypy>=0.910",
        "pyproj",
        "pytest",
        "pytest-cov",
        "tox",
        "build"
    ]
)

setup(
    name="aiotx",
    use_scm_version=True,
    version="0.0.1",
    packages=find_packages(exclude=("tests",)),
    package_data={
        "aiotx": ["py.typed"],
    },
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "aiohttp",
    ],
    extras_require={
        "test": extras_test,
    }
)
