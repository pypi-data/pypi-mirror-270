from setuptools import setup, find_packages

classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Research',
	'License :: MIT License',
	'Programming Language :: Python :: 3',
	'Topic :: Geology',
]

setup(name='IRWPy',
      version='0.0.1',
      description='Inverse Radius Weighting Interpolation',
      author='Behnam Sadeghi',
      author_email='z5218858@zmail.unsw.edu.au',
      keywords='interpolation',
      packages=find_packages(),
      install_requires=['numpy']
     )