import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='python_logger',
    version='0.0.1',
    description='Logging framework python',
    url='https://github.com/shivank0103/python-logger-project',
    author='Shivank Yadav',
    author_email='shivank0103@gmail.com',
    license='unlicense',
    packages=['cashifylogger'],
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[
        "fluent-logger==0.10.0",
        "msgpack==1.0.4"
    ],
    zip_safe=False
)
