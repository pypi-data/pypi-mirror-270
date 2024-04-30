def stopwords():
    txt= open('data/turkish.txt', 'r')
    stopwords=[]
    for i in txt:
        i=i[0:-1]
        stopwords.append(i)
    return stopwords
