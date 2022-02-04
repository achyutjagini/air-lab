import nltk
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
stop_words=set(stopwords.words('english'))
#using stemming-TEXT NORMALIZATION
file='train.csv'
filer=open(file,"r",encoding="utf-8")
text=filer.read()
text=text.replace("\n"," ")
#tokenizing words
word_tokens = word_tokenize(text)

filtered_sentence = []
symbols=[':','/',',','"','(',')','@','?',';','//','#','!','&','$','%','*','...','.','..','-','[',']','{','}']
for w in word_tokens:
    if w not in stop_words and w not in symbols:
        filtered_sentence.append(w)
print("The text after stemming" )
Stem_words = []
ps = PorterStemmer()


for w in filtered_sentence:
    rootWord = ps.stem(w)
    Stem_words.append(rootWord)
print(filtered_sentence)
print(Stem_words)


lemma_word = []


wordnet_lemmatizer = WordNetLemmatizer()
for w in filtered_sentence:
    word1 = wordnet_lemmatizer.lemmatize(w, pos = "n")
    word2 = wordnet_lemmatizer.lemmatize(word1, pos = "v")
    word3 = wordnet_lemmatizer.lemmatize(word2, pos = ("a"))
    lemma_word.append(word3)
print("The text after lemmatization")
print(lemma_word)

