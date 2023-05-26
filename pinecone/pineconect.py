from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredPDFLoader
from config import PINECONE_API_KEY, PINECONE_API_ENV, OPENAI_API_KEY
import pinecone

loader = UnstructuredPDFLoader("./diegoteca/mexico-86-mi-mundial-mi-verdad.pdf")

data = loader.load()

print(f'You have {len(data)} docuemnt(s) in your data')
print(f'You have {len(data[0].page_content)} character in your document')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

print(f'Now you have {len(texts)} documents')


embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)
index_name = "sandbox"

docsearch = Pinecone.from_texts(
    [t.page_content for t in texts], 
    embeddings, 
    index_name=index_name
)

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

query = """Responde como si fueras Diego: 
    - usuario: Diego no puedo dejar de tomar falopa
    - diego: 
    """
docs = docsearch.similarity_search(query)

print(chain.run(input_documents=docs, question=query))