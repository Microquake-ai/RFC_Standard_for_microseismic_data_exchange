
## Executive Summary


## Executive Summary

This Request for Comments (RFC) proposes a standardized format for microseismic data exchange. Primarily optimized for in-mine monitoring systems, the format holds universal relevance for all microseismic data dependent on local coordinate systems.

Our objective is to simplify the exchange of microseismic data between various platforms and vendors. Presently, data conversions can undergo lossy transformations, ushering in reconciliation challenges and inconsistencies. The task of cross-referencing multiple data elements, such as event data, system information, sensor response, and waveform data, remains intricate and often ambiguous.

Central to our proposal is the exploitation of the Adaptable Seismic Data Format (ASDF), with suggested minor adjustments ensuring unchanged compatibility with other platforms. The ASDF adopts well-established file formats from seismology:

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
eyJoaXN0b3J5IjpbNjE3NjExMTMsMTg0Nzg2MzM0NCwtMjA2MD
UxOTE0MCwxNDgxNDY3ODkxXX0=
-->