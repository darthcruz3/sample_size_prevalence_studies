import streamlit as st
import math

st.title("PTTU-QAH Dynamic Sample Size Calculator for Prevalence Studies")

# -------------------------------
# Step 1: Confidence Level
# -------------------------------
st.header("Step 1: Choose your desired Confidence Level (study-power)")
confidence_level = st.select_slider(
    "Select confidence level (%)",
    options=[80, 85, 90, 95, 99, 99.5, 99.9],
    value=95
)

z_dict = {
    80: 1.282,
    85: 1.440,
    90: 1.645,
    95: 1.960,
    99: 2.576,
    99.5: 2.807,
    99.9: 3.291
}

z = z_dict[confidence_level]
st.write(f"Z-score for {confidence_level}% confidence level: {z}")

# -------------------------------
# Step 2: Prevalence (x in y)
# -------------------------------
st.header("Step 2: Enter Prevalence")
col1, col2 = st.columns(2)
with col1:
    prevalence_numerator = st.number_input("Number of positive bacterial swabs (x)", min_value=0.0, value=5.0)
with col2:
    prevalence_denominator = st.number_input("Total number of all positive swabs (y)", min_value=1.0, value=1000.0)

p = prevalence_numerator / prevalence_denominator
st.write(f"Prevalence (p): {p:.6f}")

# -------------------------------
# Step 3: Precision
# -------------------------------
st.header("Step 3: Desired Precision")
d = st.slider("Select desired absolute precision (d)", min_value=0.001, max_value=0.2, value=0.01, step=0.001)
st.write(f"Precision (d): {d}")

# -------------------------------
# Step 4: Sample size calculation
# -------------------------------
n = (z**2 * p * (1 - p)) / (d**2)
st.write(f"Required sample size (without FPC): {math.ceil(n)}")

# -------------------------------
# Step 5: Finite Population Correction (optional)
# -------------------------------
st.header("Step 4: Finite Population Correction (Optional)")
use_fpc = st.checkbox("Apply finite population correction (FPC)?")

if use_fpc:
    N = st.number_input("Enter total population size (N)", min_value=1.0, value=10000.0)
    n_adj = n / (1 + ((n - 1) / N))
    st.write(f"Adjusted sample size (with FPC): {math.ceil(n_adj)}")