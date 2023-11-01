## Executive Summary

This purpose of the RFC is to seek comments and suggestion regarding a proposed format for the exchange of microseismic data. The focus is on microseismic data collected by in-mine monitoring system, however, the proposed format is suited for any kind of microseismic data expressed in local coordinate system. 

The scope of the exchange format encompasses four types of data including the waveforms, the catalogs and system information and grids. The proposed format exploits versatile and powerful formats broadly adopted by the seismology community. 

To facilitate the adoption of the format and the manipulation of seismological objects, we are releasing the $\mu$quake (micro-quake) library, an open source Python API built on top of Obspy. The $\mu$quake library provide access to objects and functions enabling to transparent handling of elements specific to $\mu$seismic monitoring. For instance, it allows defining a

The table below provides an overview of the different types of data and the proposed containers.

|Data Type  | Container  |
|--|--|
| Waveform | miniSEED  |
| Catalog  | QuakeML   |
| Inventory/System | StationXML |
| Grid | HDF5 |
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyNDgyODY2OV19
-->