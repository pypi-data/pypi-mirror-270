from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='func_pars',
  version='0.0.1',
  author='ilya tsikhanionak',
  author_email='ilya.tsikhanionak@gmail.com',
  description='This is the simplest module for compile cpp files.',
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='cpp c++ compile',
  python_requires='>=3.6'
)
