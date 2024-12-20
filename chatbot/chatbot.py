#third party libraries
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv
from langchain import hub
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain_openai import AzureChatOpenAI
from langchain_community.document_loaders import PyPDFLoader # for loading pdf files

load_dotenv() # load environment variables

llm = AzureChatOpenAI(
    azure_deployment="gpt-4",  # or your deployment
    api_version="2024-02-01",  # or your api version
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

embeddings = AzureOpenAIEmbeddings(
    model="text-embedding-ada-002",
)

vector_store = InMemoryVectorStore(embeddings)

#load healthy living pattern doc -- refactor such that you can load multiple docs
loader = PyPDFLoader("documents/healthy_eating_pattern.pdf")

docs = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Index chunks
vector_store.add_documents(documents=all_splits)

# Define prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


def chatbot_compile():
    # Compile application and test
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()
    return graph

if __name__ == "__main__":
    graph = chatbot_compile()
    response = graph.invoke({"question": "Whats in a healthy eating pattern?"})
    print(f"response is type {type(response)}")
    print(response["answer"])