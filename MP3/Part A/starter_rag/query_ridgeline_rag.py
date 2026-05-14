"""Query helper for the MP3 Part A starter RAG.

Loads the persisted ChromaDB collection built by ``build_starter_rag.py``
and returns the top-N matching chunks for a natural-language question.

This is the function students wrap as a tool (function-calling schema) in
Section 3 of the MP3 Part A notebook.
"""

from __future__ import annotations

import pathlib
from functools import lru_cache

import chromadb
from sentence_transformers import SentenceTransformer

_HERE = pathlib.Path(__file__).resolve().parent
_DB_DIR = _HERE / "chroma_db"

COLLECTION_NAME = "ridgeline_starter"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _get_model() -> SentenceTransformer:
    return SentenceTransformer(EMBED_MODEL_NAME)


@lru_cache(maxsize=1)
def _get_collection():
    if not _DB_DIR.exists():
        raise FileNotFoundError(
            "Starter RAG ChromaDB not found. Run "
            "`python MP3/Part\\ A/starter_rag/build_starter_rag.py` first."
        )
    client = chromadb.PersistentClient(path=str(_DB_DIR))
    return client.get_collection(COLLECTION_NAME)


def query_ridgeline_rag(question: str, n_results: int = 3) -> dict:
    """Search the Ridgeline Engineering Partners knowledge base.

    Searches Ridgeline Engineering Partners' internal knowledge base — past
    project summaries, billing rates, technical standards, employee policies,
    FEA guidelines, and material selection reports. Use this whenever the user
    asks about Ridgeline's specific projects, internal practices, or
    company-specific information.

    Args:
        question: Natural-language question.
        n_results: Number of chunks to return (default 3, max 10).

    Returns:
        dict with:
            "chunks":  list of {"text", "doc_id", "title", "score"}
            "summary": short 1-line summary of what was retrieved
    """
    n_results = max(1, min(int(n_results), 10))
    coll = _get_collection()
    model = _get_model()
    q_emb = model.encode([question], normalize_embeddings=True).tolist()
    res = coll.query(query_embeddings=q_emb, n_results=n_results)

    chunks = []
    for text, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        # ChromaDB returns L2 distance over normalized vectors; convert to a
        # cosine-similarity-style score in [0, 1].
        score = max(0.0, 1.0 - dist / 2.0)
        chunks.append({
            "text": text,
            "doc_id": meta["doc_id"],
            "title": meta["title"],
            "score": round(score, 4),
        })

    summary = (
        f"{len(chunks)} chunks retrieved. "
        f"Top match: {chunks[0]['doc_id']} — {chunks[0]['title']} (score {chunks[0]['score']})."
        if chunks else "No chunks retrieved."
    )
    return {"chunks": chunks, "summary": summary}


if __name__ == "__main__":
    # Smoke test
    out = query_ridgeline_rag("What is the standard billing rate for senior engineers?", 3)
    print(out["summary"])
    for c in out["chunks"]:
        print(f"  [{c['doc_id']}] {c['title']} (score {c['score']})")
        print("   ", c["text"][:160].replace("\n", " "), "...")
