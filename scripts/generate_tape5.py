# ==============================================================
# Generate TAPE5 for Summer Profiles (Dome C & MZS)
# ==============================================================

from pathlib import Path
from atmospheric_builder import build_profile  # adjust if needed

# --------------------------------------------------------------
# Directories
# --------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "radiosonde"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# --------------------------------------------------------------
# Input Files
# --------------------------------------------------------------

domec_file = DATA_DIR / "RDS_DOMEC_20250119_20250119.txt"
mzs_file   = DATA_DIR / "RDS_MZS_20250101_20250101.txt"

# --------------------------------------------------------------
# Build Profiles (50 km, 150 layers)
# --------------------------------------------------------------

domec_profile = build_profile("domec_summer", BASE_DIR / "data")
mzs_profile   = build_profile("mzs_summer", BASE_DIR / "data")

# --------------------------------------------------------------
# Save Profiles (optional text save)
# --------------------------------------------------------------

import numpy as np

np.savetxt(OUTPUT_DIR / "DomeC_Summer_150.txt", domec_profile, fmt="%10.3e")
np.savetxt(OUTPUT_DIR / "MZS_Summer_150.txt", mzs_profile, fmt="%10.3e")

print("Profiles generated successfully.")