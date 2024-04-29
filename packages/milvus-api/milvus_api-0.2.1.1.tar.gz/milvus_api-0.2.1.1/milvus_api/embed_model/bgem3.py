import torch
import numpy as np
from pymilvus.model.hybrid import BGEM3EmbeddingFunction
from typing import List


class PyMilvusBGEM3:
    def __init__(
            self,
            model_name: str,
            device: str = "cpu",
            use_fp16: bool = False
    ):
        if torch.cuda.is_available():
            device = 'cuda:0'
            use_fp16 = True
        self.bge_m3 = BGEM3EmbeddingFunction(
            model_name=model_name,
            device=device,
            use_fp16=use_fp16
        )

    def encode(self, query: List[str] = None, doc: List[str] = None) -> List[np.ndarray]:
        """
        Vectorize user input for database search.
        This function takes the user input and transforms it into a numerical vector using a BGE-M3.

        Args:
            query: single question or chunked query
            doc: multiple questions or chunked queries

        Returns:
             embeddings['dense']: numerical vectors representing the input.
        """
        embeddings = ""
        if query:
            embeddings = self.bge_m3.encode_queries(query)

        if doc:
            embeddings = self.bge_m3.encode_documents(doc)

        return embeddings['dense']
