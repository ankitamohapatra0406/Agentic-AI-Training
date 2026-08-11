from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from rank_bm25 import BM25Okapi
from documents import documents

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore=Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="hybrid_chatbot"
)

texts=[doc.page_content for doc in documents]

tokenized_documents = [
    text.lower().split()
    for text in texts
]

bm25=BM25Okapi(tokenized_documents)

def hybrid_search(query, k=3):

    semantic_results=vectorstore.similarity_search(
        query,
        k=k
    )
    tokenized_query=query.lower().split()

    keyword_scores=bm25.get_scores(tokenized_query)

    keyword_indices=sorted(
        range(len(keyword_scores)),
        key=lambda i: keyword_scores[i],
        reverse=True
    )[:k]

    keyword_results = [
        documents[i]
        for i in keyword_indices
    ]

    combined=[]

    for doc in semantic_results + keyword_results:
        if doc.page_content not in [
            existing.page_content
            for existing in combined
        ]:
            combined.append(doc)

    return combined[:k]