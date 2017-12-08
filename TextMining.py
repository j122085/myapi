from collections import Counter
import math
class TextMining:
    
    '''You should [I] cutArticlelist for get TFIDF'''
    def __init__(self,cutArticlelist):
        self.cutArticlelist=cutArticlelist
    
    def getWordCountList(self,N=300):
        '''get all words(most appear limit 300)'''
        wordCountList=[Counter(pincut.split(" ")).most_common(N) for pincut in self.cutArticlelist]
        return wordCountList
    
#     def getWordSet(self,N=300):
#         wordCountlist=self.getWordCountList(N)
#         wordset=set()
#         for wordCount in wordCountlist:
#             wordset.update(dict(wordCount).keys())
#         print("共{}個字".format(len(wordset)))
#         return wordset

    def getTF(self,N=300):
        TFList=[]
        n=0
        for wordCount in self.getWordCountList(N):
            n+=1
            if n%1000==0:
                print(n)
            TF={}
            allwords=sum(dict(wordCount).values())
            for wordkv in wordCount:
                TF[wordkv[0]]=(wordkv[1]/allwords)
            TFList.append(TF)
        return TFList
    
    def getWordAppear(self,N=300):
        k=0
        wordappear={}
        for wordCount in self.getWordCountList(N):
            k+=1
            if k%3000==0:
                print(k)
            for word in dict(wordCount).keys():
                if word in wordappear:
                    wordappear[word]+=1
                else:
                    wordappear[word]=1
        return wordappear
    
    def getIDF(self,N=300):
        wordappear=self.getWordAppear(N)
        artN=len(self.cutArticlelist)
        IDFDict={word:math.log(artN/wordappear[word],10) for word in wordappear}
        return IDFDict
    
    def getTFIDF(self,N=300):
        TFList=self.getTF(N)
        IDFdict=self.getIDF(N)
        TFIDFList=[]
        for artTFdict in TFList:
            artTFIDF=Counter()
            for artword in artTFdict:
                artTFIDF[artword]=artTFdict[artword]*IDFdict[artword]
            TFIDFList.append(artTFIDF)
        return TFIDFList
    
    
    
    def __str__(self):
        return "TextMining({})".format(self.cutArticlelist)