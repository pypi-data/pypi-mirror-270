from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='dinarlib',
  version='0.0.2',
  author='FORTUNA287',
  author_email='shakhmametov1020@gmail.com',
  description='This library simplifies the code',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/ShakhmametovDinar',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='dinar quick_sort intersec',
  project_urls={
    'GitHub': 'https://github.com/ShakhmametovDinar'
  },
  python_requires='>=3.6'
)