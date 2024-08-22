import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
filename = 'your_file.csv'  # Replace with your actual file path
data = pd.read_csv(filename)

# Create a plot for each column
ax = data.plot(subplots=True, figsize=(10, 12), layout=(len(data.columns), 1), sharex=False)

# Set the title for each subplot
for i, col in enumerate(data.columns):
    ax[i].set_title(col)

# Show the plot
plt.tight_layout()
plt.show()
