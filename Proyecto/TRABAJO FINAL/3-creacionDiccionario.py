import sys
import json
#import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize

      
def main(args):
    stopwords = []    
    file_stopwords = open("AnalisisGenerados/stopwordsGen.txt", "r", errors="replace")        
    stopwords = file_stopwords.read().split() 
   
    documents = {}    
    file_documents = open("documents/documentsGen.txt", "r")        
    documents = json.JSONDecoder().decode(file_documents.read())     
    
    
    newDoc = {}
    listword = []
    for key,doc in documents.items():
        doc_listwords = []
        for word in word_tokenize(doc): #split
           if word not in stopwords:              
              doc_listwords.append(word)
              if word not in listword:
                  listword.append(word)                
        newDoc[key] = doc_listwords   
        
    file = open("AnalisisGenerados/documentoMatWS.txt","w")        
    file.write(json.JSONEncoder().encode(newDoc))
    file.close() 
    print("archivo documentoMatWS creado")       

    file = open("AnalisisGenerados/wordsGen.txt","w")        
    file.write(json.JSONEncoder().encode(listword))
    file.close() 
    print("archivo wordsGen creado")
        
    
# metodo main
if __name__ == '__main__':
    main(sys.argv)