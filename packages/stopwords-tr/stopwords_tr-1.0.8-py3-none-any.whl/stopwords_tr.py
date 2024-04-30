def stopwords():
    with open('turkish.txt', 'r') as txt:
        txt = txt.read()
    stopwords=[]
    for i in txt:
        i=i[0:-1]
        stopwords.append(i)
    return stopwords
