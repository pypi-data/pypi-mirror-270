from setuptools import setup, find_packages

setup(
    name='csulb_dataset',
    version='0.1.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['data/*.csv'],  # Ensure this matches the path to your CSV files
    },
    install_requires=[
        'pandas',  # Ensure pandas is installed with your package
    ],
    author='Gurucharan Raju',
    author_email='Gurucharan.Raju-SA@csulb.edu@csulb.edu',
    description='A simple package containing a CSV dataset',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
