import mwparserfromhell
from xml.etree import cElementTree as ET
import sys
from unidecode import unidecode


"""
Run as:
    python parser.py simplewiki-20170301-pages-articles-multistream.xml
"""

wfilename = sys.argv[1]
wiki = ET.parse(wfilename)

doctemplate = "swcollection/simple%06d.txt"
docid = 0

for page in wiki.findall("page"):
    revision = page.find("revision")
    title = page.findtext("title")

    if title.startswith("Wikipedia:") or title.startswith("Template:") or\
        title.startswith("Category:") or title.startswith("MediaWiki:"):
        continue

    if revision and title:
        docid += 1
        text = revision.findtext("text")
        try:
            parsed = mwparserfromhell.parse(text)
        except:
            continue

        docname = doctemplate % (docid)

        print "Creating %s -- %s" % (docname, title)
        with open(docname, "w") as fout:
            text = unidecode(title).encode("ascii","ignore") + "\n\n"
            text += ' '.join([sent.value for sent in parsed.filter_text()])

            fout.write(unidecode(text).encode("ascii","ignore"))


