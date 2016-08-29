import os
from setuptools import setup, find_packages

requires = [
    'cornice',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_zodbconn',
    'transaction',
    'ZODB3',
    'waitress',
    'docutils',
]

setup(name='online-coding-helper',
    version=0.1,
    description='Online Coding Helper',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web programming programmer utility tool",
    author='Rom Gapuz',
    author_email='rom.gapuz@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points = """\
        [paste.app_factory]
        main=app:main
        """,
    paster_plugins=['pyramid'])
