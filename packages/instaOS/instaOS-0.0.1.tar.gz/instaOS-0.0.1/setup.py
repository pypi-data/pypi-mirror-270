from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Instagram followers list and following list'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="instaOS",
    version=VERSION,
    author="Umit KOC",
    author_email="umitkoc.com@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium', 'tqdm', 'webdriver-manager','chromedriver-autoinstaller','python-dotenv','chrome-driver'],
    keywords=['instagram', 'followers', 'following', 'not following'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)