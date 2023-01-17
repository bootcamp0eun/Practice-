# 8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)

# 8.2
print(e2f["walrus"])

# 8.3
print("\n# 8.4")
temp = list(e2f.items())
print(temp)
print(temp[1])
f2e = {temp[i][1]: temp[i][0] for i in range(0,len(temp))}
print(f2e)

# 8.4
print("\n# 8.4")
value = {i for i in e2f if e2f[i] == "chien"}
print(value)

# 8.5
print("\n# 8.5")
print(e2f.keys())

# 8.6
life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
        'plants': {},
        'other': {}
        }

# 8.7
print("\n# 8.7")
print(life.keys())

# 8.8
print("\n# 8.8")
print(life['animals'].keys())

# 8.9
print("\n# 8.9")
print(life['animals']['cats'])

# 8.10
print("\n# 8.10")
squares = {k: k**2 for k in range(10)}
print(squares)