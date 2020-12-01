import matplotlib.pyplot as plt
import re
import json


def main():
    unidade = 1
    x = [unidade, 0, 0, -unidade, 0]
    y = [0, unidade, -unidade, 0, 0]
    cores = ["#fa1e28", "#fff032", "#1ee63c", "#003153", "#fc0fc0"]
    fp = open("log.txt", "r")

    a = " "
    area = [0, 0, 0, 0, 0]
    while(a != ""):
        a = fp.readline()
        a = re.sub("[^A-Z]", "", a)
        if(a == "A"):
            area[1] = area[1]+1
        if(a == "B"):
            area[0] = area[0]+1
        if(a == "C"):
            area[3] = area[3]+1
        if(a == "D"):
            area[2] = area[2]+1
        if(a == "E"):
            area[4] = area[4]+1

    s = list(map(lambda x: x*10, area))
    plt.scatter(x, y, s=s, c=cores, alpha=0.8)
    plt.savefig('Dashboard/img/graph.png', format='png')
    plt.show()

    data = {
        "up": str(area[0]),
        "left": str(area[3]),
        "right": str(area[1]),
        "down": str(area[2]),
        "select": str(area[4])
    }

    print(data)
    with open("count.json", "w") as json_file:
        json.dump(data, json_file)


main()
