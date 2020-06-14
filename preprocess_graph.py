from tqdm import tqdm
import numpy as np

if __name__ == "__main__":
    entities = []
    embs = []

    with open("../data/razzhigaev/wikidata_translation_v1.tsv") as f:
        first_line = f.readline()
        for i in tqdm(range(78404883)):
            if i > 2 * (78404883 // 3 - 40000):
                name_emb = f.readline().strip().split("\t")
                name, emb = name_emb[0],name_emb[1:]
                splitted = name.split("/")
                if len(splitted) > 2 and "entity" in splitted[-2]:
                    name = splitted[-1][0:-1]
                    entities.append(name)
                    emb = list(map(lambda x: float(x),emb))
                    embs.append(emb)

                if i == 78404883 - 40000:
                    np.save("all_embeddings3",embs)
                    np.save("all_entities3",entities)
                    print("SAVED")
                    print(len(embs))
                    break
            else:
                f.readline()
                
    

    
