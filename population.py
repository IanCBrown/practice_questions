births = 86400 // 7
deaths = 86400 // 13
immigrants = 86400 // 45
total_pop = 312032486

print("Year: 0")
print("Population: " + str(total_pop))
for i in range(1,6):
    print("Year: " + str(i))
    total_pop += (births * 365) - (deaths * 365) + (immigrants * 365)
    print("Projected population: " + str(total_pop))


    




