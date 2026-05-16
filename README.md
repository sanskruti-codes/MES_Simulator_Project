# MES Digital Workflow Validator

A Python-based simulation of a Manufacturing Execution System (MES) 
for pharmaceutical production, built with Streamlit.

## What it does
Simulates a 3-step pharma manufacturing workflow with real-time 
parameter validation enforced against a Master Recipe:

- **Step 1 – Raw Material Mixing:** Temperature must be 20–25°C  
- **Step 2 – Chemical Reaction:** pH must be 6.5–7.5  
- **Step 3 – Aseptic Filling:** Volume must be 500ml ± 5ml  

If any parameter falls outside spec, the workflow halts immediately 
and flags for quality review — simulating GMP compliance standards 
used in life sciences manufacturing.

## Tech Stack
- Python
- Streamlit
- State Machine Logic (via session_state)

## How to run
pip install streamlit

streamlit run app.py

## Key Concepts Demonstrated
- Master Recipe enforcement
- AS-IS to TO-BE process mapping
- Real-time data validation
