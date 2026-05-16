import streamlit as st
import time

# --- STEP A: CONFIGURATION (The "Recipe") ---
# This represents the "Master Recipe" for a Life Sciences product
RECIPE = {
    "Step 1: Raw Material Mixing": {"temp_min": 20, "temp_max": 25, "unit": "°C"},
    "Step 2: Chemical Reaction": {"ph_min": 6.5, "ph_max": 7.5, "unit": "pH"},
    "Step 3: Aseptic Filling": {"volume": 500, "tolerance": 5, "unit": "ml"}
}


st.set_page_config(page_title="Enabl3 MES Prototype", layout="centered")
st.title("MES Prototype")
st.markdown("---")

# --- STEP B: LOGIC ENGINE (The "Algorithm") ---
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1

def validate_input(step_name, value):
    rules = RECIPE[step_name]
    if "temp_min" in rules:
        return rules["temp_min"] <= value <= rules["temp_max"]
    if "ph_min" in rules:
        return rules["ph_min"] <= value <= rules["ph_max"]
    if "volume" in rules:
        return (rules["volume"] - rules["tolerance"]) <= value <= (rules["volume"] + rules["tolerance"])
    return False

# --- STEP C: THE "TO-BE" WORKFLOW ---
st.header(f"Phase {st.session_state.current_step} Execution")

if st.session_state.current_step == 1:
    step = "Step 1: Raw Material Mixing"
    val = st.number_input(f"Enter {step} ({RECIPE[step]['unit']})", value=22.0)
    if st.button("Submit & Validate"):
        if validate_input(step, val):
            st.success("Spec Validated. Transitioning to next phase...")
            time.sleep(1)
            st.session_state.current_step = 2
            st.rerun()
        else:
            st.error("OUT OF SPEC: Workflow halted for Quality Review.")

elif st.session_state.current_step == 2:
    step = "Step 2: Chemical Reaction"
    val = st.number_input(f"Enter {step} ({RECIPE[step]['unit']})", value=7.0)
    if st.button("Submit & Validate"):
        if validate_input(step, val):
            st.success("Spec Validated. Transitioning to next phase...")
            time.sleep(1)
            st.session_state.current_step = 3
            st.rerun()
        else:
            st.error("CRITICAL ERROR: pH balance incorrect. System Lockout.")

elif st.session_state.current_step == 3:
    step = "Step 3: Aseptic Filling"
    val = st.number_input(f"Enter {step} ({RECIPE[step]['unit']})", value=500.0)
    if st.button("Submit & Validate"):
        if validate_input(step, val):
            st.success("Spec Validated. Transitioning to next phase...")
            time.sleep(1)
            st.session_state.current_step = 4
            st.rerun()
        else:
            st.error("OUT OF SPEC: Volume deviation detected. Batch on hold.")

elif st.session_state.current_step == 4:
    st.balloons()
    st.success("PRODUCTION COMPLETE: Batch Ready for Distribution.")
    if st.button("Reset Factory Line"):
        st.session_state.current_step = 1
        st.rerun()