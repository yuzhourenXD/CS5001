
def rankViewer(viewerData, adData):
    viewrsRanking = []
    for i in range(100):
        list = []
        for j in range(100):
            point = 0
            for k in range(1, 4):
                if adData[i][k] == viewerData[j][k]: point += 1
            list.append(point)
        viewrsRanking.append(list)
    return viewrsRanking

def rankads(viewerData, adData):
    adRanking = []
    for i in range(1, 101):
        list = []
        for j in range(1, 101):
            point = 0
            for k in range(1, 4):
                if viewerData[i][k] == adData[j][k]: point += 1
            list.append(point)
        adRanking.append(list)
    return adRanking