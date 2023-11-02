---

---

## Introduction

### Purpose

This RFC aims to invite comments on a suggested format to allow for standardized and consistent access to $\mu$seismic data collected by mine μseismic monitoring systems. The proposed conventions and format objective is to enable a seamless, lossless and convenient exchange between different platforms. It considers future needs for developing high-performance, flexible, and accurate artificial intelligence that is envisioned to use the full range of available seismic data.

> **Note:** The objective of the proposed standard **does not** concern or prescribe how seismic data are **internally managed** within proprietary platforms, although the proposed implementation is designed for high performance and computational efficiency and would be suited for that purpose.

The proposed standard applies to triggered events and continuous recording alike and is suited for efficiently storing the high-density DAS data.

Access to the μseismic data collected by in-mine monitoring systems is currently inconsistent. Variations arise from site to site and vendor to vendor and are often tailored to third-party requests. Such inconsistencies lead to inefficiencies, making data usage unnecessarily challenging and limiting the potential of μseismic data.

To ensure mines have access to technologies and approaches leading to optimal outcomes permitting the safe and productive operation of mines, allowing unrestricted access to μseismic data in a standardized format is a must.

This document proposes conventions and a format for the lossless and seamless exchange of μseismic data.

We seek alignment from different stakeholders, including μseismic system and service providers, end-clients, industry practitioners, academic researchers, and research institutions.

### Scope

The standard outlined in this RFC seeks to:

- Define comprehensive, flexible and extensible data formats and structure for μseismic data exchange, encapsulating all necessary data elements to foster the normalization of data processing and analysis. The proposed framework is designed to enhance interoperability between various sites and vendors, minimizing discrepancies stemming from the lack of common reference.
- Propose adaptations to the base format to capture the essence of mining data.
  - Defining a list of acceptable event types in mining.
  - Establishing an unequivocal and standardized naming convention for the logical organization of the seismic system components.

### Objective

This RFC aims to:

- Foster a standardized representation of μseismic data, creating a universally accepted convention and eliminating fragmented or inconsistent data representations.
- Facilitate an efficient mechanism for the storage, dissemination, and accessibility of μseismic data. Ensuring versatility and catering to diverse applications ranging from real-time processing to long-term data analysis.
- Promote cross-platform compatibility, ensuring the data can be seamlessly processed, interpreted, and utilized irrespective of the platform, tool, or system.
- Enhance data integrity, ensuring it remains consistent, accurate, and unaltered during exchanges, making it reliable for various analytical and operational purposes.

### Rationale

#### Need for a New Standard

The increase in microseismic data, particularly from expansive monitoring systems and new technologies like DAS, underscores the pressing need for an efficient and unified data format. Currently, the system information, catalog, and waveform data are provided in a series of files that do not allow simple cross-referencing. For instance, one file may refer to a sensor with a long name, whereas another uses a numerical ID. The link between the name and the numerical ID is left ambiguous. Some other essential information such as the sensor types to identify whether the sensor is a 4.5Hz or 15Hz geophone, a high-frequency accelerometer, or a low-frequency FBA.

The varied nature of microseismic data formats hinders streamlined integration and analysis, posing challenges in managing and deriving value in datasets collected by in-mine monitoring systems. The lossy and incoherent nature of current data exchange formats hinders innovation and makes the utilization of μseismic data unnecessarily tricky. Given the critical importance of microseismic data in ensuring safety and improving underground mining operations, establishing a standardized format and mechanism of exchange becomes imperative. The proposed standard objective is facilitating more straightforward data access, efficient storage, smoother data exchanges across different platforms, and accommodating various data types.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDUwNTk3MDAsMTM5ODQ1MDg2OV19
-->