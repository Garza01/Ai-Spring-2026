"""ACME Robotics MiniClaw knowledge base — re-export for MP3 Part B.

The corpus itself lives in ``MP2/Part B/corpus/`` (15 documents covering
manufacturing capabilities, material test data, previous product history,
engineering design standards, vendor communications, and project status).
We re-use it here so MP2 and MP3 stay in sync.

Load with:
    from acme_miniclaw_corpus import acme_documents
    print(f"Loaded {len(acme_documents)} ACME documents")
"""

from __future__ import annotations

import json
import pathlib

_HERE = pathlib.Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent.parent  # MP3/Part B/miniclaw_starter_rag/ → repo root
_CORPUS_DIR = _REPO_ROOT / "MP2" / "Part B" / "corpus"


def _load_corpus():
    if not _CORPUS_DIR.exists():
        raise FileNotFoundError(
            f"ACME corpus not found at {_CORPUS_DIR}. The MP3 starter RAG "
            f"re-uses the MP2 Part B corpus — make sure that folder exists."
        )
    manifest_path = _CORPUS_DIR / "manifest.json"
    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)

    docs = []
    for entry in manifest:
        text = (_CORPUS_DIR / entry["filename"]).read_text(encoding="utf-8")
        docs.append({
            "id": entry["id"],
            "title": entry["title"],
            "type": entry["type"],
            "date": entry.get("date", ""),
            "author": entry.get("author", ""),
            "text": text,
        })
    return docs


acme_documents = _load_corpus()
