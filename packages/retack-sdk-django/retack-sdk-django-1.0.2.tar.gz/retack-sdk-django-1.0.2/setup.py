from setuptools import setup, find_packages

setup(
    name='retack-sdk-django',
    version='1.0.2',
    description='Retack SDK for Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Truenary',
    author_email='ramesh.shrestha@truenary.com',
    # url='https://github.com/yourusername/retack-sdk-django',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],  # Add any dependencies here
)
