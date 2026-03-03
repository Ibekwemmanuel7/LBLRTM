# LBLRTM

\# LBLRTM Atmospheric Profile Pipeline



This repository builds physically consistent 50 km atmospheric profiles from Antarctic radiosonde observations and generates LBLRTM-compatible TAPE5 input files.



The current implementation focuses on \*\*summer profiles\*\* for:



\- Dome C (Antarctica Plateau)

\- Mario Zucchelli Station (MZS, coastal Antarctica)



---



\## Overview



The pipeline performs the following steps:



1\. Ingest radiosonde observations

2\. Compute thermodynamic variables (including water vapor volume mixing ratio)

3\. Extend the atmosphere to 50 km using climatology

4\. Re-grid to a uniform 150-layer structure

5\. Generate LBLRTM-ready TAPE5 input files



---



\## Repository Structure

