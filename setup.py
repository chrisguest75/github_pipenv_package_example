from distutils.core import setup

setup(
    name='github_pipenv_package_example',
    version='0.1.0',
    author='Chris Guest',
    author_email='chris@chrisguest.dev',
    packages=['github_pipenv_package_example'],
    scripts=[],
    url='https://github.com/chrisguest75/github_pipenv_package_example',
    license='LICENSE.txt',
    description='This is a simple demonstration of hosting a Python package on Github',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)