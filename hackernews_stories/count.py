#importing  another file to read the dataframe
import read
df = read.load_data()
# s is the long string of conected headlines
s = " ".join(map(str,df["headline"].values))
#lowercase the words in the long string s
s = s.lower()
#splitting the words by space and put them in a list
word_list = s.split(" ")
#importing the Counter class 
from collections import Counter
# c is a counter dictionary, "most_common" is a method to find count of most used words
c = Counter(word_list).most_common(100)
print(c)
    
    