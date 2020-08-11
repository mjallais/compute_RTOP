#!/usr/bin/python

# Create RTOP file of image file on the mask passed in arguments
# arg 1 : path to dMRI image
# arg 2 : path to mask
# arg 3 : path to b-values
# arg 4 : path to b-vectors

import sys
from os import path
import numpy as np
from astropy import units
import nibabel as nib
from scipy import ndimage
from dipy.core import gradients
from dipy.reconst import mapmri

def compute_RTOP(dwi_, mask_, bvals_, bvecs_):

    if path.exists(dwi_) and path.exists(mask_) and path.exists(bvals_) and path.exists(bvecs_):
        dwi = nib.load(dwi_)
        mask = nib.load(mask_)
        bvals = np.loadtxt(bvals_) * units.s / units.mm**2
        bvecs = np.loadtxt(bvecs_)
    else:
        print("One of the files do not exist, exit.")
        exit()

    dwi_data = dwi.get_data()
    mask_data = mask.get_data()

    nodif = dwi.slicer[:,:,:,0]

    gtab = gradients.gradient_table_from_bvals_bvecs(bvals,
                                                     bvecs,
                                                     b0_threshold=5)
    map_model = mapmri.MapmriModel(
            gtab,            
            laplacian_regularization=True,
            laplacian_weighting=0.2
        )
    map_fit = map_model.fit(dwi_data, mask=mask_data)
    rtop = map_fit.rtop()
    rtop_cortex_norm = rtop / rtop[mask_data!=0].mean()

    rtop_nii = nib.Nifti1Image(rtop, affine=dwi.affine)
    rtop_cortex_norm_nii = nib.Nifti1Image(rtop_cortex_norm, affine=dwi.affine)
        
    rtop_nii.to_filename('RTOP_cortex.nii.gz')
    rtop_cortex_norm_nii.to_filename('RTOP_cortex_norm.nii.gz')

    return