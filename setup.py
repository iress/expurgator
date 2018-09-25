import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'expurgator.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="expurgator",
    version=__version__,
    url="https://github.com/Iress/expurgator",

    author="Jeremy Epstein",
    author_email="jeremy.epstein@iress.com.au",

    description="Censor sensitive string data in Python.",
    long_description=open('README.md').read(),

    py_modules=['expurgator'],
    zip_safe=False,
    platforms='any',

    install_requires=['six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'pytest>=3', 'coverage', 'coveralls', 'setuptools>=27.3,<38.6',
            'wheel==0.30']},

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
