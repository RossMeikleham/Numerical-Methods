from setuptools import setup

setup(name='numericalmethods',
      version='0.0.1',
      description='Collection of modules which implement Numerical Methods concepts',
      url='https://github.com/RossMeikleham/Numerical-Methods',
      author='RossMeikleham',
      author_email='RossMeikleham@hotmail.co.uk',
      license='MIT',
      package_dir={'numericalmethods': 'src'},
      packages=['numericalmethods'],
      install_requires=['numpy'],
      zip_safe=False)
