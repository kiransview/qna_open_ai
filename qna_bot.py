from typing import Any
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


def run_llm(query: str) -> Any:
    pdf_path = "shashi_resume.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=200, separator="\n")
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_text")

    new_vectorstore = FAISS.load_local("faiss_text", embeddings)
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=new_vectorstore.as_retriever()
    )
    return qa({"query": query})


if __name__ == "__main__":
    print(run_llm(query="Give me some intro about Shashi Kiran in 3 Sentences"))
