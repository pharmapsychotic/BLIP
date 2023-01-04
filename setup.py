from pathlib import Path
from setuptools import setup, find_packages


def setup_package():

    package_name = "blip"
    root = Path(__file__).parent.resolve()
    print("roo", root)

    with open(root / "README.md", "r") as fh:
        long_description = fh.read()

    with open(root / "requirements.txt") as file:
        REQUIRED_MODULES = [line.strip() for line in file]

    with open(root / "requirements-dev.txt") as file:
        DEVELOPMENT_MODULES = [line.strip()
                               for line in file if "-e" not in line]

    extras = {"dev": DEVELOPMENT_MODULES}
    extras["all"] = [item for group in extras.values() for item in group]

    setup(
        name=package_name,
        description="",
        author="salesforce",
        author_email="",
        url="",
        version="",
        license="",
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=REQUIRED_MODULES,
        packages=find_packages(),
        extras_require=extras,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 2 - Pre-Alpha",
        ],
        python_requires=">=3.6",
        include_package_data=True,
    )


if __name__ == "__main__":
    setup_package()
