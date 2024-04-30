import setuptools

setuptools.setup(
    name="jimmyskitchen",
    version="0.0.1",
    author="Julius Landes",
    author_email="Lhamo.Landes@campus.lmu.de",
    description="Framework for trading US stocks",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/JuliusLhamo/JimsKitchenPublic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'GitPython',
        'pandas',
        'plotly',
        'numpy'
    ],
)