---

---

## Grid Data Format

### Overview

The HDF5 format serves as a robust and scalable data storage platform optimized for handling complex and large datasets. In the realm of microseismic monitoring, the format's hierarchical file architecture, akin to a file system, proves invaluable for organizing grid data and associated metadata efficiently.

Two primary categories of grids are relevant:
- **Global**: These grids extend across the entire network, typical examples being *P*- and *S*-wave velocity grids.
- **Instrument Specific**: These grids are confined to individual instruments and are typically used for storing travel time and angle information.

**Velocity Grid**
```	
/Phase {P or S} for Velocity Grid and InstrumentID for travel time 
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
**Instrument Grids (Velocity, Angles)**

For instrument-specific grids, the structure is proposed to be:

```
/Phase {P or S} (Group)
	/InstrumentID (Group)
		/Grid Type ('TIME', 'AZIMUTH', 'TAKEOFF', ...) 
		    @Grid ID (Attribute, type: string)
		    @Seed Station Code (Attribute, type: str)
		    @Seed Location Code (Attribute, type: str)
		    @Seed Coordinate System (Attribute, type: str)
		    @Seed Coordinates (Attribute type: float[3])
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

> Note: The only difference between the global (Velocity) and instrument specific grid definition is that for instrument grid, additional parameters are added to ensure cross-referencing to a velocity grid (`Velocity Model ID`) and that the Seed information is preserved (`Seed Station`, `Seed Location`, `Seed Coordinate System`, `Seed Coordinates`).  

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTg0MjY1MDMsMTg5ODYzOTkxMSwtMj
AwNzA3MTc5LDExMjQ0NzgzMiwyMTg3NTM5NTQsMTk1MDQ2Njc3
NCwtMTMzNjg5OTA0MSwtMjA3MzAwMDM1MSwtMjEwMDUzNjEwMS
wtMTg1NDg4MDUyOSw3NzM1NDU1NDksLTIwMjY3MjAwMjcsMjA4
NDE3Mzk4MywtMjUwOTQwMjY0LDE4MDEzNTQ0ODQsMTM2Njk5MD
U4NCwyMDk1MDk5NDUwLC0xMTI2NzIxNDY1LDk1NjQwOTc0LDIx
MjQyMjM1NjNdfQ==
-->