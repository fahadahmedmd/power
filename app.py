import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate total power consumption (example calculation, adjust as needed)
def calculate_power_consumption(flow_rate, nominal_diameter, piping_weight):
    # Placeholder for the actual calculation
    total_power = flow_rate * 0.1 + nominal_diameter * 0.05 + piping_weight * 0.02
    return total_power

# Streamlit user inputs
st.title('H2 Purification Unit Power Consumption Calculator')

# File uploader for the Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    excel_data = pd.ExcelFile(uploaded_file)
    total_power_consumption_df = pd.read_excel(uploaded_file, sheet_name='Total-Power-Consumption')

    # Extract the necessary input values
    flow_rate = total_power_consumption_df.iloc[0, 3]  # Flow rate (Nm3/h)
    nominal_diameter = total_power_consumption_df.iloc[2, 3]  # Nominal diameter (NW)
    piping_weight = total_power_consumption_df.iloc[3, 3]  # Piping weight (kg)

    # Display extracted values
    st.write(f"Extracted Flow Rate: {flow_rate} Nm3/h")
    st.write(f"Extracted Nominal Diameter: {nominal_diameter} NW")
    st.write(f"Extracted Piping Weight: {piping_weight} kg")

    flow_rate = st.number_input('Input Flow rate (Nm3/h)', value=flow_rate)
    nominal_diameter = st.number_input('Input the nominal Diameter for Dryer vessel (NW)', value=nominal_diameter)
    piping_weight = st.number_input('Assumed Total weight along pipings (kg)', value=piping_weight)

    # Calculate total power consumption
    total_power = calculate_power_consumption(flow_rate, nominal_diameter, piping_weight)
    st.write(f'Total Power Consumption: {total_power:.2f} kW')

    # Example equipment power consumption (adjust as needed)
    equipment_power = {
        'Electrical Heater': total_power * 0.3,
        'Regenration Heater': total_power * 0.25,
        'Regenration Blower': total_power * 0.2,
        'Blower-process Gas': total_power * 0.15,
        'Utilities': total_power * 0.1
    }

    # Display bar graph of equipment power consumption
    fig, ax = plt.subplots()
    ax.bar(equipment_power.keys(), equipment_power.values())
    ax.set_xlabel('Equipment')
    ax.set_ylabel('Power Consumption (kW)')
    ax.set_title('Power Consumption by Equipment')
    st.pyplot(fig)
else:
    st.write("Please upload an Excel file to proceed.")
