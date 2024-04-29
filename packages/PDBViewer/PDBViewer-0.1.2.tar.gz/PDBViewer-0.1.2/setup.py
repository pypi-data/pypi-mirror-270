from setuptools import setup, find_packages

setup(
    name='PDBViewer',
    version='0.1.2',
    packages=find_packages(),
    license='MIT',
    author='Edris Sharif Rahmani',
    author_email='rahmani.biotech@gmail.com',
    description='Automatically retrieve a PDB file for a given RCSB PDB id and visualize its 3D structure.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sharifrahmanie/PDBViewer/archive/refs/tags/v0.1.1.tar.gz',
    keywords=['PDB', 'RCSB', 'Protein', '3D structure', 'Bioinformatics'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
        'py3Dmol'
    ],
)
