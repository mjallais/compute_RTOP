import argparse
from RTOP import compute_RTOP

parser = argparse.ArgumentParser()
parser.add_argument("dwi", type=str, help="Path to the diffusion image.")
parser.add_argument("mask", type=str, help="Path to the mask image on which to compute RTOP. Mask image must be in the same space as the diffusion image.")
parser.add_argument("bvals", type=str, help="Path to the text file that contains the b-values used in the acquisition of the diffusion image.")
parser.add_argument("bvecs", type=str, help="Path to the text file that contains the b-vectors used in the acquisition of the diffusion image.")

args = parser.parse_args()

compute_RTOP(args.dwi, args.mask, args.bvals, args.bvecs)