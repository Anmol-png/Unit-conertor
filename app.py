# ============================================================
# 🌈 Streamlit Unit Converter Web App
# Author: Anmol (with ❤️ from ChatGPT)
# ------------------------------------------------------------
# ✅ Converts: Mass, Length, Temperature, Time, Speed, Area, Volume
# ✅ Option for scientific notation
# ✅ Modern gradient UI (Streamlit + CSS)
# ✅ Deployable on Google Colab or Hugging Face Spaces
# ============================================================

import streamlit as st
st.set_page_config(
    page_title="Universal Unit Converter - By Anmol Kumari",
    page_icon="⚙️",
    layout="centered"
)

st.markdown("""
<meta name="title" content="Universal Unit Converter - By Anmol Kumari">
<meta name="description" content="Convert units easily! Supports Length, Mass, Temperature, Time, Speed, and more. Free, simple and accurate.">
<meta name="keywords" content="unit converter, anmol kumari, length converter, weight converter, temperature converter, online calculator">
<meta name="author" content="Anmol Kumari">
""", unsafe_allow_html=True)

# -----------------------------
# 🌍 Unit Conversion Dictionaries
# -----------------------------
MASS = {
    "kilogram (kg)": 1000.0,
    "gram (g)": 1.0,
    "milligram (mg)": 0.001,
    "pound (lb)": 453.59237,
    "ounce (oz)": 28.349523125,
}

LENGTH = {
    "kilometer (km)": 1000.0,
    "meter (m)": 1.0,
    "centimeter (cm)": 0.01,
    "millimeter (mm)": 0.001,
    "inch (in)": 0.0254,
    "foot (ft)": 0.3048,
    "mile (mi)": 1609.344,
}

TEMPERATURE_UNITS = ["celsius (°C)", "fahrenheit (°F)", "kelvin (K)"]

TIME = {
    "second (s)": 1.0,
    "minute (min)": 60.0,
    "hour (h)": 3600.0,
    "day (d)": 86400.0,
}

SPEED = {
    "m/s": 1.0,
    "km/h": 1000.0 / 3600.0,
    "mph": 1609.344 / 3600.0,
}

AREA = {
    "m²": 1.0,
    "cm²": 0.0001,
    "ft²": 0.09290304,
}

VOLUME = {
    "liter (L)": 1.0,
    "milliliter (mL)": 0.001,
    "cubic meter (m³)": 1000.0,
    "gallon (US)": 3.785411784,
}

CATEGORIES = {
    "Mass": MASS,
    "Length": LENGTH,
    "Temperature": None,
    "Time": TIME,
    "Speed": SPEED,
    "Area": AREA,
    "Volume": VOLUME,
}

# -----------------------------
# 🌡️ Conversion Functions
# -----------------------------
def convert_temperature(value, from_unit, to_unit):
    if from_unit.startswith("celsius"):
        c = value
    elif from_unit.startswith("fahrenheit"):
        c = (value - 32) * 5 / 9
    elif from_unit.startswith("kelvin"):
        c = value - 273.15
    else:
        raise ValueError("Unknown temperature unit")

    if to_unit.startswith("celsius"):
        return c
    elif to_unit.startswith("fahrenheit"):
        return c * 9 / 5 + 32
    elif to_unit.startswith("kelvin"):
        return c + 273.15
    else:
        raise ValueError("Unknown temperature unit")


def convert_generic(value, from_unit, to_unit, table):
    base_from = table[from_unit]
    base_to = table[to_unit]
    return value * base_from / base_to


def format_number(val, scientific=False):
    if scientific:
        return f"{val:.6e}"
    if val != 0 and (abs(val) >= 1e9 or abs(val) <= 1e-6):
        return f"{val:.6e}"
    return f"{val:.6g}"


# -----------------------------
# 🎨 Streamlit Page Setup
# -----------------------------
st.set_page_config(page_title="✨ Unit Converter", page_icon="⚙️", layout="centered")

# Custom CSS (Gradient background + Card style)
st.markdown("""
    <style>
        body {
            background: radial-gradient(circle at 10% 10%, rgba(124,58,237,0.25), transparent 10%),
                        radial-gradient(circle at 90% 90%, rgba(14,165,164,0.2), transparent 10%),
                        #0f172a;
            color: white;
        }
        .stApp {
            background: none;
        }
        div[data-testid="stMarkdownContainer"] h1 {
            color: #e2e8f0;
            text-align: center;
        }
        .stButton>button {
            border-radius: 12px;
            background: linear-gradient(135deg, #7c3aed, #0ea5a4);
            color: white;
            font-weight: 600;
            border: none;
            padding: 0.6rem 1.4rem;
            transition: 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
        }
        .result-box {
            background-color: rgba(255,255,255,0.05);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            font-size: 1.2rem;
            color: #d9f99d;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧠 UI Layout
# -----------------------------
st.title("✨ Universal Unit Converter")

st.markdown("Convert between mass, length, temperature, time, speed, area, and volume — with optional scientific notation.")

category = st.selectbox("Select a category:", list(CATEGORIES.keys()))

# Show unit dropdowns based on category
if category == "Temperature":
    from_unit = st.selectbox("From Unit:", TEMPERATURE_UNITS)
    to_unit = st.selectbox("To Unit:", TEMPERATURE_UNITS)
else:
    table = CATEGORIES[category]
    from_unit = st.selectbox("From Unit:", list(table.keys()))
    to_unit = st.selectbox("To Unit:", list(table.keys()))

value = st.text_input("Enter value to convert:", "1")
scientific = st.checkbox("Show in scientific notation")

if st.button("🔁 Convert"):
    try:
        num = float(value)
        if category == "Temperature":
            result = convert_temperature(num, from_unit, to_unit)
        else:
            result = convert_generic(num, from_unit, to_unit, CATEGORIES[category])
        formatted = format_number(result, scientific)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = <b>{formatted}</b> {to_unit}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠️ Conversion error: {e}")

st.markdown("""
<div style='text-align:center; font-size:14px; color:gray; margin-top:30px;'>
© 2025 <b>Anmol Kumari</b> — All rights reserved.
</div>
""", unsafe_allow_html=True)

