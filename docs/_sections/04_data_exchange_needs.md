---

---

## Data Exchange Requirements

### Overview

The intended application directly governs the specificity of data requirements. When catalog data meets quality standards and its classification, location, and source parameters are reliable, it may suffice for certain applications. However, for more demanding or complex tasks, raw waveforms and accompanying metadata become essential. Sole reliance on catalog data in such instances often leads to ill-posed problems characterized by insufficient model space orthogonality and ambiguous solutions. To fully leverage waveform data, access to inventory or system metadata is imperative for instrument localization and sensor characterization. For completeness, one could also benefit from access to seismic velocities, especially when 3D models are used.

### Seismic System Information Categories

Seismic system information can be partitioned into four main categories:

- **Catalog:** Catalog data includes processed attributes related to seismic events: time, location, magnitude, amplitude (PPV, PPA), classification, *P*P- and *S*S-wave picks, and moment tensor/focal mechanism data.
    
- **Inventory:** Details the seismic network, stations, and sensor configurations. This includes sensor location, type, response, and orientations. Inventory data should facilitate necessary data manipulation for analysis.
    
- **Waveform:** Raw or event-triggered time-series data recorded by the instruments, foundational for all seismic analyses.
    
- **Velocities/Travel Time Grids:** Required for location, magnitude calculation, and moment tensor inversion. Allows for ray tracing and wavefield rotation to isolate P- and S-waves.

Information in these categories must be internally coherent, enabling straightforward cross-referencing and understanding of data provenance and relationships.

### Waveforms

Waveforms should include:

- Instrument and channel ID
- Sampling rate or interval
- Start time
- Amplitude, in ADC counts or physical units

### Catalog

Catalog data is bifurcated into:

- **Event-related:** Minimum requirements:
    - Time (local and UTC)
    - Location
    - Classification 
    - Magnitude, along with seismic moment \( M<sub>0</sub>_0 \) and corner frequency \( f<sub>c</sub>_c \) for moment magnitude
    - Radiated energy for *P*P- and *S*S-waves
    - Moment tensor solution if available

- **Waveform-related:** Derived from waveform data:
    - Picks: *P*P- and *S*S-wave onset times
    - Amplitude: Information, evaluation mode, and status

### Inventory/System Information

Minimum inventory requirements:

- Instrument ID
- Location
- Channel orientations
- Instrument response, per channel

### Velocity Grids

A functional velocity grid should comprise:

- Origin
- Spacing between grid nodes
- Dimensions: Number of grid points in each axis
- Data: Grid values
- Units (m or ft)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMzE2NDc2NTFdfQ==
-->
