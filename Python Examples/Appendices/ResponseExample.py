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

# Now, the Stream object should contain waveforms in acceleration, velocity, and displacement units
