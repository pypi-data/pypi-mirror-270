from setuptools import setup

setup(
    name='vector_database',
    version='0.0.1',
    packages=['vector_database'],
    description='A tool to build vector database quickly',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jude Wang',
    author_email='pinkr1veroops@gmail.com',
    url='https://github.com/PinkR1ver/vector_database',
    license='MIT',
    keywords='vector database',
    install_requires=[
        'numpy',
        'tkinter',
        'pandas',
        'torch',
        'torchvision',
        'rich'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)