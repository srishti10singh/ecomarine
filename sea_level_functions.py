import pandas as pd
import matplotlib.pyplot as plt

def plot_sea_level(data):
    # Grouping by 'GMSL' and summing up the values
    ts = data.groupby(["GMSL"])["GMSL"].sum()

    # Converting the data to float
    ts = ts.astype('float')

    # Plotting
    plt.figure(figsize=(14,8))
    plt.title('Global Average Absolute Sea Level Change')
    plt.xlabel('Time')
    plt.ylabel('Sea Level Change')
    plt.plot(ts.index, ts.values)  # Assuming 'ts.index' contains the time information
    plt.show()
# Example usage:
# plot_sea_level(data)
