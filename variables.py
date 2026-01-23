# Examples of variables and different ways to print them

name = "Lin"
grade = 13
country = "USA"
study = "DA"

# Print variables individually
print(name)
print(country)
print(grade)
print(study)

print("______________")

# Print using commas
print("My name is", name, "I live in", country, "I am in", grade, "and I study", study)

# Print using f-string
print(f"My name is {name}, I live in {country}, I am in {grade}, and I study {study}")

# Print using concatenation (convert numbers to string)
print("My name is " + name + " I live in " + country + " I am in " + str(grade) + " and I study " + study)
