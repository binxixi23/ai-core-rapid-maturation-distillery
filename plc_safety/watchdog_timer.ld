// Studio 5000 Logix Designer - ASCII Representation
// Task: AI_Watchdog_Interlock (Periodic Task, Rate = 10ms)
// Hardware Tier: GuardLogix Safety Partner Processor

RUNG 0
Description: Detect a state transition (0 to 1 OR 1 to 0) from the AI Server Heartbeat tag.
  XOR AI_Watchdog_Heartbeat AI_Last_Heartbeat_State OTE AI_Heartbeat_Changed 

RUNG 1
Description: If the heartbeat state changed, reset the watchdog timer. If it stalls, the timer accumulates milliseconds.
  XIO AI_Heartbeat_Changed TON AI_Watchdog_Timer 2000 0 

RUNG 2
Description: Sync memory latch with current heartbeat status for the next logic scan.
  XIC AI_Watchdog_Heartbeat OTE AI_Last_Heartbeat_State
  XIO AI_Watchdog_Heartbeat XIO AI_Last_Heartbeat_State RES AI_Last_Heartbeat_State

RUNG 3
Description: If the timer reaches its preset 2000ms boundary, permanently latch a Communication Fault.
  XIC AI_Watchdog_Timer.DN OTE AI_Communication_Fault

RUNG 4
Description: Master Safety Permissive Line. Instantly cuts off AI control loops if a fault is present.
  XIO AI_Communication_Fault OTE AI_Permissive_Active
