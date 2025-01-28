# script.py

from utils import celsius_to_fahrenheit, celsius_to_kelvin

def main():
    print("Temperature Converter")
    temp = float(input("Enter the temperature in Celsius: "))
    
    fahrenheit = celsius_to_fahrenheit(temp)
    kelvin = celsius_to_kelvin(temp)

    print(f"{temp}°C is equal to {fahrenheit}°F and {kelvin}K")

if __name__ == "__main__":
    main()
