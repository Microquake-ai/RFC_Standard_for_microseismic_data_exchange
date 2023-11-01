
## Executive Summary

The RFC aims to solicit feedback on a standardized format for microseismic data exchange. While the format is optimized for in-mine monitoring systems, it is applicable to all microseismic data reliant on local coordinate systems. 

The proposed schema covers four categories of data: waveforms, catalogs, system information, and grids. Existing data formats widely recognized in seismology are employed without modification efor each type:

|Data Type        | Format     |
|-----------------|------------|
| Waveform        | miniSEED    |
| Catalog         | QuakeML     |
| System Inventory| StationXML  |
| Grid            | HDF5        |

To streamline data distribution, we recommend the use of the Adaptable Seismic Data Format (ASDF), which allows for the cohesive packaging of Waveform, Catalog, and System Inventory into a single file. This document details the dataformat and the 

To facilitate the adoption of the proposed format we are introducing the μquake library — a Python API built upon Obspy — for easier manipulation of seismological objects. This library offers specialized functions for microseismic monitoring, including the provision for a Cartesian coordinate system as an alternative to geographic coordinates.

The ultimate goal is to secure industry and supplier consensus on this format by the close of 2024. 

Feedback is both encouraged and welcomed.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5MjE4MDk1MywxNDgxNDY3ODkxXX0=
-->