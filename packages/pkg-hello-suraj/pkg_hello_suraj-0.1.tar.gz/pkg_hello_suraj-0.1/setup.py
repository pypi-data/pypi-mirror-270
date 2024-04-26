from setuptools import setup, find_packages

setup(
    name='pkg_hello_suraj',
    version='0.1',
    packages=find_packages(),
    description='A simple hello world package',
    long_description=open('README.md').read(),
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
