from setuptools import setup

setup(name='compute_rtop',
      version='0.1',
      description='',
      url='',
      author='',
      author_email='',
      license='MIT',
      packages=['compute_rtop'],
      install_requires=[
          'astropy',
          'nibabel',
          'dipy',
      ],
      scripts=[
          'scripts/compute_rtop'
      ],
      zip_safe=True)

