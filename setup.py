import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        return f.read()


setup(
    name="tutor-contrib-enrollmentreports",
    use_scm_version=True,
    url="https://github.com/hastexo/tutor-contrib-enrollmentreports",
    project_urls={
        "Code": "https://github.com/hastexo/tutor-contrib-enrollmentreports",
        "Issue tracker": "https://github.com/hastexo/tutor-contrib-enrollmentreports/issues",  # noqa: E501
    },
    license="AGPLv3",
    description="enrollmentreports plugin for Tutor",
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["tutor <15, >=14.0.0"],
    setup_requires=["setuptools-scm"],
    entry_points={
        "tutor.plugin.v1": [
            "enrollmentreports = tutorenrollmentreports.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
