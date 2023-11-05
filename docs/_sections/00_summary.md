
## Executive Summary

This Request for Comments (RFC) proposes a standardized format for microseismic data exchange. Primarily optimized for in-mine monitoring systems, the format holds universal relevance for all microseismic data dependent on local coordinate systems.

Our objective is to simplify the exchange of microseismic data between various platforms and vendors. Presently, data conversions can undergo lossy transformations, ushering in reconciliation challenges and inconsistencies. The task of cross-referencing multiple data elements, such as event data, system information, sensor response, and waveform data, remains intricate and often ambiguous.

Central to our proposal is the exploitation of the Adaptable Seismic Data Format (ASDF), with suggested minor adjustments ensuring unchanged compatibility with other platforms. The ASDF adopts well-established file formats from seismology:

|Data Type        | Format     |
|-----------------|------------|
| Waveform        | miniSEED-like   |
| Catalog         | QuakeML  |
| System Inventory| StationXML  |

Designed for extensibility, the ASDF format facilitates atomic, computationally efficient access to waveform data. This is crucial when handling vast data volumes, such as with continuous data streams or distributed acoustic sensing (DAS).

Beyond the seismic data format, our proposal extends to the definition of grid data. We present a format tailored for the storage and transfer of such data. This suggested format is versatile, accommodating various grid types including but not limited to velocity, and travel time.

The μQuake (microQuake) library serves as a practical mechanism to adopt the standards we outline in this proposal. While its foundation lies in Obspy, μQuake is tailored specifically to the nuances of microseismic monitoring. Beyond the core capabilities of Obspy, μQuake has evolved over time, with Version 2.0 poised to incorporate support for the ASDF file format and the grid structures proposed herein, ensuring a seamless integration of these new standards.

Our objective is to see a progressive adoption of the standard by the industry and the supplier and to provide a blueprint for a mode.

Your feedback is essential and greatly appreciated.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg4Njg3MDQ4NywtNzk4ODM0MzEsLTE0Nz
cwNjc4MCwtMTUyMzI0MjI0LDE0ODc0MDUyNTMsLTExOTQxODU1
MzAsMTg0Nzg2MzM0NCwtMjA2MDUxOTE0MCwxNDgxNDY3ODkxXX
0=
-->