# Piping & Instrumentation Diagram (P&ID) Symbol Key
**Standard Framework:** ISA-5.1 Automation Symbols and Identification

## 1. Instrument Identification Tagging
The letters on the P&ID balloons denote the variables tracked and engineering functions:
- **First Letter (Measured Variable):**
  - `F` = Flow
  - `P` = Pressure
  - `T` = Temperature
  - `A` = Analysis (NIR Spectrometer, E-Tongue, E-Nose, Gas Sniffers)
- **Succeeding Letters (Component Function):**
  - `I` = Indicator
  - `T` = Transmitter
  - `V` = Valve
  - `C` = Controller

## 2. P&ID Instrument Symbols Lookup

| Tag Identifier | Component Class | Functional Logic & Architectural Placement | Balloon Representation |
| :--- | :--- | :--- | :--- |
| **FIT-01** | Flow Transmitter | **Inline Electromagnetic Flowmeter**: Placed on primary loop line to confirm fluid velocities stay under static ignition limits (<1.5 m/s). | `◯` (Field Mounted) |
| **PIT-01** | Pressure Transmitter | **Sanitary Diaphragm Pressure Sensor**: Hardwired directly to GuardLogix Safety task to catch pressure spikes. | `<◯>` (Safety Element) |
| **AIT-01** | Analytical Transmitter | **Inline NIR Spectrometer optical probe**: Sends live multi-wavelength infrared spectrum array to Edge computing node. | `[◯]` (Shared Controller Layer) |
| **AE-01** | Analytical Element | **E-Tongue Electrochemical Array**: Submersed inside an inline flow cell to track real-time polyphenol extraction. | `◯` (Field Mounted) |
| **XV-101** | Isolation Valve | **Pneumatic Spring-Return Ball Valve**: Fails to the closed position immediately if instrument air or electrical 24VDC loops go dark. | `⧓` with a top box `[XV]` |
| **ASH-01** | Gas Monitor Sensor | **Explosion-Proof LEL Gas Sniffer**: Placed on facility floor to trace ethanol vapor leaks. | `<◯>` (Safety Element) |
