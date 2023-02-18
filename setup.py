import os
from pathlib import Path
import pkg_resources
from setuptools import setup, find_packages

def setup_package():
    root = Path(__file__).parent.resolve()

    with open(root / "requirements-dev.txt") as file:
        DEVELOPMENT_MODULES = [line.strip()
                               for line in file if "-e" not in line]
    extras = {"dev": DEVELOPMENT_MODULES}
    extras["all"] = [item for group in extras.values() for item in group]

    setup(
        name="blip-ci",
        version="0.0.2",
        license="BSD-3",
        author="salesforce",
        author_email="",
        url="https://github.com/pharmapsychotic/BLIP",
        description="BLIP library for use with CLIP Interrogator",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[
            str(r)
            for r in pkg_resources.parse_requirements(
                open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
            )
        ],
        include_package_data=True,
        extras_require=extras,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 2 - Pre-Alpha",
        ],
        python_requires=">=3.6",
    )


if __name__ == "__main__":
    setup_package()
