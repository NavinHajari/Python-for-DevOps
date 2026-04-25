# String formatting
name = input("What is your name:")
city = input("Enter your city name:")
intro = f"Hello Dost, this is {name} from {city}"
other_name = input("Enter the other name: ")
print(intro.replace("Dost",other_name))
print(dir(city))
