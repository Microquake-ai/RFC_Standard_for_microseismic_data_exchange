---

---

## Appendix B: Response {:#appendix-b-response}

### Instrument Response

The instrument response is a comprehensive representation of the signal transformation across the entire seismic data acquisition chain. It outlines how the original ground motion gets converted into the digital data recorded. In the SEED and Obspy frameworks, the instrument response is structured in a chain-like manner, connecting various stages such as the sensor response, pre-amplifiers, filters, and digitizers. Each stage contributes its frequency-dependent correction factors to the overall instrument response, which are often characterized by poles and zeros in the Laplace domain. By chaining these components together, one can obtain the complete response function that allows for precise ground-motion reconstruction from the recorded data.

The following example demonstrates how to construct a response for a 15 Hz geophone element connected to a 24-bit digitizer. The data are assumed to be recorded between $$\pm 2.5$$ volts and stored as ADC counts. We utilize the $$\mu$$quake library, an extension of the Obspy library specifically tailored for $$\mu$$seismic applications. The example includes code to create a synthetic stream with random values to simulate waveform data. Subsequently, it illustrates how to change the waveform representation from ADC counts to acceleration, velocity, and displacement.

```python
import numpy as np
from uquake.core import Stream, Trace, UTCDateTime
from uquake.core.inventory import Inventory, Network, Station, Channel, Site
from uquake.core.inventory.response import Response, PolesZerosResponseStage, CoefficientsTypeResponseStage

# Create Inventory, Network, and Station as before
inv = Inventory(networks=[], source="Example")
net = Network(code="XX", stations=[], description="Example Network")
sta = Station(code="STA1", x=0.0, y=0.0, z=0.0, site=Site(name="Example Site"))

# Create the Channel and Response objects
cha = Channel(code="HHZ", location_code="", x=0.0, y=0.0, z=0.0, sample_rate=100.0)
resp = Response()

# Poles and Zeros for 15 Hz geophone
pz_stage = PolesZerosResponseStage(
    stage_sequence_number=1,
    stage_gain=1.0,
    stage_gain_frequency=1.0,
    input_units="M/S",
    output_units="V",
    pz_transfer_function_type="LAPLACE (RADIANS/SECOND)",
    normalization_frequency=1.0,
    zeros=[0j],
    poles=[-94.44j, 94.44j],
    normalization_factor=1.0
)

# Coefficients for 24-bit digitizer
coeff_stage = CoefficientsTypeResponseStage(
    stage_sequence_number=2,
    stage_gain=1 / (2.5 / (2**23)),
    stage_gain_frequency=1.0,
    input_units="V",
    output_units="COUNT",
    cf_transfer_function_type="DIGITAL",
    numerator=[1.0],
    denominator=[]
)

# Add stages and complete the hierarchy
resp.response_stages.append(pz_stage)
resp.response_stages.append(coeff_stage)
cha.response = resp
sta.channels.append(cha)
net.stations.append(sta)
inv.networks.append(net)

# Create a Stream with random ADC count values simulating the data
npts = 1000
starttime = UTCDateTime(0)
sampling_rate = 100.0

# Create a single Trace object
trace = Trace(data=np.random.randint(-2**23, 2**23, npts))
trace.stats.starttime = starttime
trace.stats.sampling_rate = sampling_rate
trace.stats.network = "XX"
trace.stats.station = "STA1"
trace.stats.channel = "HHZ"

# Create a Stream object and append the Trace
stream = Stream(traces=[trace])

# Attach the response to the Stream
stream.attach_response(inv)

# Convert waveform from ADC count to physical units
stream.remove_response(output="ACC")
stream.remove_response(output="VEL")
stream.remove_response(output="DISP")
```

### IRIS NRL

The Incorporated Research Institutions for Seismology Nominal Response Library (NRL) serves as a centralized repository for sensor and digitizer responses. Inclusion of the equipment utilized in microseismic monitoring within the NRL not only guarantees the accuracy of response characteristics but also promotes standardization across platforms. This is essential for ensuring data integrity and facilitating data interchange within the broader seismic research community. Both the µquake and Obspy libraries provide mechanisms to easily integrate these NRL-specified responses into the StationXML format, thus enhancing both data fidelity and workflow efficiency.

```python
# Using uquake
from uquake.core.inventory import Inventory, Network, Station, Channel, Site
from uquake.clients.nrl import NRL

# Initialize NRL client
nrl = NRL()

# Construct response from NRL
response_uquake = nrl.get_response(
    sensor_keys=['Sensor Manufacturer', 'Sensor Model'],
    datalogger_keys=['Datalogger Manufacturer', 'Datalogger Model']
)

# Define channel with x, y, z coordinates
channel = Channel(
    code="EHZ",
    location_code="",
    x=0.0,
    y=0.0,
    z=0.0,
    response=response_uquake
)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5NzgxNDQ5NywyMzI0MzAwNjRdfQ==
-->
