# 7.1
year_lists = [2001, 2002, 2003, 2004, 2005]

# 7.2
print(year_lists[2])

# 7.3
year_lists.sort()
print(year_lists[-1])

# 7.4
things = ["mozzarella", "cinderella", "salmonella"]

# 7.8
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)

# 7.9
surprise[-1] = surprise[-1].lower()
print(surprise)
surprise[-1] = surprise[-1][-1::-1].capitalize()
print(surprise)

# 7.10
list = [n for n in range(1, 10) if n % 2 == 0]
print(list)

# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
    ]
start2 = "Someone better"
for i in (0, len(rhymes)-1):
    for s1 in start1:
        print(s1.capitalize(), end='! ')
    print(rhymes[i][0].capitalize() + "!")
    print(f"{start2} {rhymes[i][1]}.")