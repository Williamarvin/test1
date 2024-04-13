my_dict = {"mango":{200:100},
        "stawberry":100,
        "durian":300,
        "coconut":250}

dict1 = dict()
keys = my_dict.keys()
keys = list(keys)
#
# group by
#

# get
print(my_dict.get("mango"))

for i in range(len(my_dict)):  
    dict1[(keys[i], i)] = my_dict.get(keys[i])
    
print(dict1)