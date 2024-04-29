from setuptools import setup, find_packages

setup(
    name='NCBIGeneInfo',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    author='Edris Sharif Rahmani',
    author_email='rahmani.biotech@gmail.com',
    description='A package to retrieve gene information from NCBI',
    package_data={'NCBIGeneInfo': ['NCBI_gene_dict']},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sharifrahmanie/NCBIGeneInfo/archive/refs/tags/v0.1.tar.gz',
    keywords=['NCBI', 'Gene symbol', 'Gene', 'Bioinformatics'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
