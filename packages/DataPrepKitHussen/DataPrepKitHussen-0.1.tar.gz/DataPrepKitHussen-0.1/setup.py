from setuptools import setup, find_packages

setup(
    name="DataPrepKitHussen",
    version="0.1",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "sklearn"],
    author="Hussen",
    description="A data preparation toolkit",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
