import os
import pickle
import shutil
from tqdm import tqdm
from whoosh import index
from I_fetch_pubmed import medline_folder
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer


# Schema - Taken straight from the docs, removed "tags"
schema = Schema(from_addr=ID(stored=True),
                to_addr=ID(stored=True),
                subject=TEXT(stored=True),
                body=TEXT(analyzer=StemmingAnalyzer()),)

# Index
index_dir = "pubmed_index"


def get_index():
    # Create your index here
    return

if __name__ == "__main__":
    get_index()

