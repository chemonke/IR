import pickle

with open("./pmid2contents/pmid2content0.pkl", "rb") as f:
    data = pickle.load(f)

first_key = next(iter(data))
print(first_key, data[first_key])