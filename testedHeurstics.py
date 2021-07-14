
def degreeCostPercentage(G, b, C):

    S = []
    costs = []
    TC = 0
    d = dict()

    for node in G.nodes:
        d[node] = G.degree[node] / C[node]

    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    for k,v in d.items():

        budgetLeft = b - TC

        if TC+v <= b:

            S.append(k)
            costs.append(v)
        
            TC += v
        
        if TC == b:
            break
    
    # print(costs)
    return S

"""
Random
[62, 102, 156, 193, 240, 286, 328, 387, 434, 473]
[210, 323, 406, 491, 586, 648, 721, 787, 828, 903]
[544, 635, 860, 1010, 1186, 1355, 1534, 1662, 1707, 1811]
Degree
[117, 212, 323, 421, 523, 702, 855, 985, 1128, 1264]
[100, 220, 318, 401, 501, 612, 718, 840, 932, 1073]
[112, 236, 342, 412, 508, 802, 979, 1176, 1401, 1635]
Page Rank
[67, 103, 157, 252, 312, 333, 404, 473, 565, 631]
[61, 160, 198, 238, 287, 362, 437, 501, 575, 627]
[64, 243, 272, 283, 332, 496, 625, 644, 770, 826]
"""


def degreeCostPercentage2(G, b, C, p=0.01):

    S = []
    costs = []
    degrees = []
    TC = 0
    d = dict()
    dd = dict()
    t = dict()

    for node in G.nodes:
        t[node] = 0
        d[node] = G.degree[node]
        dd[node] = G.degree[node] / C[node]

    while True:

        oldSeedSet = S.copy()

        dd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in dd.items():

            if k in S:
                continue

            nodeCost = C[k]
            budgetLeft = b - TC

            if TC+nodeCost <= b:

                TC += nodeCost

                S.append(k)

                costs.append(v)

                for neighbour in G.neighbors(k):
                    if neighbour not in S:
                        t[neighbour] += 1
                        dd[neighbour] = 1+(d[neighbour]-t[neighbour])*p / C[neighbour]
                break
        # return seedSet

        if TC == b or oldSeedSet == S:
            # print(costs)
            return S

"""
Random
[307, 577, 775, 1005, 1202, 1372, 1537, 1706, 1889, 2063]
[688, 981, 1194, 1421, 1575, 1756, 1915, 2050, 2180, 2314]
[1514, 1991, 2375, 2735, 3113, 3315, 3552, 3762, 4041, 4190]
Degree
[133, 314, 377, 468, 517, 608, 657, 768, 816, 924]
[64, 153, 186, 234, 262, 308, 336, 386, 428, 482]
[139, 329, 499, 623, 674, 910, 1046, 1143, 1272, 1390]
Page Rank
[36, 75, 112, 150, 189, 228, 273, 311, 350, 391]
[160, 277, 356, 444, 521, 575, 625, 690, 740, 789]
[321, 592, 715, 696, 838, 907, 985, 1058, 1160, 1208]
"""