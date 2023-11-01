## Executive Summary

This purpose of the RFC is to seek comments and suggestion regarding a proposed format for the exchange of microseismic data. The focus is on microseismic data collected by in-mine monitoring system, however, the proposed format is suited for any kind of microseismic data expressed in local coordinate system. 

The scope of the exchange format encompasses four types of data including the waveforms, the catalogs and system information and grids. The proposed format exploits versatile and powerful formats broadly adopted by the seismology community. 

The table below provides an overview of the different types of data and the proposed containers.

|Data Type  | Format  |
|--|--|
| Waveform | miniSEED  |
| Catalog  | QuakeML   |
| Inventory/System | StationXML |
| Grid | HDF5 |

For distributing the information, we propose exploiting the Adaptable Seismic Data Format (ASDF) to further and consistently package the Waveform, Catalog and Inventory information in one single file. 

To facilitate the adoption of the format and the manipulation of seismological objects, we are releasing the $\mu$quake (micro-quake) library, an open source Python API built on top of Obspy. The $\mu$quake library provide access to objects and functions enabling to transparent handling of elements specific to $\mu$seismic monitoring. In particular, it allows the seamless use of a Cartesian coordinate system instead of the latitude and longitude.

The objective is to get consensus and approval by the industry and suppliers of $\mu$seismic monitoring on the data format by the end of 2024. 

Contribution and comments are encouraged and welcome.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4MTQ2Nzg5MV19
-->