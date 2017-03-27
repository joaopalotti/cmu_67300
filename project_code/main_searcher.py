
# Load models from one or many files, as you prefer...
from search_models import DohaQatarTFSearchModel # , VectorSpaceModel, BooleanSearchModel

# You can also write them in separate files and load you models with:
#
# from vector_model import VectorSpaceModel
# from lm_model import LanguageModel
#

####
#    IMPORTANT: YOU SHOULD USE THE SAME INDEXING PROCEDURE USED FOR INDEXING THE COLLECTION!
####

# For example, if you have used porter stemmer, you have to used it here again.
from nltk import stem
snowball = stem.SnowballStemmer('english')

# The stopwords removal is up to you. What happens if you had removed stopwords before and decided not to remove them now?
stopwords = []
with open("stopwords.txt") as fstop:
    stopwords = [sw.strip() for sw in fstop.readlines()]

# Load list of queries in memory
query_list = []
with open("queries.txt") as qfile:
    for line in qfile.readlines():
        qid, qstr = line.strip().split(",")
        query_list.append((int(qid), qstr))

# Now my query_list looks like a list of pairs: [(1,"beirut"), (2,"float precision error"), (3, "post rock bands")]


# load my favorite model
model = DohaQatarTFSearchModel(index_file="./iindex.map", document_mapping_file="./docs.map")

# run each one of the queries...
for query_id, query_str in query_list:
    model.search(query_id, query_str, stopwords, snowball.stem)


# """
#  Vector space model:
# """
#
#vsm = VectorSpaceModel(index_file="./iindex.map", document_mapping_file="./docs.map")
#vsm.search(query)
#
# """
# You might want to implement other methods as well...
# ....that is it, folks!
# """
#
