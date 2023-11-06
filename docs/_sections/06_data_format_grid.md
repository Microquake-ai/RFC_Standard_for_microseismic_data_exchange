---

---

## Grid Data Format

### Overview

The HDF5 format serves as a robust and scalable data storage platform optimized for handling complex and large datasets. In the realm of microseismic monitoring, the format's hierarchical file architecture, akin to a file system, proves invaluable for organizing grid data and associated metadata efficiently.

Two primary categories of grids are relevant:
- **Global**: These grids extend across the entire network, typical examples being *P*- and *S*-wave velocity grids.
- **Instrument Specific**: These grids are confined to individual instruments and are typically used for storing travel time and angle information.

For simplicity and portability, we suggest combining the grids in one convenient containers with the following structure





```	
@Type (Attribute, type: {'GLOBAL', 'LOCAL'})
/Label Phase {P or S} for Velocity Grid and InstrumentID for travel time 
    @Grid ID (Attribute, type: string)
    @Schema Version (Attribute, type: string)
    @Creation Timestamp (Attribute, type: string - ISO 8601 format)
    @Type (Attribute, type: string - value from the set {'VELOCITY'})
    @Units (Attribute, type: string - value from the set {'m/s', 'ft/s', 's/m', 'ft/s'})
    @Coordinate System (Attribute, type: string - reference to coordinate system used)
    @Origin (Attribute, type: float[3])
    @Spacing (Attribute, type: float[3])
    @Dimensions (Attribute, type: int[3])
    @Compression (Attribute, type: string - description of any compression used)
    /Data (Dataset, type: float[n, m, l], optional: checksum)
```

The structure accommodates both a single and multiple phase.

For instrument-specific grids, the structure is proposed to be:

```
@Type (Attribute, type: string - value from the set {'TIME', 'ANGLE'})
/Phase {P or S} (Group)
	Velocity Grid
	/InstrumentID (Group)
		/Grid Type ('TIME', 'AZIMUTH', 'TAKEOFF', ...) 
			Local Grid
		    @Grid ID (Attribute, type: string)
		    @Schema Version (Attribute, type: string
		    @Velocity Model ID (Attribute, type: string)
		    @Schema Version (Attribute, type: string)
		    @Modification Timestamp (Attribute, type: string - ISO 8601 format)
		    @Type (Attribute, type: string - value from the set {'TIME', 'ANGLE'})
		    @Units (Attribute, type: string - value from the set {'SECOND', 'DEGREES'})
		    @Coordinate System (Attribute, type: string - reference to coordinate system used)
		    @Origin (Attribute, type: float[3])
		    @Spacing (Attribute, type: float[3])
		    @Dimensions (Attribute, type: int[3])
		    @Compression (Attribute, type: string - description of any compression used)
		    /Data (Dataset, type: float[n, m, l], optional: checksum)
```

This layout ensures a standardized and accessible approach to microseismic grid data storage, accommodating both global and instrument-specific needs.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkzNjQzMDU5NSwtMTMzNjg5OTA0MSwtMj
A3MzAwMDM1MSwtMjEwMDUzNjEwMSwtMTg1NDg4MDUyOSw3NzM1
NDU1NDksLTIwMjY3MjAwMjcsMjA4NDE3Mzk4MywtMjUwOTQwMj
Y0LDE4MDEzNTQ0ODQsMTM2Njk5MDU4NCwyMDk1MDk5NDUwLC0x
MTI2NzIxNDY1LDk1NjQwOTc0LDIxMjQyMjM1NjMsLTE0OTY4Mz
A5MDUsMzk5MjY3NTg1LC0yMTQ0NzA4OTU4XX0=
-->