import setuptools


requirements = []
with open("requirements.txt", "r") as f:
    for line in f:
        requirements.append(line.strip())


setuptools.setup(
    name="hpolib-extractor",
    version="3.0.0",
    author="nabenabe0928",
    author_email="shuhei.watanabe.utokyo@gmail.com",
    url="https://github.com/nabenabe0928/hpolib-extractor/",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    platforms=["Linux"],
    install_requires=requirements,
    include_package_data=True,
)
