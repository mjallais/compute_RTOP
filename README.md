# compute_RTOP

### Use:
In python script by importing:
```python
from compute_RTOP.RTOP import compute_RTOP
```
OR in command line:
```bash
python compute_RTOP.py arg1_dwi arg2_mask arg3_bvals arg4_bvecs
```

Requires 4 arguments:
- path to the dMRI image
- path to the mask on which to compute RTOP (must be in the same space as the dMRI image)
- path to the b-values used during the acquisition
- path to the b-vectors used during the acquisition
