# 8.11
print("# 8.11")
odd_set = {i for i in range(10) if i % 2 != 0}
print(odd_set)

# 8.12
print("\n# 8.12")
for i in (n for n in range(10)):
    print(f"Got {i}")

# 8.13
print("\n# 8.13")
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
new = {k: v for k, v in zip(keys, values)}
new2 = dict(zip(keys, values))
print(new)
print(new2)

# 8.14
print("\n# 8.14")
titles = ['Creature of Habit', 'Crewel Fate']
plots = ["A nun turns into a mon ster", "A haunted yarn shop"]
movies = dict(zip(titles, plots))
print(movies)