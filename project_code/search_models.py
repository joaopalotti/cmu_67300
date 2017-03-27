from utilities import tokenize, load_index

class SearchModel:

    def __init__(self, index_file, document_mapping_file):
        self.index, self.docmap = load_index(index_file, document_mapping_file)

    def _get_entry(self, keyword):

        if keyword not in self.index: # Hey this keyword was not found!
            return []

        # TODO: improve this fuction...how about loading the idf here
        # TODO: how about calculating the LM probabilities here as well?

        postings = []

        for doc, freq in self.index[keyword].iteritems():
            postings.append((doc,freq))

        return postings

    def __prepare_query(self, query, stopwords=[], stemming_func=None):
        """
            This is a private method to preprocess a query.
            This should return a list of tokens after the query is processed.
        """
        pass

    def search(self, query_id, query_str):
        """
            This is the main public method of this class and its subclasses.
            Given a string query, it will print to the screen a ranked list of documents that
            answer the given query.
        """
        pass

# We will use SearchModel class as the base class.
class DohaQatarTFSearchModel(SearchModel):
    """
        This is a particular search model that I am making up to serve as an example.
        Here, I do not care for the query you are providing, I change your query to "Doha Qatar".

        Then I apply a "TF model", i.e. I score documents based only on the TF of query terms that
        appear in a document:

        score(d, q) = For all token X_d=1,q=1  sum tf_x

    """

    def __prepare_query(self, query, stopwords=[], stemming_func=None):
        return tokenize(query, stopwords, stemming_func)

    def search(self, query_id, query_str, stopwords, stemming_func):

        # I do not care about what you are searching for, I just care for the query "Doha Qatar"
        #query_str = "Doha Qatar"

        query_tokens = self.__prepare_query(query_str, stopwords, stemming_func)

        # I need a structure to keep the scores for each document
        # Example:
        # doc1 -> score: 0.00002
        # doc2 -> score: 0.003
        # ...
        doc_scores = {}

        for token in query_tokens:
            postings = self._get_entry(token)

            for (doc, freq) in postings:

                # check to avoid KeyError
                if doc not in doc_scores:
                    doc_scores[doc] = 0.0

                # the score of a document is just the sum of TFs
                # for the query tokens in the document
                doc_scores[doc] += freq

        # After this loop, doc_scores is populated with the sum of frequencies of each term in the
        # documents that they appeared.
        # This is a minor improvement in the Boolean OR model.

        # We need to sort the doc_scores structure to obtain the final ranked list.
        result_list = sorted(doc_scores.items(), key=lambda x:(x[1], x[0]), reverse=True)

        # This print below is just for debug and educational purpose.
        # Uncomment it to see a more friendly output.
        #for docid, score in result_list:
        #    print "Document %s, score: %.3f" % (self.docmap[docid], score)

        # Now, the next print is the official one that you should use:
        docRank = 1
        for docid, score in result_list[:100]: # only the top 100 documents...
            # TREC Format: <topicId, Q0, docName, docRank, score, runName>
            print "%d\tQ0\t%s\t%d\t%.2f\t%s" % (query_id, self.docmap[docid], docRank, score, "joaoRun1")
            docRank += 1

