from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredPDFLoader
from config import PINECONE_API_KEY, PINECONE_API_ENV, OPENAI_API_KEY, PINECONE_INDEX_NAME 
import pinecone


class VectorStorage:
    """
    This class is responsible for storing 
    and searching documents in a Pinecone index
    using OpenAI embeddings.
    """
    
    
    def __init__(self, chunk_size=1000, chunk_overlap=0):
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.index_name = PINECONE_INDEX_NAME
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # Initialize Pinecone
        pinecone.init(
            api_key=PINECONE_API_KEY,
            environment=PINECONE_API_ENV
        )

    def _load_texts(self, pdf_path):
        data = UnstructuredPDFLoader(pdf_path).load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, 
            chunk_overlap=self.chunk_overlap)

        print(f'You have {len(data)} document(s) in your data')
        print(f'You have {len(data[0].page_content)} character in your document')
        texts = text_splitter.split_documents(data)
        print(f'Now you have {len(texts)} documents')
        return texts

    def search_similar_documents(self, query, pdf_path):
        texts = self._load_texts(pdf_path)
        docsearch = Pinecone.from_documents(texts, self.embeddings, index_name=self.index_name)
        docs = docsearch.similarity_search(query)
        return docs[0].page_content