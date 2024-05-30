from ai_modules.chatmodel_modules import ServiceChatModel
# from ai_modules.embedding_modules import ServiceEmbedding
# from llama_index.readers.web import TrafilaturaWebReader
# from llama_index.core.node_parser import SentenceSplitter
from evaluating_modules import CustomDeepEvalLLM

# Define chat model
chat_service = ServiceChatModel(service_name="GEMINI")
chat_model = chat_service.get_chat_model()
#
# # Define embedding model
# embedding_service = ServiceEmbedding(service_name="TOGETHER")
# embedding_model = embedding_service.get_embedding_model()
#
# # Define reader
# reader = TrafilaturaWebReader()
# splitter = SentenceSplitter(chunk_size=800,chunk_overlap=100)
# # Get documents
# documents = reader.load_data(["https://en.wikipedia.org/wiki/Neymar"])
# documents = splitter.get_nodes_from_documents(documents=documents)

custom_llm = CustomDeepEvalLLM(model=chat_model)
print(custom_llm.generate("Write me a joke"))

# from deepeval.dataset import EvaluationDataset
#
# dataset = EvaluationDataset()
# dataset.generate_goldens_from_docs(
#     document_paths=['Python-Developer-SOTATEK.pdf'],
#     max_goldens_per_document=10
# )


