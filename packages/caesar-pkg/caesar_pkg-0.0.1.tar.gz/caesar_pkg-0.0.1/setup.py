from setuptools import setup, find_packages

setup(
    name='caesar_pkg',
    version='0.0.1',
    author='Senthil Palanivelu',
    author_email='senthilcaesar@gmail.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

