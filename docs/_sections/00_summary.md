
## Executive Summary

This Request for Comments (RFC) introduces a proposed standardized format for microseismic data exchange. Optimized primarily for in-mine monitoring systems, this format is universally suitable for any microseismic data dependent on local coordinate systems.

The goal is simple: to ease the exchange of microseismic data across different platforms and vendors. Currently, data conversions often result in a lossy transformation, leading to reconciliation challenges and inconsistencies. Cross-referencing various data components, such as event data, system information, sensor response, and waveform data, is often complex and ambiguous.

Our proposed schema exploits the adaptable seismic data format (ASDF), which is based on well-established file formats widely adopted in seismology that are:

|Data Type        | Format     |
|-----------------|------------|
| Waveform        | miniSEED like   |
| Catalog         | QuakeML  |
| System Inventory| StationXML  |

The ASDF format is well-designed, extensible and allow for atomic computationally efficient access to the waveform data, essential for when working with a large volume of data as it is the case for continuous data or distributed acoustic sensing (ASDF). 

We also extend the propos



To facilitate the adoption of the proposed format, we introduce the μQuake (microQuake) library for easier manipulation of seismological objects. μQuake is an open source, Python API built upon Obspy. This library offers specialized functions for microseismic monitoring, including the provision for a Cartesian coordinate system as an alternative to geographic coordinates.

The ultimate goal is to secure industry and supplier consensus on this format by the close of 2024. 

Feedback is both encouraged and welcomed.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNzc3MjI1NzcsMTg0Nzg2MzM0NCwtMj
A2MDUxOTE0MCwxNDgxNDY3ODkxXX0=
-->