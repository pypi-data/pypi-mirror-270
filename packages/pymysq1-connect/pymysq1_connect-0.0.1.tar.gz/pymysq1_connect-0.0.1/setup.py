from setuptools import setup, find_packages


setup(
  name='pymysq1-connect',
  version='0.0.1',
  author='PythonIntepritator',
  author_email='Python@gmail.com',
  description='This is the simplest module for connect to mysql',
  long_description_content_type='text/markdown',
  url='https://github.com/artur4real/Triangle',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles',
  project_urls={
    'GitHub': 'https://github.com/artur4real/Triangle'
  },
  python_requires='>=3.6'
)