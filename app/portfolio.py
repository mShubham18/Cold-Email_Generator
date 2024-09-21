import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path = "app/Resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        #self.client = chromadb.PersistentClient("vectorstore")
        self.client = chromadb.Client(settings={"persist_directory": "vectorstore"})
        #
        self.collection = self.client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
               self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links":row["Links"]},
                    ids=[str(uuid.uuid4())]
                )
    def query_links(self, skills):
        return self.collection.query(query_texts=["Experience in Python","Experience in React Native"],n_results = 2).get("metadatas",[])