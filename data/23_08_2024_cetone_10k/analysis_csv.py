import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
filename = '10k_run.csv'
data = pd.read_csv(filename)

PLOY_Y = "HR"

# Filter data for the two labels
data_without = data[data['Label'] == 'without']
data_cetone = data[data['Label'] == 'ketone']

# Plot the data
plt.figure(figsize=(14, 8))

# Plot for 'without' label in blue
plt.plot(data_without['Dist'].values, data_without[PLOY_Y], color='blue', label='Without')
# Add labels for 'without'
for i, row in data_without.iterrows():
    t = plt.text(row['Dist'], row[PLOY_Y], str(row['result']), color='black', size=14)
    t.set_bbox(dict(facecolor='blue', alpha=0.8, edgecolor='blue'))

# Plot for 'cetone' label in red
plt.plot(data_cetone['Dist'].values, data_cetone[PLOY_Y], color='red', label='ketone')
gain = ((data_cetone[PLOY_Y].values - data_without[PLOY_Y].values) / data_without[PLOY_Y].values) * 100
counter = 0
# Add labels for 'cetone'
for i, row in data_cetone.iterrows():
    t = plt.text(row['Dist'],
                 row[PLOY_Y],
                 str(row['result']) + " " + str(round(gain[counter], 2)) + "%",
                 color='black',
                 size=14)
    t.set_bbox(dict(facecolor='red', alpha=0.8, edgecolor='red'))
    counter += 1

# Customizing the X-axis to display only specific values
plt.xticks(data_cetone['Dist'].values)
plt.gca().invert_xaxis()

# Adding labels and title
plt.xlabel('Dist')
plt.ylabel(PLOY_Y)
plt.title(f'With and without ketone, gain: {abs(gain.mean().round(2))}%')
plt.legend()

# Show the plot
plt.show()
