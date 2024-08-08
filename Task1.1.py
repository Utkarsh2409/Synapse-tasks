#The combinations() function from the itertools module is a tool for generating all possible combinations of a given length from a specified iterable. 

from itertools import combinations

Kevin={"Hasley", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}

Stuart={"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}

Bob={"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacey", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}

Edith={"Metallica",  "Billie Elish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

djs= {"Kev":Kevin, "Stu":Stuart, "Bo": Bob, "Edi": Edith}

def overlapping(dj1,dj2):
    common_artists=dj1.intersection(dj2)
    overlap_dj1=len(common_artists)/len(dj1)
    overlap_dj2=len(common_artists)/len(dj2)
    return overlap_dj1, overlap_dj2

pairs=[]
for dj1, dj2 in combinations(djs.keys(), 2):
    overlap_dj1, overlap_dj2=overlapping(djs[dj1], djs[dj2])
    if overlap_dj1>=0.3 and overlap_dj2>=0.3:
        avg_overlap=(overlap_dj1+overlap_dj2)/2
        pairs.append(((dj1,dj2), avg_overlap))

pairs.sort(key=lambda x: x[1], reverse=True)

for pair, overlap in pairs:
    print(f"Pair: {pair}, Overlap: {overlap*100:.2f}%")