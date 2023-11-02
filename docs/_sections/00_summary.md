
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

Complementing this proposal is the μQuake (microQuake) library, an open-source Python API developed on Obspy. μQuake offers an intuitive interface, ensuring smooth interactions with seismic data.

Our aim is clear: secure industry and supplier consensus on this format by the close of 2024.

Your insightful feedback is both crucial and welcomed.

Beyond the ASDF, our proposal encompasses grid data considerations. We present a format tailored for the storage and transfer of such data. This suggested format is versatile, accommodating various grid types including but not limited to velocity, and travel time.

Parallel to this proposal, we introduce the μQuake (microQuake) library. While based on Obspy, μQuake is not just a mere adaptation: it significantly extends Obspy's functionalities tailored specifically for microseismic data. Beyond its inherent capabilities for reading, writing, and managing seismological information, μQuake incorporates additional tools and an optimized interface to seamlessly integrate the changes we've proposed. This includes adept handling of various file types like ASDF and the grid formats delineated in this document.

Our aspiration is to achieve industry and supplier consensus on this format by the end of 2024.

Your feedback is essential and greatly appreciated.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MjMyNDIyNCwxNDg3NDA1MjUzLC0xMT
k0MTg1NTMwLDE4NDc4NjMzNDQsLTIwNjA1MTkxNDAsMTQ4MTQ2
Nzg5MV19
-->