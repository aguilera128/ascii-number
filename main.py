#!/usr/bin/python3

def Ascii(dato):

    if dato.isalpha():
        print(f"The ASCCI number of your input is: {ord(dato)}")
    else:
        print(f"The ASCII alphabet or your input is: {chr(int(dato))}")


dato = input("Enter ASCII number or letter to convert:")

Ascii(dato)