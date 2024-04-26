from setuptools import setup

setup(
    name='csvtojsonify',
    version='1.2.0',
    packages=['csvtojsonify'],
    entry_points={
        'console_scripts': [
            'csvtojsonify=csvtojsonify.csvtojsonify:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.9.6',
    author='Sriram Sreedhar',
    author_email='sriramsreedhar003@gmail.com',
    description='A tool to convert CSV files to JSON.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sriramsreedhar/csvtojsonify',
)
