# LBLRTM: Gas Optical Depth Profile Generation

MATLAB scripts for generating gas optical depth profiles using the Line-By-Line Radiative Transfer Model (LBLRTM) for far-infrared radiative transfer studies.

## Project Overview
This repository provides MATLAB scripts to preprocess radiosonde data and compute gas optical depth profiles using LBLRTM. The scripts process atmospheric profiles (e.g., temperature and water vapor mixing ratio from Dome C and Mario Zucchelli Station) to prepare TAPE5 inputs, and generate optical depth outputs (e.g., TAPE7 or NetCDF) for far-infrared wavelengths (e.g., 44 μm).

### Key Features
- **Radiosonde Processing**: Generates TAPE5-compatible profiles from radiosonde data.
- **Optical Depth Calculation**: Uses LBLRTM to compute gas optical depth profiles.
- **Visualization**: Produces publication-quality plots of radiosonde profiles or optical depth.

## Repository Structure
- `src/`: MATLAB scripts for processing and LBLRTM.
  - `testplot_radiosonde.m`: Plots temperature and WVMR profiles for Dome C and MZS (summer/winter).
  - `generate_od.m`: Generates optical depth profiles (placeholder).
  - `process_tape5.m`: Parses TAPE5 inputs (placeholder).
- `data/`: Radiosonde and TAPE5 files (large files at [external link]).
  - `DomeC_means.txt`, `DomeC_meanw.txt`, etc.: Radiosonde profiles.
- `docs/`: Documentation, including methodology.
- `tests/`: Validation scripts (e.g., `test_od.m\').
- `figures/`: Output plots (e.g., `Polar_Temp_WVMR_4Panel.png`) at 600 DPI.

## Prerequisites
- **MATLAB**: R2023a or later.
- **LBLRTM**: Download from [LBLRTM website](http://rtweb.aer.com/lblrtm.html).
- **MATLAB NetCDF Toolbox**: For .nc outputs (optional).
- **Sample Data**: Radiosonde files (e.g., `DomeC_means.txt`) or TAPE5 files (e.g., `TAPE5_MZSLev138`) (large datasets at [external link]).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ibekwemmanuel7/LBLRTM.git
   cd LBLRTM
   ```
2. Install MATLAB and the NetCDF toolbox (if needed).
3. Install LBLRTM (follow [LBLRTM website](http://rtweb.aer.com/lblrtm.html) instructions).
4. Ensure radiosonde files are in `data/` or download from [external link].

## Usage
1. **Process Radiosonde Data**:
   ```matlab
   run('src/testplot_radiosonde.m')
   ```
   Generates plots like `figures/Polar_Temp_WVMR_4Panel.png`.
2. **Generate Optical Depth** (when implemented):
   ```matlab
   run('src/generate_od.m')
   ```
   Produces TAPE7 or NetCDF outputs.
3. **Visualize Results**:
   Plots saved to `figures/` (600 DPI).

## Example Workflow
```matlab
% Process radiosonde data
run('src/testplot_radiosonde.m'); % Plots temperature and WVMR profiles
% Generate optical depth (placeholder)
run('src/generate_od.m'); % Outputs to data/TAPE7_output.nc
% Plot optical depth
figure;
plot(optical_depth, altitude, 'LineWidth', 1.5);
xlabel('Optical Depth'); ylabel('Altitude (km)');
set(gca, 'FontName', 'Helvetica', 'FontSize', 14);
print('figures/od_profile', '-dpng', '-r600');
```

## Data Sources
- **Radiosonde Files**: Profiles from Dome C and MZS (summer/winter, e.g., `DomeC_means.txt`, `MZS_mean.txt`).
- **TAPE5 Files**: Atmospheric profiles from Concordia Station (e.g., 138 levels).
- **TAPE7 Outputs**: Optical depth profiles (large files at [external link]).
- **External Storage**: Large datasets hosted at [external link] due to GitHub’s 100MB limit.

## Validation
- Scripts in `tests/` (e.g., `test_od.m`) validate optical depth outputs against reference data for wavelengths like 44 μm.

## Contributing
Contributions are welcome! Open an issue or submit a pull request. See `docs/methodology.md` for details.

## License
MIT License (see `LICENSE` file).

## Contact
For questions, contact [your.email@example.com] or open an issue on GitHub.

## Acknowledgments
- LBLRTM developers (Atmospheric and Environmental Research).
- Concordia Station and Mario Zucchelli Station for radiosonde data.
- [Your institution or advisor, if applicable].
