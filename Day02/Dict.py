# dictionary
env = ["dev", "prd", "stg", "test"]

device_info = {
    "name" : "Apple MacBook Pro",
    "RAM"  : "16 GB",
    "CPU"  : 8,
    "isNEW": False
}

# print(device_info.get("name"))

# device_info.update({"environments":env})

print(device_info)

# print(type(device_info)) # prints the type of data structure 

device_ids = {1,2,3,3,4,4,5}

# print(len(device_ids)) # doesn't print the count of duplicates

new_device_ids = {2,3,4,6,7,8,9}


print(device_ids.union(new_device_ids)) # prints both the sets combined without duplicates

print(device_ids.intersection(new_device_ids)) # prints only the common values from both sets

# tuples

weekdays = ("Sunday", "Monday")

print(weekdays)

