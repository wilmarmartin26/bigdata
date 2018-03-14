import glob
import os
import sys
 

def main(args):
    
    path_stopwords = 'stopwords/'
    stopwords = []
    for filename in glob.glob(os.path.join(path_stopwords, '*.txt')):
        file = open(filename, encoding="utf8")  
        print(str(filename))
        stopwords = stopwords + (file.read().split())        

    file = open("AnalisisGenerados/stopwordsGen.txt","w", encoding="utf8")    
    dic = {}
    for sw in stopwords:
        lowerCase = sw.lower()
        if lowerCase is not dic.keys():
            dic[lowerCase] = sw

    for out in dic:
        file.write(out + '\n')
    
    file.close() 

# metodo main
if __name__ == '__main__':
    main(sys.argv)
