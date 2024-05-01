from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='EcoStock',
    version='0.5',
    author="Antonio Paparo, Giovanni Paparo, Ludovica De Giacomo and Francesco Caldo",
    author_email="antoniopaparo@outlook.com",
    description='A Python package for investigating the correlation between economic and financial data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tonij10/fastapi-project",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'argparse',
        'uvicorn',
        'pandas',
        'numpy',
        'matplotlib',
        'yfinance',
        'plotly',
        'requests',
        'seaborn',
        'statsmodels',
        'uuid',

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
