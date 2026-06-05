#creating dictionary
person = {
    "name" : "Rafik",
    "age" : 21,
    "city" : "Dhaka"
}

#access values
print(person["name"])
print(person["age"])


#add new keys
person["country"] = "Bangladesh"

print(person)


#update existing key
person["age"] = 22

print(person)


"""
del keys
Removes the key directly
❌ Does NOT return anything
❌ Will crash if key doesn’t exist
"""
del person["city"]

print(person)


"""pop key
Removes the key
✅ Returns the removed value
Safer option (can give default value)
"""
person.pop("age")

print(person)


#get() safe access
print(person.get("name"))
print(person.get("salary"))


#keys()
print(person.keys())


#values()
print(person.values())


#items()
print(person.items())


#Loop keys
for key in person:
    print(key)


#Loop values
for value in person.values():
    print(value)


#Loop key + value (MOST IMPORTANT)
for key, value in person.items():
    print(key, value)