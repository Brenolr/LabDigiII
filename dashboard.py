import matplotlib.pyplot as plt
import re
def main():
    unidade=1
    x=[unidade,0,0,-unidade]
    y=[0,unidade,-unidade,0]
    cores=["#fa1e28","#fff032","#1ee63c","#003153"]
    fp=open("log.txt","r")
    
    a=" "
    area=[0,0,0,0]
    while(a!=""):
        a=fp.readline()
        a=re.sub("[^A-Z]", "", a)
        if(a=="A"):
            area[1]=area[1]+1
        if(a=="B"):
            area[0]=area[0]+1
        if(a=="C"):
            area[3]=area[3]+1
        if(a=="D"):
            area[2]=area[2]+1

    plt.scatter(x, y,s=area, c=cores, alpha=0.8)
    plt.show()

main()