
## Executive Summary

This Request for Comments (RFC) introduces a proposed standardized format for microseismic data exchange. Optimized primarily for in-mine monitoring systems, this format is universally suitable for any microseismic data dependent on local coordinate systems.

The goal is simple: to ease the exchange of microseismic data across different platforms and vendors. Currently, data conversions often result in a lossy transformation, leading to reconciliation challenges and inconsistencies. Cross-referencing various data components, such as event data, system information, sensor response, and waveform data, is often complex and ambiguous.
Our proposed schema exploits already well-established file formats widely adopted in seismology:

|Data Type        | Format     |
|-----------------|------------|
| Waveform        | miniSEED like   |
| Catalog         | QuakeML  |
| System Inventory| StationXML  |
| Grid            | HDF5        |

To streamline data distribution, we recommend the use of the Adaptable Seismic Data Format (ASDF), which allows for the cohesive packaging of Waveform, Catalog, and System Inventory serialized in familiar and widely adopted format into a single convenient file that is adapted for computational efficiency. This document details the data format, the additions and how the modifications are implemented.

To facilitate the adoption of the proposed format, we introduce the μQuake (microQuake) library for easier manipulation of seismological objects. μQuake is an open source, Python API built upon Obspy. This library offers specialized functions for microseismic monitoring, including the provision for a Cartesian coordinate system as an alternative to geographic coordinates.

The ultimate goal is to secure industry and supplier consensus on this format by the close of 2024. 

Feedback is both encouraged and welcomed.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI3ODQyOTYzNywxODQ3ODYzMzQ0LC0yMD
YwNTE5MTQwLDE0ODE0Njc4OTFdfQ==
-->