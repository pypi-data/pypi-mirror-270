from setuptools import setup, find_packages

long_description = ""
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='colorful_logging',
    version='0.3',
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/zamoosh/colorful_logging',
    author='zamoosh',
    author_email='moyi.pary@gmail.com',
    description='A library to print colorful',
    long_description_content_type="text/markdown",
    long_description=long_description,
    license='MIT',
    keywords="colorful logging, color printing, color output",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
