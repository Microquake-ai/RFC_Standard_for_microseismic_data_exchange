---

---

## Grid Data Format {:#data-format-grid}

### Overview

The HDF5 format is a flexible, high-performance data storage format designed for complex, large datasets. In the context of storing grid information, HDF5 offers a hierarchical file structure similar to a file system, facilitating the organization of data into groups and datasets. This structure allows for efficient and intuitive storage of multidimensional grid data, along with associated metadata, in a single, portable file.

We suggest defining two types of grids:
- **Global**: Grids that apply to the entire network like the *P*- and *S*-wave velocities grids
- **Instrument Specific**: Grids that apply to a specific instrument, like the travel time and angle grids

For the purpose of microseismic monitoring, we suggest organizing the information by storing all similar elements in a single file. For example, we would store all the velocity models in one file, all the travel time grids in another, and the angle grids in yet another.

In this context, we suggest limiting the scope of the grid storage to two types of structured grids: regular or rectilinear grids.
- **Regular Grid**: A grid in which the spacing between the points is constant in each dimension. In 3D, this would resemble a cubic lattice.
- **Rectilinear Grid**: A grid in which the spacing between the points can vary along each axis but remains orthogonal. In 3D, this would look like a deformed cubic lattice, where the deformations are axis-aligned.

Note that the regular grid is a special case of a rectilinear grid, where the spacing is the same along each axis.

#### General Format

The grid data structure, whether global or instrument-specific, contains common elements that define its geometry and facilitate its interpretation. A straightforward yet effective description can be achieved using the origin, spacing, and dimensions of the grid.
- **Origin**: The origin refers to the coordinate point in the grid where the spatial indices are (0,0,0). It acts as the reference point for other grid points and is specified in the coordinate system used (e.g., `enu` or `ned`).
- **Spacing**: The spacing describes the distance between adjacent grid points along each axis (x, y, z). It dictates the resolution of the grid. In regular grids, the spacing is constant, while in rectilinear grids, it can vary along each axis. The spacing is generally provided in units consistent with the chosen coordinate system.
- **Dimensions**: The dimensions specify the total number of grid points along each axis (x, y, z), thereby determining the overall size and shape of the grid.
- **Type**: This describes the type of value store inside the grids possible values are
	- VELOCITY:  velocity (m/sec); 
	- SLOWNESS: slowness (sec/m);  
	- TIME: time (sec);  
	- TAKEOFF: takeoff angles 3D grid;
	- AZIMUTH: Azimuth angle. 
- **Data**: The value at grid points


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzk5MjY3NTg1LC0yMTQ0NzA4OTU4XX0=
-->