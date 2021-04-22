n, m = map(int, input().split())

chef = {}
nation = {}

for _ in range(n):
    name, country = input().split()
    nation[country] = 0
    chef[name] = [country, 0]


for _ in range(m):
    subj = input()
    chef[subj][1] += 1
    nation[chef[subj][0]] += 1

max_chef = ['zzzzz', 0]

for name, (country, votes) in chef.items():
    if votes > max_chef[1] or (votes == max_chef[1] and name < max_chef[0]):
        max_chef = [name, votes]

max_country = ['zzzzzz', 0]

for country, votes in nation.items():
    if votes > max_country[1] or (votes == max_country[1] and country < max_country[0]):
        max_country = [country, votes]

# print(chef, nation, sep='\n')
print(max_country[0], max_chef[0], sep='\n')