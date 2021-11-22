import io
from setuptools import find_packages, setup

setup(
    name             = 'Crawler_program',
    version          = '1.0',
    description      = 'Crawler',
    author           = 'och',
    author_email     = 'shining@sk.com',
    install_requires = ['beautifulsoup4'],
    packages= find_packages(),
    keywords         = ['test', 'lesson'],
    python_requires  = '>=3.6',
    package_data={"andyutil":[
      'data/domains.txt'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)