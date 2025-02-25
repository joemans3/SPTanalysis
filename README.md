![Alt text](./extras/logo/spt-analysis-logo-v2.svg)
# SPT(Single Particle Tracking)Analysis
A Python module for calculating and analyzing Mean Square Displacement (MSD) and trajectory angles from particle tracking data. This module provides robust tools for both ensemble and individual track analysis, with support for various statistical calculations and data transformations.

## Features

### MSD Analysis
- Calculate MSD for individual tracks and ensemble averages
- Support for multi-dimensional tracking data (2D/3D)
- Flexible unit conversion (pixels to microns, frames to seconds)
- Bootstrap analysis capabilities
- Built-in error calculation and statistical analysis


### Angle Analysis
- Calculate trajectory angles between consecutive segments
- Ensemble and individual track angle distributions
- Asymmetry metrics for directional analysis
- Flexible track length filtering

## Installation

### ***PyPi***

1. Run:
```bash
pip install sptanalysis
```

## Usage

### MSD Analysis

```python
# Initialize with track dictionary
track_dict = {
    "track1": [[x1,y1], [x2,y2], ...],
    "track2": [[x1,y1], [x2,y2], ...]
}
from sptanalysis.msd import MSD_Calculations_Track_Dict
msd_calc = MSD_Calculations_Track_Dict(
    track_dict,
    pixel_to_um=0.13,
    frame_to_seconds=0.02
)

# Access results
ensemble_msd = msd_calc.individual_store.ensemble_MSD
track_msds = msd_calc.individual_store.track_MSD
```
Default does not consider bootstrap for errors, rather uses SEM. For bootstrap:
```python
msd_calc = MSD_Calculations_Track_Dict(
    track_dict,
    pixel_to_um=0.13,
    frame_to_seconds=0.02,
    bootstrap=True,
    bootstrap_samples=0.1,
    bootstrap_percentile=0.9,
    bootstrap_num=100,
)
```
```python
# Initialize angle calculations
angle_calc = Track_Calculations_Individual_Dict(
    track_dict,
    pixel_to_um=0.13,
    frame_to_seconds=0.02,
    min_track_length=3
)

# Access angle results
ensemble_angles = angle_calc.individual_store.ensemble_angles
track_angles = angle_calc.individual_store.track_angles

# errors for the above
ensemble_angles_error = angle_calc.individual_store.ensemble_angles_error
track_angles_error = angle_calc.individual_store.track_angles_error

from sptanalysis.angles import asymmetry_metric
# Calculate asymmetry metric
asymmetry = asymmetry_metric(
    angle_distribution=ensemble_angles[0],  # angles at tau=0
    forward_angle_range=np.array([0, np.pi/2]),
    backward_angle_range=np.array([np.pi/2, np.pi])
)
```
## Notes

1. The module assumes sequential tau values for MSD calculations
2. Angle calculations require a minimum of 3 points per track
3. Angle measurements are in radians
4. Asymmetry metrics are bounded between -1 and 1
5. All calculations support unit conversions from pixels to physical units

## Data Structure

### Track Dictionary Format
```python
track_dict = {
    "track_ID": [[x1,y1], [x2,y2], ...],
    ...
}
```
or if including z values:
```python
track_dict = {
    "track_ID": [[x1,y1,z1], [x2,y2,z2], ...],
    ...
}
```

### MSD Analysis Output
```python
ensemble_msd = {"tau_value": msd_value, ... }
track_msd = {"track_ID": {"tau_value": msd_value, ...}, ... }
```
Similar Structure for the errors.

### Angle Analysis Output
```python
{
    "ensemble_angles": {tau: [angles...]},
    "track_angles": {track_ID: {tau: [angles...]}},
    "track_storage": {track_ID: [[x,y]...]}
}
```

## Contributing

When contributing to this module, please ensure:
1. Any modifications maintain backward compatibility
2. New features are properly documented
3. Test cases are included for new functionality
