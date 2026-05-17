"""
Hybrid Retriever (BM25 + Chroma)
Goal: combine sparse BM25 retrieval with dense Chroma embeddings.

Expected output: list of top-k documents with hybrid scores
"""

# TODO: import BM25Okapi, Chroma, and HuggingFaceEmbeddings
# TODO: build two indexes (BM25 & Chroma)
# TODO: implement fusion logic:
#        score_hybrid = alpha * dense_score + (1 - alpha) * sparse_score
# TODO: add optional multi-hop expansion using named entities
# TODO: return fused document list


Hint: use model "sentence-transformers/all-MiniLM-L6-v2" for Chroma.