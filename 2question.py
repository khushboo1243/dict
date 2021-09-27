
a_dictionary = {"one": 1, "two" : 2, "three": 3}


desired_key = "two"

for key in a_dictionary.keys():

  if key == desired_key:

    del a_dictionary[key]

    break


print(a_dictionary)

# Output

# {'one': 1, 'three': 3}    

