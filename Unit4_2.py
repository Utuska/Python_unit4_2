ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

new = []

for i in ids.values():
    for j in i:
        if j not in new:
            new.append(j)
print(new)