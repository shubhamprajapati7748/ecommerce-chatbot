import pandas as pd 
from langchain_core.documents import Document 

def dataConverter():
    products_data = pd.read_csv("../dataset/flipkart_product_reviews.csv")

    data = products_data[['product_title', 'review']]

    product_docs = []

    for index, row in data.iterrows():
        metadata = {"product_name" : row['product_title']}
        doc = Document(page_content=row['review'], metadata=metadata)
        product_docs.append(doc)

    return product_docs

# if __name__ == "__main__":
#     docs = dataConverter()
#     print(docs)