"""
Logic for ingesting documents into MongoDB vector store
"""

import os
from typing import List, Optional, Set

from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print as rich_print

from lango_cli_beta.rag_config import RagConfig
from lango_cli_beta.utils import initialize_vectorstore


def _list_files_recursively(folder_path: str) -> List[str]:
    all_files: List[str] = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if full_path.endswith(".txt") or full_path.endswith(".pdf"):
                all_files.append(full_path)
    return all_files


def _transform_data_to_documents(
    ingest_path: str,
    metadata: Optional[dict] = None,
    chunk_size: int = 500,
    chunk_overlap: int = 75,
) -> dict:
    """
    Convert the data provided by the user, into a list
    of LangChain documents.
    """
    # Read the data from the ingest path
    filepaths = _list_files_recursively(ingest_path)

    loader = UnstructuredFileLoader(filepaths)
    unsplit_docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=int(chunk_size),
        chunk_overlap=int(chunk_overlap),
        length_function=len,
        is_separator_regex=False,
        add_start_index=True,
    )

    docs: List[Document] = text_splitter.split_documents(unsplit_docs)

    # remap metadata
    unique_metadata_keys: Set[str] = set()
    for doc in docs:
        doc.metadata = {
            **(metadata or {}),
            "_path": doc.metadata["source"][0],
        }
        unique_metadata_keys.update(doc.metadata.keys())

    return {
        "docs": docs,
        "unique_metadata_keys": unique_metadata_keys,
    }


class Ingester:
    ingest_path: str

    metadata: Optional[dict] = None

    chunk_size: int = 500

    chunk_overlap: int = 75

    should_ingest: bool = True

    def __init__(self, config: RagConfig) -> None:
        if config.ingest_path is None:
            raise ValueError("An ingest path must be provided when ingesting data.")

        self.ingest_path = config.ingest_path
        self.metadata = config.metadata
        self.chunk_size = config.chunk_size
        self.chunk_overlap = config.chunk_overlap
        # Env var which controls whether or not to ingest data.
        # Defaults to True, and will only be False if explicitly set to "False".
        self.should_ingest = os.getenv("SHOULD_INGEST_DATA") != "False"

    def ingest_data(self) -> None:
        """Ingest the data into the MongoDB vector store.
        First, convert the raw ingest data into LangChain documents.
        Then, ingest the documents into the MongoDB vector store
        using the MongoDocumentStore to index the documents.
        """
        docs_and_metadata_keys = _transform_data_to_documents(
            self.ingest_path,
            metadata=self.metadata,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )
        docs = docs_and_metadata_keys["docs"]
        vectorstore = initialize_vectorstore()

        ids = []
        if self.should_ingest:
            ids = vectorstore.add_documents(docs)

        rich_print(f"Added [bold #0af2b0]{len(ids)}[/bold #0af2b0] docs.")
