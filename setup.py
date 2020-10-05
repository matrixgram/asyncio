import setuptools

with open('README.md', 'r') as fh:
    long_descript = fh.open()
setuptools.setup(
    name='pkg-utility-matrixgram',
    version='0.0.1',
    author='Mohammad Hayeri',
    author_email='MatrixGram1994@gmail.com',
    long_descript=long_descript,
    long_descript_content_type='text/markdown',
    description='set of utilities',
    url='https://github.com/matrixgram/pkg-utility',
    packages=setuptools.findall(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Aproved ::MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
