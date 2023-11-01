---

---

## Appendix C: Coordinate System Handling 

### Coordinate System Handling

From version 2.2.0, µquake includes classes for handling coordinates and their transformations. The main classes are `Coordinates`, `CoordinateTransformation`, and `CoordinateSystem`. Those classes are used to describe coordinates and have been integrated in the following classes:

- `uquake.core.event.Origin`
- `uquake.core.inventory.Station`
- `uquake.core.inventory.Channel`
- `uquake.grid.base.Grid`

### `Coordinates` Class

The `Coordinates` class represents a point in a specific coordinate system. It contains the following attributes and methods:

- **x, y, z: float** - Coordinates in the chosen system.
- **coordinate_system: CoordinateSystem** - Specifies whether the system is `NED` or `ENU`.
- **transformation: CoordinateTransformation** - Object for handling coordinate transformations.

### `CoordinateTransformation` Class

The `CoordinateTransformation` class handles transformations between custom coordinate systems and latitude-longitude-based systems. Attributes include:

- **translation: tuple** - Translation vector as (dx, dy, dz).
- **rotation: list or tuple** - Rotation matrix or Euler angles.
- **epsg_code: int** - EPSG code for the target coordinate system.
- **scaling: float or tuple** - Optional scaling factors.
- **reference_elevation: float** - Reference elevation for depth conversions.

### `CoordinateSystem` Enumeration

The `CoordinateSystem` enumeration specifies the coordinate system being used. It enforces a right-hand coordinate system and supports two types:

- **NED** - North, East, Down coordinate system.
- **ENU** - East, North, Up coordinate system.
