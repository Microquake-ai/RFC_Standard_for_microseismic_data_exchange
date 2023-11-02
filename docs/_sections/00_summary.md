
## Executive Summary

This Request for Comments (RFC) introduces a proposed standardized format for microseismic data exchange. Optimized primarily for in-mine monitoring systems, this format is universally suitable for any microseismic data dependent on local coordinate systems.

The goal is simple: to ease the exchange of microseismic data across different platforms and vendors. Currently, data conversions often result in a lossy transformation, leading to reconciliation challenges and inconsistencies. Cross-referencing various data components, such as event data, system information, sensor response, and waveform data, is often complex and ambiguous.

Our proposed schema exploits the adaptable seismic data format (ASDF) suggesting minor modifications that do not alter the compatibility with other platforms. The ASDF is based on well-established file formats widely adopted in seismology that are:

|Data Type        | Format     |
|-----------------|------------|
| Waveform        | miniSEED like   |
| Catalog         | QuakeML  |
| System Inventory| StationXML  |

The ASDF format is well-designed, extensible and allow for atomic computationally efficient access to the waveform data, essential for when working with a large volume of data as it is the case for continuous data or distributed acoustic sensing (ASDF). 

We also extend the proposal to grid data to store and transfer the *P*- and *S*-wave velocity information to name only those.

In tandem with this proposal, we present the μQuake (microQuake) library. As an open-source Python API built on Obspy, μQuake provides a convenient interface allowing the seamless 

Our aspiration is to achieve industry and supplier consensus on this format by the end of 2024.

Your feedback is essential and greatly appreciated.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5OTU4NjMxNSwxODQ3ODYzMzQ0LC0yMD
YwNTE5MTQwLDE0ODE0Njc4OTFdfQ==
-->