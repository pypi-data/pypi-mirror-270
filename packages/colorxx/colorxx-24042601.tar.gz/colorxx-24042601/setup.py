from setuptools import setup,find_packages
import colorx


setup(
    name=colorx.__release_name__,
    version=colorx.__version__,
    description='A simple class with colorful fonts',
    author=colorx.__author__,
    author_email=colorx.__author_email__,
    packages=find_packages(),
    license="Apache 2.0",
    url=colorx.__url__,
    install_requires=[
    ],
    entry_points={
    },
    long_description="easy module to type write color full fonts",
    long_description_content_type='text/markdown'
)