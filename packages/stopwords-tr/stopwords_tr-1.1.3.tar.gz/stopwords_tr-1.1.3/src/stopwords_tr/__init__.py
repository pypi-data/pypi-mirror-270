def stopwords():
    txt= open('stopwords_tr/turkish.txt', 'r')
    stopwords=[]
    for i in txt:
        i=i[0:-1]
        stopwords.append(i)
    return stopwords
