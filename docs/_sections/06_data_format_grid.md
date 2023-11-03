---

---

## Grid Data Format

### Overview

The HDF5 format serves as a robust and scalable data storage platform optimized for handling complex and large datasets. In the realm of microseismic monitoring, the format's hierarchical file architecture, akin to a filesystem, proves invaluable for organizing grid data and associated metadata efficiently.

Two primary categories of grids are relevant:
- **Global**: These grids extend across the entire network, typical examples being *P*- and *S*-wave velocity grids.
- **Instrument Specific**: These grids are confined to individual instruments and are typically used for storing travel time and angle information.

We recommend compartmentalizing similar types of grids into single HDF5 files for clarity and accessibility. For instance, all *P*- and *S*-wave velocity grids would reside in one file, all travel time grids in another, and all angle grids in a separate file.

The scope for these grid storage is confined to two categories—regular and rectilinear grids:
- **Regular Grid**: This grid maintains uniform spacing between grid points across all dimensions, essentially forming a cubic lattice in 3D.
- **Rectilinear Grid**: Here, the spacing can differ along each axis while still maintaining orthogonality. In 3D, it manifests as an axis-aligned, deformed cubic lattice.

### Data Structure and Metadata

The proposed HDF5 data structure for both global and instrument-specific grids comprises consistent metadata attributes to define the grid's geometric properties.

#### Common Attributes

- **Origin**: Coordinate of the grid's origin point where spatial indices are (0,0,0), defined in the coordinate system in use (`enu` or `ned`).
- **Spacing**: Describes the inter-point spacing along each axis (x, y, z), specified in units congruent with the coordinate system.
- **Dimensions**: Indicates the number of grid points along each axis (x, y, z), dictating the grid's size and shape.
- **Type**: Enumerated data field indicating the kind of values stored in the grid. Possible types include:
  - `VELOCITY` for velocity in m/sec
  - `SLOWNESS` for slowness in sec/m
  - `TIME` for time in sec
  - `TAKEOFF` for takeoff angles in a 3D grid
  - `AZIMUTH` for azimuth angles
- **Data**: The actual grid data points storing the values.

#### HDF5 Structure

For global grids, the suggested HDF5 structure is as follows:

```
/Phase {P or S}
    @Origin
    @Spacing
    @Dimensions
    @Type
    /Data
```


For instrument-specific grids, the structure is proposed to be:

```
/type
    /instrumentID
        /grid
            @origin
            @spacing
            @dimensions
            /data
```

This layout ensures a standardized and accessible approach to microseismic grid data storage, accommodating both global and instrument-specific needs.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxMTgyMTg1MCw5NTY0MDk3NCwyMTI0Mj
IzNTYzLC0xNDk2ODMwOTA1LDM5OTI2NzU4NSwtMjE0NDcwODk1
OF19
-->