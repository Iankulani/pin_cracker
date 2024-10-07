# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:50:02 2024

@author: IAN CARTER KULANI
"""

import time

# Define the correct PIN (you can change this to any 4-digit PIN for testing)
CORRECT_PIN = "3456"  # Example PIN to crack

# Define the path to the PIN file
PIN_FILE = 'pin.txt'

def load_pins(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def try_pin(pin):
    # Simulate the process of trying a PIN (e.g., connecting to a server or checking a local condition)
    return pin == CORRECT_PIN

def brute_force_pins(pins):
    for pin in pins:
        print(f"Trying PIN: {pin}")
        if try_pin(pin):
            print(f"Found the correct PIN: {pin}")
            return pin
        time.sleep(0.1)  # Simulate a delay to avoid rapid-fire attempts
    print("PIN not found.")
    return None

def main():
    # Load the PINs from the file
    pins = load_pins(PIN_FILE)
    
    # Perform the brute-force attack
    brute_force_pins(pins)

if __name__ == "__main__":
    main()
