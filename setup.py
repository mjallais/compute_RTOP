from setuptools import setup

setup(name='compute_rtop',
      version='0.1',
      description='Compute RTOP given a dMRI image and a mask',
      url='',
      author='Maëliss Jallais',
      author_email='maeliss.jallais@inria.fr',
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

