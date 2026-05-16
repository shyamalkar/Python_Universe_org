countries =  ["India", "USA", "Austrelia", "ireland", "Sri lanka", 
              "Iceland", "Cuba", "Iran", "Poland"]

# Count all the countries
#also print all these countries as a list
#["India", "Ireland", "Iceland", "Iran"]

counter = 0 
output = []

for country in countries:
    if country.startswith("I"):
        counter = counter + 1
        output.append(country)

print(counter)
print(output)