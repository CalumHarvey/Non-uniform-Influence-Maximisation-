
# %%
import matplotlib.pyplot as plt
import seaborn

# Random GitHub Linear Threshold

random = [0, 55, 131, 190, 243, 400, 462, 489, 550, 676, 755]
degree = [0, 5739, 7966, 9615, 37657, 37657, 37657, 37657, 37657, 37657, 37657]
Sdiscount = [0, 5739, 7924, 9669, 37657, 37657, 37657, 37657, 37657, 37657, 37657]
Ddiscount = [0, 5741, 7874, 9625, 11475, 37657, 37657, 37657, 37657, 37657, 37657]
# avgcost = [0, 61, 122, 185, 248, 310, 369, 427, 487, 543, 600]
# Hcost = [0, 398, 511, 580, 662, 805, 859, 938, 1007, 1054, 1110]
Lcost = [0, 659, 1081, 1479, 1815, 2183, 2503, 2834, 3155, 3461, 3769]
PICR = [0, 5904, 7186, 8073, 8843, 9428, 10113, 10586, 11294, 11664, 11978]
PICRnp = [0, 6221, 8747, 11070, 37657, 37657, 37657, 37657, 37657, 37657, 37657]

# x = [250, 500, 750, 100, 1250, 1500, 1750, 2000, 2250, 2500]

heuristics = ["Random", "Degree", "Single Discount", "Degree Discount", "Lowest Cost", "PICR", "PICRnp"]
data = [random, degree, Sdiscount, Ddiscount, Lcost, PICR, PICRnp]

yAxis = []
for x in range(len(data[0])):
    yAxis.append((50*5)*x)
print(yAxis)

for x in range(len(data)):
    plt.plot(yAxis, data[x], label=heuristics[x])
    
plt.legend()

plt.xlabel("Budget")
plt.ylabel("Influence Spread")

plt.show()
# %%

# %%

import matplotlib.pyplot as plt
import seaborn

# Degree Amazon Weighted Cascade

random = [0, 268, 493, 918, 969, 1245, 1546, 1794, 2062, 2366, 2606]
degree = [0, 21, 36, 36, 30, 43, 60, 66, 82, 84, 107]
Sdiscount = [0, 16, 29, 43, 50, 50, 86, 69, 96, 98, 94]
Ddiscount = []
avgcost = [0, 274, 547, 807, 1053, 1319, 1628, 1801, 2045, 2401, 2644]
Hcost = [0, 20, 26, 23, 30, 42, 78, 66, 71, 108, 122]
Lcost = [0, 1772, 3392, 4962, 6450, 7811, 9401, 10733, 11960, 13698, 14651]
PICR = []
PICRnp = [0, 370, 825, 1261, 1867, 2168, 2622, 3089, 3363, 3748, 4256]

# ["Random", "Degree", "Single Discount", "Degree Discount", "Average Cost", "Highest Cost", "Lowest Cost", "PICR", "PICR without prob"]
# [random, degree, Sdiscount, Ddiscount, avgcost, Hcost, Lcost, PICR, PICRnp]

heuristics = ["Random", "Degree", "Single Discount", "Average Cost", "Highest Cost", "Lowest Cost", "PICR without prob"]
data = [random, degree, Sdiscount, avgcost, Hcost, Lcost, PICRnp]

yAxis = []
for x in range(len(data[0])):
    yAxis.append((50*5)*x)
print(yAxis)

for x in range(len(data)):
    plt.plot(yAxis, data[x], label=heuristics[x])
    
plt.legend()

plt.xlabel("Budget")
plt.ylabel("Influence Spread")

plt.show()





# %%



import matplotlib.pyplot as plt
import seaborn

# Degree Github Linear Threshold

random = [0, 19, 59, 75, 119, 164, 152, 226, 169, 145, 237]
degree = [0, 5, 17, 29, 16, 31, 92, 148, 132, 137, 171]
Sdiscount = [0, 5, 17, 29, 16, 31, 92, 148, 132, 137, 171]
Ddiscount = [0, 5, 17, 29, 16, 31, 92, 148, 132, 137, 171]
avgcost = [0, 56, 117, 177, 233, 296, 354, 412, 467, 532, 596]
Hcost = [0, 5, 17, 29, 16, 31, 92, 148, 132, 137, 171]
Lcost = [0, 311, 616, 927, 1241, 1552, 1869, 2179, 2487, 2792, 3103]
PICR = [0, 311, 616, 927, 1241, 1552, 1869, 2179, 2487, 2792, 3103]
PICRnp = [0, 311, 616, 927, 1241, 1552, 1869, 2179, 2487, 2792, 3103]

# ["Random", "Degree", "Single Discount", "Degree Discount", "Average Cost", "Highest Cost", "Lowest Cost", "PICR", "PICR without prob"]
# [random, degree, Sdiscount, Ddiscount, avgcost, Hcost, Lcost, PICR, PICRnp]

heuristics = ["Random", "Degree", "Single Discount", "Degree Discount", "Average Cost", "Highest Cost", "Lowest Cost", "PICR", "PICR without prob"]
data = [random, degree, Sdiscount, Ddiscount, avgcost, Hcost, Lcost, PICR, PICRnp]

yAxis = []
for x in range(len(data[0])):
    yAxis.append((50*5)*x)
print(yAxis)

for x in range(len(data)):
    plt.plot(yAxis, data[x], label=heuristics[x])
    
plt.legend()

plt.xlabel("Budget")
plt.ylabel("Influence Spread")

plt.show()



# %%
