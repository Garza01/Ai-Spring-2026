"""One-time build script for the MiniClaw starter RAG.

Loads the ACME corpus, chunks it, embeds with all-MiniLM-L6-v2, and persists
a ChromaDB collection to ``miniclaw_starter_rag/chroma_db/``. Subsequent
imports of ``query_miniclaw_rag`` load from disk.

Run from the repo root or from the package directory:

    python "MP3/Part B/miniclaw_starter_rag/build_index.py"
"""

from __future__ import annotations

import pathlib
import sys

import chromadb
from sentence_transformers import SentenceTransformer

_HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

from acme_miniclaw_corpus import acme_documents  # noqa: E402

_DB_DIR = _HERE / "chroma_db"

COLLECTION_NAME = "miniclaw_starter"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap
    return chunks


def build():
    print(f"Loaded {len(acme_documents)} ACME documents")

    print(f"Loading embedding model {EMBED_MODEL_NAME} ...")
    model = SentenceTransformer(EMBED_MODEL_NAME)

    _DB_DIR.mkdir(exist_ok=True)
    client = chromadb.PersistentClient(path=str(_DB_DIR))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    coll = client.create_collection(COLLECTION_NAME)

    ids, texts, metas = [], [], []
    for doc in acme_documents:
        for i, chunk in enumerate(chunk_text(doc["text"])):
            ids.append(f"{doc['id']}__chunk_{i:03d}")
            texts.append(chunk)
            metas.append({
                "doc_id": doc["id"],
                "title": doc["title"],
                "type": doc.get("type", ""),
                "chunk_idx": i,
            })

    print(f"Embedding {len(texts)} chunks ...")
    embeddings = model.encode(
        texts, show_progress_bar=False, normalize_embeddings=True
    ).tolist()

    coll.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metas)
    print(f"Indexed {coll.count()} chunks into '{COLLECTION_NAME}' at {_DB_DIR}")


if __name__ == "__main__":
    build()
