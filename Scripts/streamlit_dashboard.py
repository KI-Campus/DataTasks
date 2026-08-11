import streamlit as st
import numpy as np

st.title("Response Statistics Dashboard")

st.write(
    "Mapping: veryGood = 1, good = 2, average = 3, "
    "bad = 4, veryBad = 5"
)

# Number of responses for each category
veryGood = st.number_input(
    "Number of veryGood responses",
    min_value=0,
    value=0,
    step=1
)

good = st.number_input(
    "Number of good responses",
    min_value=0,
    value=0,
    step=1
)

average = st.number_input(
    "Number of average responses",
    min_value=0,
    value=0,
    step=1
)

bad = st.number_input(
    "Number of bad responses",
    min_value=0,
    value=0,
    step=1
)

veryBad = st.number_input(
    "Number of veryBad responses",
    min_value=0,
    value=0,
    step=1
)

# Apply the mapping to the response counts
responses = (
    [1] * int(veryGood)
    + [2] * int(good)
    + [3] * int(average)
    + [4] * int(bad)
    + [5] * int(veryBad)
)

if len(responses) > 0:
    # Same direct calculation method
    median = np.median(responses)
    mean = np.mean(responses)
    std = np.std(responses)

    # Separate outputs
    st.subheader("Median")
    st.write(median)

    st.subheader("Mean")
    st.write(mean)

    st.subheader("Standard Deviation")
    st.write(std)

else:
    st.info("Enter at least one response to calculate the statistics.")