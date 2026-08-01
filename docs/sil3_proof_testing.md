# Annual SIL-3 Proof-Testing Schedule for Factory Safety Licensing

To maintain the operational license for the high-energy E-Beam and High-Voltage maturation arrays, the automation team must execute and log these functional checks annually.

## 🛠️ Mandatory Verification Routines

### Test 1: Ethanol Vapor Sniffer Trip Check
- **Method:** Inject certified 25% LEL ethanol reference gas directly onto `EX-SNIFFER-01`.
- **Pass Criteria:** Safety PLC must drop the 24VDC master safety relay and open the main power contactor within **<2.0 seconds**, killing grid power to the E-Beam.

### Test 2: Hydrostatic Over-Pressure Transient Dump
- **Method:** Isolate loop valves and manually pressure pipeline to **6.0 Bar** using a test pump.
- **Pass Criteria:** Pressure transmitter must signal the GuardLogix Safety PLC, slamming the spring-return pneumatic isolation valve (`V-DRAIN-01`) shut within **<150 milliseconds**.
