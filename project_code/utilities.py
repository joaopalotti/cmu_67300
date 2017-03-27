import re

def open_file(fname):
    """
        Given the path to a file called 'fname', this function will open this file
        and return its text.
    """
    content = ""
    with open(fname) as f:
        # extract content from text
        content = f.read()
    return content

def tokenize(text, stopwords = set([]), stemming_func = None):
    """
        Given a text, an optional list of tokens to filter and an optional stemming function,
        this function applies the defined pre-processing in the input text, returning its tokens.

        Usage example:

        >> from nltk.stem.porter import PorterStemmer
        >> stemmer = PorterStemmer()
        >> st = stemmer.stem

        >> tokenize("This is my simple text.", ["a", "the", "of"], st)

    """
    tokens = []

    # replace punctuation for white space
    text = re.sub("\W", " ", text)

    # remove double white spaces:
    text = " ".join(text.split())

    # split text to obtain tokens:
    tokens = [t.lower() for t in text.split()]

    # Remove stopwords if needed
    if len(stopwords) > 0:
        tokens = [t for t in tokens if t not in stopwords]

    # Apply some stemming if desired
    if stemming_func is not None:
        tokens = [stemming_func(t) for t in tokens]

    return tokens

def load_index(index_file, docmap_file):
    """
    Loads the index into memory
    """
    #return iindex, docmap
    pass

