import time
from pymilvus import DataType, utility, Collection, connections, CollectionSchema, FieldSchema
from typing import Union, List
from functools import reduce


class MilvusDB:
    def __init__(self, host: str, port: str):
        self.__host = host
        self.__port = port
        connections.connect(host=self.__host, port=self.__port)
        self.info()
        # Default field
        self.__field = [
            FieldSchema(name="id", dtype=DataType.INT64, auto_id=True, is_primary=True),
            FieldSchema(name="chunk_id", dtype=DataType.INT64),
            FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=65535),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=1024)
        ]

    def info(self):
        """
        Display connection information of Milvus.
        """
        print(f"Milvus | Host Server : {self.__host} | Port: {self.__port}")
        # print(f"All collections: {reduce(lambda e1,e2: e1+','+e2, utility.list_collections())}")

    @staticmethod
    def insert_data(collection_name: str, data: List[dict], chunk_size: int = 1000) -> None:
        """
        Batch insert data into the database.
        This function takes a list of data and inserts it into the database in a batch manner,
        improving efficiency for large datasets.

        Args:
            collection_name: the name of the collection
            data: the data that you want to insert into the database
            chunk_size: batch size for each insertion
        """
        if utility.has_collection(collection_name):
            collection = Collection(collection_name)

        else:
            raise ValueError(f"{collection_name} does not existed. Please check your collection name.")

        # Insert data by `chunk_size`.
        for i in range(0, len(data), chunk_size):
            collection.insert(data[i:i+chunk_size])
        # After final entity is inserted, it is best to call flush to have no growing segments left in memory.
        collection.flush()

    def create_collection(
            self,
            collection_name: str,
            total_number: int,
            field: List[FieldSchema] = None,
            index_type: str = "FLAT",
            metric_type: str = "COSINE"
    ) -> None:
        """Create an empty collection.

        Args:
            collection_name: the name of the collection
            total_number: the total number of your dataset
            field: all columns that you want to add to the `collection_name`
            index_type: indexing algorithm for arranging data. ref: https://milvus.io/docs/v2.3.x/index.md
            metric_type: to measure the metric of distance between vectors. ref: https://milvus.io/docs/v2.3.x/metric.md

        """
        if not utility.has_collection(collection_name):  # True if collection exists, false if it does not.
            # Add fields to schema.
            fields = field if field else self.__field
            schema = CollectionSchema(fields)
            collection = Collection(collection_name, schema)

            # Prepare index parameters.
            nlist = int(4 * (total_number ** 0.5))
            index = {
                "index_type": index_type,
                "metric_type": metric_type,
                "params": {"nlist": nlist}
            }
            collection.create_index(field_name="embeddings", index_params=index)
            print(f"Collection '{collection_name}' created successfully.")

        else:
            print(f"Collection '{collection_name}' already exists")

    @staticmethod
    def search(
            query: Union[List[list], list],
            collection_name: str,
            anns_field: str,
            output_filed: List[str],
            top_k: int = 1,
            nprobe: int = 1,
            metric_type: str = "COSINE"
    ) -> List[List[dict]]:
        """
        Search the database based on query vectors.
        This function searches the database and return that are most similar to the provided query vector.

        Args:
            query: question vectors
            collection_name: the name of the collection
            anns_field: the name of the field to search on
            output_filed: the name of the field to return. Milvus supports returning the vector field
            top_k: the number of most similar results to return. Default is 1
            nprobe: the number of most similar clusters to return. Default is 1
            metric_type: to measure the metric of distance between vectors. this setting must be same when you create the collection

        Returns:
            results: The contents of 'top_k' similar results
        """
        if utility.has_collection(collection_name):  # True if collection exists, false if it does not.
            collection = Collection(collection_name)
            # The collection must be loaded before search operation.
            if str(utility.load_state(collection_name)) == "NotLoad":
                collection.load(replica_number=2)
        else:
            raise ValueError(f"{collection_name} does not existed. Please check your collection name.")

        s_time = time.time()
        results = collection.search(
            data=query,
            anns_field=anns_field,
            output_fields=output_filed,
            limit=top_k,
            param={
                "metric_type": metric_type,
                "offset": 0,
                "param": {
                    "nprobe": nprobe
                }
            }
        )
        e_time = time.time()
        print(f"Search complete | cost time: {e_time-s_time}s")

        return results
