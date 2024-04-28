from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# python3 setup.py sdist
# twine check dist/*
# twine upload dist/*
# python setup.py develop

setup(
    name='proofproposition',
    version='0.0.1',
    description='Proposition Logic',
    url='https://github.com/HappyMayzhang/proofproposition',
    author='may.xiaoya.zhang',
    author_email='may.xiaoya.zhang@gmail.com',
    entry_points={
        'console_scripts':[
            'proof=proofproposition.main:main'
        ]
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.3',
    install_requires=[
        'TatSu>=5.12.0'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
