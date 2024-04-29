from setuptools import find_packages, setup

setup(
    name="uk_std_libraries",
    version="0.0.7",
    description="Україномовна бібліотека адаптації мови Python",
    package_dir={"": "додаток"},
    packages=find_packages(where="додаток"),
    long_description="Україномовна бібліотека адаптації мови Python",
    long_description_content_type="text/markdown",
    url="https://github.com/NeoUKR/uk_std_libraries.git",
    author="Коваленко Костянтин",
    author_email="neokkv@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
