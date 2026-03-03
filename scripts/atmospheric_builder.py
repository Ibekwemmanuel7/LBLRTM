
# ==============================================================
# Atmospheric Profile Builder for LBLRTM
# ==============================================================

import numpy as np
import pandas as pd
import xarray as xr
from pathlib import Path

R = 287.0
g = 9.80665
M_air = 28.9644
M_h2o = 18.01528
M_o3  = 47.9982

def compute_water_vapor_ppmv(q):
    r = q / (1 - q)
    return r * (M_air / M_h2o) * 1e6

def integrate_height(p, T):
    z = np.zeros_like(p)
    for i in range(1, len(p)):
        T_avg = 0.5 * (T[i-1] + T[i])
        dz = (R * T_avg / g) * np.log(p[i-1] / p[i])
        z[i] = z[i-1] + dz
    return z

def interpolate_to_grid(z_old, data_old, z_new):
    return np.interp(z_new, z_old, data_old)

def build_profile(case, data_dir):

    data_dir = Path(data_dir)

    if case == "domec_summer":
        file_path = data_dir / "radiosonde" / "RDS_DOMEC_20250119_20250119.txt"
        clim_path = data_dir / "climatology" / "subsum_lev075.txt"

    elif case == "domec_winter":
        file_path = data_dir / "radiosonde" / "RDS_DOMEC_20250707_20250707.txt"
        clim_path = data_dir / "climatology" / "subwin_lev075.txt"

    elif case == "mzs_summer":
        file_path = data_dir / "radiosonde" / "RDS_MZS_20250101_20250101.txt"
        clim_path = data_dir / "climatology" / "subsum_lev075.txt"

    elif case == "mzs_winter":
        return build_from_era5(
            data_dir / "radiosonde" / "eb959c878639371795dd87cc50eba56.nc",
            data_dir / "climatology" / "subwin_lev075.txt"
        )
    else:
        raise ValueError("Invalid case")

    df = pd.read_csv(file_path, sep=r"\s+")

    tempC = df["Temp"].values
    pres  = df["Pres"].values
    rh    = df["Rh"].values
    hgt   = df["height"].values / 1000.0

    tempK = tempC + 273.15

    es = 6.112 * np.exp((17.67 * tempC) / (tempC + 243.5))
    e  = (rh / 100.0) * es
    q  = (0.622 * e) / (pres - 0.378 * e)

    wvr = compute_water_vapor_ppmv(q)

    z_new = np.linspace(hgt.min(), 50, 138)

    p_i   = interpolate_to_grid(hgt, pres, z_new)
    T_i   = interpolate_to_grid(hgt, tempK, z_new)
    h2o_i = interpolate_to_grid(hgt, wvr, z_new)

    clim = np.loadtxt(clim_path, skiprows=3)    
    z_clim = clim[:,1]

    co2_i = interpolate_to_grid(z_clim, clim[:,6], z_new)
    o3_i  = interpolate_to_grid(z_clim, clim[:,7], z_new)
    n2o_i = interpolate_to_grid(z_clim, clim[:,8], z_new)
    co_i  = interpolate_to_grid(z_clim, clim[:,9], z_new)
    ch4_i = interpolate_to_grid(z_clim, clim[:,10], z_new)
    o2_i  = interpolate_to_grid(z_clim, clim[:,11], z_new)

    idx = np.arange(1, len(z_new)+1)

    return np.column_stack([
        idx, z_new, p_i, T_i,
        h2o_i, co2_i, o3_i,
        n2o_i, co_i, ch4_i, o2_i
    ])

def build_from_era5(nc_file, climatology_file):

    ds = xr.open_dataset(nc_file)

    T = ds["t"].isel(latitude=0, longitude=0).values
    q = ds["q"].isel(latitude=0, longitude=0).values
    o3 = ds["o3"].isel(latitude=0, longitude=0).values
    p = ds["pressure_level"].values * 100

    if p[0] < p[-1]:
        p = p[::-1]
        T = T[::-1]
        q = q[::-1]
        o3 = o3[::-1]

    z = integrate_height(p, T)
    z_km = z / 1000
    p_hPa = p / 100

    h2o = compute_water_vapor_ppmv(q)
    o3_ppmv = o3 * (M_air / M_o3) * 1e6

    z_new = np.linspace(z_km.min(), 50, 138)

    p_i   = interpolate_to_grid(z_km, p_hPa, z_new)
    T_i   = interpolate_to_grid(z_km, T, z_new)
    h2o_i = interpolate_to_grid(z_km, h2o, z_new)
    o3_i  = interpolate_to_grid(z_km, o3_ppmv, z_new)

    clim = np.loadtxt(climatology_file)
    z_clim = clim[:,1]

    co2_i = interpolate_to_grid(z_clim, clim[:,6], z_new)
    n2o_i = interpolate_to_grid(z_clim, clim[:,8], z_new)
    co_i  = interpolate_to_grid(z_clim, clim[:,9], z_new)
    ch4_i = interpolate_to_grid(z_clim, clim[:,10], z_new)
    o2_i  = interpolate_to_grid(z_clim, clim[:,11], z_new)

    idx = np.arange(1, len(z_new)+1)

    return np.column_stack([
        idx, z_new, p_i, T_i,
        h2o_i, co2_i, o3_i,
        n2o_i, co_i, ch4_i, o2_i
    ])
