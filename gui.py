import tkinter as tk
from utils import celsius_to_fahrenheit, celsius_to_kelvin

def convert_temp():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        result_label.config(
            text=f"{celsius}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K"
        )
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Input field
entry_label = tk.Label(root, text="Enter temperature in Celsius:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.pack()

# Result display
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
