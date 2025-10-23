def celsius_para_fahrenheit(celsius):
    # Fórmula: (C * 9/5) + 32
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def fahrenheit_para_celsius(fahrenheit):
    # Fórmula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius
