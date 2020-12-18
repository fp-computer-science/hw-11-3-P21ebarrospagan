# Author: EBP (AMDG) 12/17/20

last_initials = ["A", "B", "B", "D", "D", "G", "G", "J", "K", "L", "P", "S", "T", "T", "V", "W"]

rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan", "Phil", "Eman", "Alex", "Nicholas"], ["Christian", "Josh", "Matt", "Francesco"], ["Patrick", "Nico", "Trevayne"]]


for row in rows:
    for index, name in enumerate(row):
            row[index] = name + " " + last_initials[index] + "."
print(rows)