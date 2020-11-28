import os, pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer

def data_reader(dir_path):
    file_content = {}
    for i, f in enumerate(os.listdir(dir_path)):
        doc = open(os.path.join(dir_path, f), 'r', encoding="ISO-8859-1").read()
        doc_line = doc.split("\n")
        flag_title_found = False
        content = ""
        for ln in doc_line:
            if ln != '' and ln[0] != '<':
                if ln[0] == '#':
                    content = ln[1:]
                elif flag_title_found == False:
                    title = ln
                    flag_title_found = True
                elif flag_title_found == True:
                    content += ln
        file_content[i] = {"title": title, "content": content}
    return file_content

def create_vecs(algo, corpus):
    if algo == "tf":
        vectorizer = CountVectorizer()
    elif algo == "tfidf":
        vectorizer = TfidfVectorizer()

    # fc = data_reader(f"./data/{corpus}")
    fc = data_reader(f"./app/engine/data/{corpus}")
    df = pd.DataFrame(fc).T
    
    vect = vectorizer.fit(df["content"])

    # pickle.dump(vect, open(f"./pkls/{corpus}_{algo}.pkl", "wb"))
    if not os.path.exists("./app/engine/pkls"):
        os.mkdir("./app/engine/pkls")

    pickle.dump(vect, open(f"./app/engine/pkls/{corpus}_{algo}.pkl", "wb"))
    return vect

def create_bert_vecs(corpus):
    fc = data_reader(f"./app/engine/data/{corpus}")
    df = pd.DataFrame(fc).T
    bert_model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    bert_embs = bert_model.encode(df["content"])
    pickle.dump(bert_embs, open(f"./app/engine/pkls/{corpus}_bert.pkl", wb))
    return bert_embs

def get_top_docs(q, a, c):
    # if os.path.exists(f"./app/engine/pkls/{c}_{a}.pkl"):
    if os.path.exists(f"./pkls/{c}_{a}.pkl"):
        vect = pickle.load(open(f"./app/engine/pkls/{c}_{a}.pkl", "rb"))
        # vect = pickle.load(open(f"./pkls/{c}_{a}.pkl", "rb"))
    else:
        vect = create_vecs(a, c)
    
    q_vec = vect.transform([q])[0]
    q_arr = q_vec.toarray()[0].reshape(1, -1)

    # fc = data_reader(f"./data/{c}")
    fc = data_reader(f"./app/engine/data/{c}")
    df = pd.DataFrame(fc).T
    
    x_vec = vect.transform(df["content"])
    x_arr = x_vec.toarray()

    # print(f"x_arr.shape: {x_arr.shape}")
    # print(f"q_arr.shape: {q_arr.shape}")

    if a == "bert":
        # sims = {}
        # for i, doc in enumerate()
        pass
    else:
        sims = {}
        for i, doc in enumerate(x_arr):
            # print(f"doc.shape: {doc.shape}\t:q_arr.shape {q_arr.shape}")
            sim_score = cosine_similarity(doc.reshape(1, -1), q_arr)[0][0]
            sims[i] = sim_score
        sims_sorted = {k: v for i, (k, v) in enumerate(sorted(sims.items(), key=lambda item: item[1], reverse=True)) if i < 10}
        # sims_sorted = {k: v for i, (k, v) in enumerate(sorted(sims.items(), key=lambda item: item[1], reverse=True))}

    ret_docs = {}
    for idx, (k, v) in enumerate(sims_sorted.items()):
        ret_docs[k] = fc[k]

    return ret_docs