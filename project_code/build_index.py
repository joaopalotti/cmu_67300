import os
import glob
from utilities import tokenize, open_file

class IIndex:

    def __init__(self, files):
        """
            Input Parameter:

            * files: the location of the collection in your computer.

            This will create a internal variable called 'files' (accessiable with self.files),
            which will contain all the files from the collection:
            ["<...path...>/simplecollection/simple000001.txt", "<...path...>/simplecollection/simple0000002.txt", ...]

        """
        self.files = glob.iglob(os.path.join(files, "*"))

    def create(self, stopword_list=[], stemming_func=None):
        """
            Input Parameters:

            * stopword_list: a list of words to be removed from the collection. ["the","a","an","of"...]
            * stemming_func: a function for stemming.

            Output:
            * the following two files in disk.

            (1) docs.map:

            This file will contain a large number of lines with mapping of document names and their ids.
            Every line contains two numbers separated by a single comma: the document name and its internal id.

            Example:
            -------

            simple000001.txt,1
            simple001234.txt,2
            simple987654.txt,3
            ...
            ...


            (2) iindex.map:

            By now, this file contains a large number of lines, one for every single token found in the text and their
            occurences in the files of this collection.

            The output are posting lists for the collection that look like this:

            wordA,doc1:freq1,doc2:freq2,doc3:freq3....
            wordB,doc3:freq3,doc5:freq5,doc6:freq6....

        """
        stopwords = set(stopword_list)

        docid = 0
        doc_mapping = {}

        iindex = {}

        for f in self.files:
            text = open_file(f)
            tokens = tokenize(text, stopwords, stemming_func)
            doc_mapping[os.path.basename(f)] = docid

            print("Processing (%d) - %d Tokens - %s" % (docid, len(tokens), f))
            for token in tokens:
                if token not in iindex:
                    iindex[token] = {}

                if docid not in iindex[token]:
                    iindex[token][docid] = 0

                iindex[token][docid] += 1
            docid += 1

        # Save to document mappings to disk:
        with open("docs.map","w") as fout:
            for docname,docid in doc_mapping.items():
                fout.write("%s,%d\n" % (docname, docid))

        # Save iindex to disk:
        with open("iindex.map","w") as fout:
            for token, doc_freq in iindex.items():
                fout.write("%s" % (token))

                for docid,freq in doc_freq.items():
                    fout.write(",%s:%d" % (docid,freq))
                fout.write("\n")

