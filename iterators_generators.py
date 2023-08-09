class CustomCollection:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return iter(self.data)
    
    def to_list(self):
        return list(self.data)
    
    def to_set(self):
        return set(self.data)
    
custom_collection = CustomCollection([1, 2, 3])

#add ability to be used in a for in loop

for item in custom_collection:
    print(item)

#add ability to be used in a list comprehension

nums_squared = [x ** 2 for x in custom_collection]
print(nums_squared)

#add ability to convert to a list or other collection type

converted_list = custom_collection.to_list()
print(converted_list)