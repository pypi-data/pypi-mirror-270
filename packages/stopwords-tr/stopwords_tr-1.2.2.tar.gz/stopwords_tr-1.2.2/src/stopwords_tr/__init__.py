
txt=open('turkish.txt', 'r')
def stopwords():
    stopwords=[]
    for i in txt:
        i=i[0:-1]
        stopwords.append(i)
    return stopwords
