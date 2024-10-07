# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:54:47 2024

@author: IAN CARTER KULANI
"""

# Generate all 4-digit PINs and save them to pin.txt
with open('pin.txt', 'w') as file:
    for pin in range(1000000):
        file.write(f"{pin:04}\n")  
# Format PIN with leading zeros
