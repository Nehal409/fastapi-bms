import pandas as pd

def calculate_soc(battery_data_file):
    # Battery parameters
    Q = 3.5  # Battery capacity in mAh
    Vmax = 4.2 
    Vmin = 3.0
    dt = 60  # Time interval in seconds (1 minute)

    battery_data = pd.read_csv(battery_data_file, parse_dates=["Timestamp"])

    # Calculate initial SoC using voltage-based method (OCV)
    initial_V = battery_data.iloc[0]["Voltage(V)"]
    initial_SoC_OCV = (initial_V - Vmin) / (Vmax - Vmin) * 100

    # Initialize lists to store results
    SoC_CCM_list = []
    SoC_OCV_list = []
    Combined_SoC_list = []

    # Iterate through battery readings
    SoC_CCM = initial_SoC_OCV  # Initialize Coulomb counting SoC with initial OCV estimate
    for i, reading in battery_data.iterrows():
        # Battery current in A (negative for discharge, positive for charge)
        I = reading["Current(A)"]

        # Calculate SoC using voltage-based method (OCV)
        V = reading["Voltage(V)"]
        SoC_OCV = (V - Vmin) / (Vmax - Vmin) * 100  # OCV method
        
        # Calculate SoC using Coulomb counting method
        dQ = I * dt  # Change in charge/discharge
        SoC_CCM = SoC_CCM + (dQ / Q)  # Coulomb counting method
        
        ''' Combine methods using weighted average (Use fuzzy logic in project)'''
        alpha = 0.5
        Combined_SoC = alpha * SoC_CCM + (1 - alpha) * SoC_OCV
        
        # Append results to lists
        SoC_CCM_list.append(SoC_CCM)
        SoC_OCV_list.append(SoC_OCV)
        Combined_SoC_list.append(Combined_SoC)

    # Create a list of  dictionaries with results
    results = []
    for i, reading in enumerate(battery_data["Timestamp"]):
        result = {
            "Timestamp": str(reading),
            "Coulomb Counting SoC": SoC_CCM_list[i],
            "Voltage-Based SoC (OCV)": SoC_OCV_list[i],
            "Combined SoC": Combined_SoC_list[i]
        }
        results.append(result)

    return results

