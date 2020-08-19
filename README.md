# compute_RTOP

Compute RTOP of a diffusion MRI image on a specified mask.

Requires 4 arguments:
- path to the dMRI image
- path to the mask on which to compute RTOP (must be in the same space as the dMRI image)
- path to the b-values used during the acquisition
- path to the b-vectors used during the acquisition


### Installation
Using pip (within the directory):
```bash
python3 -m pip install .
```
OR manually:
```bash
python setup.py install
```

### Dependencies
- nibabel
- dipy
- astropy
