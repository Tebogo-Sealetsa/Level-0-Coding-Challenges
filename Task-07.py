def convert_to_fahrenheit(celsius):
    temperature = (9/5)*celsius +32
    print(temperature)
    return temperature

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit -32)/(9/5)
    print(temperature)
    return temperature

convert_to_fahrenheit(20)
convert_to_celsius(68)
