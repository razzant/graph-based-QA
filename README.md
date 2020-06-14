# graph-based-QA
RDF triple retrieval from WikiData with a trained projection module (fine-tuned DistilBERT) on the graph embeddings (Pytorch-BigGraph)

In this work, we demonstrate how knowledge graphs could improve the quality of question answering and knowledge retrieval systems. The presented approach is based on specially constructed and trained deep neural model, which maps text to the space of pretrained graph embeddings (Pytorch-BigGraph) of a given knowledge base (WikiData). Being trained in a semi-supervised way, the retrieval module searches for relevant facts (in RDF triple format) to a given query providing a list of ranked verifiable facts from WikiData. The presented model significantly outperforms the bag-of-words baseline in terms of Mean Reciprocal Rank (MRR).

Requirements:
  - python                    3.7.6
  - transformers              2.4.1
  - torch                     1.3.1
  - Wikidata                  0.6.1
  - wikidataintegrator        0.5.3
  - en-core-web-sm            2.2.0
