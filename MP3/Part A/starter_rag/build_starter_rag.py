"""Build the MP3 Part A starter RAG.

Re-uses the Ridgeline Engineering Partners corpus from MP2 Part A. Embeds it
with all-MiniLM-L6-v2 and persists a ChromaDB collection to
``starter_rag/chroma_db/``. Run once; subsequent imports load from disk.

Run from the repo root or from MP3/Part A/:
    python "MP3/Part A/starter_rag/build_starter_rag.py"
"""

from __future__ import annotations

import json
import pathlib
import sys

import chromadb
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------------
# Paths — work whether script is run from repo root or its own folder
# ---------------------------------------------------------------------------

_HERE = pathlib.Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent.parent  # MP3/Part A/starter_rag/ → repo root
_CORPUS_DIR = _REPO_ROOT / "MP2" / "Part A" / "corpus"
_DB_DIR = _HERE / "chroma_db"

COLLECTION_NAME = "ridgeline_starter"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 500   # characters
CHUNK_OVERLAP = 100


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    """Simple character-window chunker (matches the MP2 Section 3 pattern)."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap
    return chunks


def load_corpus():
    if not _CORPUS_DIR.exists():
        raise FileNotFoundError(
            f"Could not find Ridgeline corpus at {_CORPUS_DIR}. "
            "This script expects the MP2 Part A corpus to already exist."
        )
    manifest_path = _CORPUS_DIR / "manifest.json"
    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)
    docs = []
    for entry in manifest:
        text = (_CORPUS_DIR / entry["filename"]).read_text(encoding="utf-8")
        docs.append({"id": entry["id"], "title": entry["title"], "text": text})
    return docs


def build():
    print(f"Loading Ridgeline corpus from {_CORPUS_DIR} ...")
    docs = load_corpus()
    print(f"  Loaded {len(docs)} documents")

    print(f"Loading embedding model {EMBED_MODEL_NAME} ...")
    model = SentenceTransformer(EMBED_MODEL_NAME)

    _DB_DIR.mkdir(exist_ok=True)
    client = chromadb.PersistentClient(path=str(_DB_DIR))
    # Delete and recreate so re-runs are deterministic
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    coll = client.create_collection(COLLECTION_NAME)

    ids, texts, metas = [], [], []
    for doc in docs:
        for i, chunk in enumerate(chunk_text(doc["text"])):
            ids.append(f"{doc['id']}__chunk_{i:03d}")
            texts.append(chunk)
            metas.append({"doc_id": doc["id"], "title": doc["title"], "chunk_idx": i})

    print(f"Embedding {len(texts)} chunks ...")
    embeddings = model.encode(texts, show_progress_bar=False, normalize_embeddings=True).tolist()

    coll.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metas)
    print(f"Indexed {coll.count()} chunks into '{COLLECTION_NAME}' at {_DB_DIR}")


if __name__ == "__main__":
    build()
    sys.exit(0)
