import setuptools

setuptools.setup(
    name="kayoc",
    version="0.0.7",
    packages=setuptools.find_packages(),
    install_requires=["requests==2.31.0", "aiohttp==3.9.3"],
)