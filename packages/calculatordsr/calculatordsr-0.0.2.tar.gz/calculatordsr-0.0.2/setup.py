import sys
from setuptools import setup

python_version = sys.version_info[:2]
required_python_version = (3,9)
if python_version < required_python_version:
   sys.stderr.write("This tool doesn't support Python version 3.9 and below. Use the latest version of Python.")
   sys.exit(1)

# with open('README.md','r',encoding = 'utf-8') as r:
#     readme = r.read()

setup(
    name = 'calculatordsr',
    packages = ['calculatordasar'],
    version = '0.0.2',
    license = 'GPL 2+',
    description = 'calculator dasar untuk penjumlahan, perkalian, pembagian dan pengurangan',
    # long_description=readme,
    long_description_content_type="text/markdown",
    author = 'Sidiq Brewstreet',
    author_email = '',
    url = '',
    keywords = ['calculator'],
    python_requires=">=3.9",
    install_requires=[
            'requests',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only'
    ],
)