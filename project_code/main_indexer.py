from build_index import IIndex

"""
Some examples of stemmers
"""
from nltk import stem
porter = stem.PorterStemmer()

# Another one:
snowball = stem.SnowballStemmer("english")

# Or you can use another library if you want to:
# from stemming import lovins
# lovins.stem("arabic")

"""
An example of stopword
"""
stopwords = []
with open("stopwords.txt") as fstop:
    stopwords = [sw.strip() for sw in fstop.readlines()]

# you will need to adjust this parameter to map the location of this collection in your computer
myindex = IIndex("../project_collection/swcollection")
myindex.create(stopword_list=stopwords, stemming_func=porter.stem)


