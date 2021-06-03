import os
from setuptools import setup, find_packages


version = "0.1"

install_requires = [
    'horseman',
    'orjson',
    'pydantic',
    'python-arango',
]

test_requires = [
    'docker',
    'pyhamcrest',
    'pytest',
]


setup(
    name='pydantic_arango',
    version=version,
    author='Souheil CHELFOUH',
    author_email='trollfot@gmail.com',
    url='http://gitweb.dolmen-project.org',
    download_url='http://pypi.python.org/pypi/pydantic_arango',
    description='Arango Models implementation for Pydantic',
    long_description=(open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read()),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python:: 3 :: Only',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['pydantic_arango',],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    entry_points={
       'pytest11': [
           'pydantic_arango = pydantic_arango.fixtures.arango',
       ],
    },
)
