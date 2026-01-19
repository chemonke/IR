import os
import pickle
import shutil
from tqdm import tqdm
from whoosh import index
from I_fetch_pubmed import medline_folder
from whoosh.fields import Schema, TEXT, ID

"""
Data structure:
    Dict[int, Tuple[str, str, List[str]]]

    key -> pmid
    value -> (title, abstract, MeSH)
"""

# Schema
schema = Schema(pmid=TEXT(stored=True),
                title=TEXT(stored=True),
                abstract=TEXT(stored=True),
                mesh=TEXT(stored=True))

# Index
indexdir = "pubmed_index"

def get_index(reset=True):
    if reset and os.path.exists(indexdir):
        shutil.rmtree(indexdir)

    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
        ix = index.create_in(indexdir, schema)
    else:
        ix = index.open_dir(indexdir)
    
    writer = ix.writer()

    for file in tqdm(os.listdir(medline_folder)):
        path = os.path.join(medline_folder, file)
        with open(path, "rb") as f:
            data = pickle.load(f)
        
        for pmid, value in data.items():
            title, abstract, mesh = value
            writer.add_document(pmid=pmid, title=title,abstract=abstract, mesh=mesh)
    
    writer.commit()

    return ix

if __name__ == "__main__":
    get_index()