dictA = {"Beefsteak": 20, "Campari": 100}
dictB = {"McIntosh": 5, "Fuji": 11, "Honeycrisp": 32}

dictComb = {
    "Beefsteak McIntosh": 25, "Beefsteak Fuji": 31, "Beefsteak Honeycrisp": 52,
    "Campari McIntosh": 105, "Campari Fuji": 111, "Campari Honeycrisp": 132
}
I tried something like this:

for (a, b) in zip(dictA, dictB):
     dictComb.update({" ".join([a, b]): sum([dictA[a], dictB[b]])})
Unfortunately, that gives:

dictComb = {"Beefsteak McIntosh": 25, "Campari Fuji": 111}
