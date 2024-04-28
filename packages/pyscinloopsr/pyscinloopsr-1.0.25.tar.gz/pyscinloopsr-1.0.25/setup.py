from setuptools import find_packages, setup

setup(
    name='pyscinloopsr',
    packages=find_packages(include=['pyscinloopsr']),
    version='1.0.25',
    description='Facilitator for scientists in the loop of SR modelling',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Djalma Pereira',
    #install_requires='pysr'
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'], #tests_require=['pytest==4.4.1'],
    test_suite='tests',
)