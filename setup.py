from setuptools import setup

setup(name='compute_RTOP',
      version='0.1',
      description='Compute RTOP given a dMRI image and a mask',
      url='',
      author='Maëliss Jallais',
      author_email='maeliss.jallais@inria.fr',
      license='MIT',
      packages=['compute_RTOP'],
      install_requires=[
          'astropy',
          'nibabel',
          'dipy',
      ],
      scripts=[
          'scripts/compute_RTOP'
      ],
      zip_safe=True)

