import os
from dotenv import load_dotenv
from config import EMBEDDING_MODEL,PG_COLLECTION_NAME
from langchain_community.document_loaders import DirectoryLoader,UnstructuredPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

load_dotenv()

loader=DirectoryLoader(
    os.path.abspath("/home/chirag/Desktop/PDFlINE/sourcedocs"),
    glob="**/*pdf",
    # use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)

docs=loader.load()
print(docs)
#
# embeddings=OpenAIEmbeddings(
#     model=EMBEDDING_MODEL,
# )

# text_splitter= SemanticChunker(
#     embeddings=OpenAIEmbeddings
# )
#
# chunks=text_splitter.split_documents(docs)
# print(chunks)
#
# PGVector.from_documents(documents=chunks,
#                         embeddings=embeddings,
#                         collection_name=PG_COLLECTION_NAME,
#                         connection_string="postgresql+psycopg://postgres@localhost:5432/pdf_rag_vectors",
#                         pre_delete_collection=True,
#                         )