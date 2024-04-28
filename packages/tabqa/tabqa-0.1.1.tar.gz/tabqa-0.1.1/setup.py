from setuptools import find_packages, setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='tabqa',
    packages=find_packages(),
    version='0.1.1',
    description='This Python script provides functions to generate SQL queries based on input questions and database schemas using a pre-trained language model.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author='Ketan More',
    install_requires = ["torch", "transformers", "bitsandbytes", "accelerate", "sqlparse"],
    setup_requires = ["torch", "transformers", "bitsandbytes", "accelerate", "sqlparse"],
    tests_require= ["torch", "transformers", "bitsandbytes", "accelerate", "sqlparse"],
    test_suite='tests',
)