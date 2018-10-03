    
# coding: utf-8



import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import PunktSentenceTokenizer

# sent1="The river bank was full of dead fishes."
# sent2="The workers at the industrial plant were overworked."

from nltk.corpus import stopwords
functionwords=set(stopwords.words('english'))


def lesk(word,context):
    synset=wn.synsets(word)
    bestsense=''
    max_Overlap=0
    for syns in synset:
    #     print(sent)
        overlap=Compute_Overlap(syns,context)
        if overlap>max_Overlap:
            max_Overlap=overlap
            bestsense=syns.definition()
    return bestsense,max_Overlap

def Compute_Overlap(syns,sent):
    gloss = PunktSentenceTokenizer().tokenize(syns.definition())
#     print(gloss)
    for u in gloss:
        gloss=set(nltk.word_tokenize(u))
    for i in syns.examples():
        print("example",i)
        s=set(nltk.word_tokenize(i))
        gloss=gloss.union(s)
        gloss = gloss.difference( functionwords )
    # print("Gloss:",gloss)
    if isinstance(sent, str):
        sentence = set(sent.split(" "))
    elif isinstance(sent, list):
        sentence = set(sent)
    elif isinstance(sent, set):
        pass
    else:
        print('yo')
    sentence=sentence.difference(functionwords)
    length=len( gloss.intersection(sentence) )
    define=syns.definition()
    print(syns)
    print("Definition:",define," Overlap:",length)
    return length


if __name__ == "__main__":
    sentence=input("Enter the sentence:")
    word=input("Enter the word to be Disambiguated")
    #sent="The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities."
    #word="Bank"
    Bestsense,max_Overlap=lesk(word,sentence)
    print("Final chosen sense")
    print(Bestsense," with a word overlap of ",max_Overlap," words.")


