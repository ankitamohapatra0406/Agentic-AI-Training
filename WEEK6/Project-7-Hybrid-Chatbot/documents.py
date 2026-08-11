from langchain_core.documents import Document

documents=[
    Document(
        page_content=(
            "Retrieval-Augmented Generation (RAG) combines information "
            "retrieval with a language model. It retrieves relevant information "
            "from an external knowledge base and provides it to the language model "
            "as context."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "Embeddings are numerical representations of text. Similar pieces "
            "of text have similar embeddings, which allows systems to perform "
            "semantic search."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "A vector database stores embeddings and allows applications to "
            "efficiently find information that is semantically similar to a query."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "Keyword search finds documents by matching important words from "
            "the user's query with words appearing in the documents."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "Hybrid search combines semantic search and keyword search. "
            "This improves retrieval because semantic search understands meaning "
            "while keyword search can find exact terms."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "LangChain is a framework for building applications powered by "
            "large language models. It provides components for prompts, models, "
            "retrievers, and chains."
        ),
        metadata={"source": "sample.txt"}
    ),

    Document(
        page_content=(
            "LangGraph is a framework for building stateful applications and "
            "agent workflows using graphs. It is useful for creating multi-step "
            "and multi-agent AI systems."
        ),
        metadata={"source": "sample.txt"}
    ),
]