from chat_modules.llamaindex import ServiceChatModule
from utils import StandardlizedDeepEvalLLM
from deepeval.synthesizer import Synthesizer
from deepeval.dataset import EvaluationDataset

# Define chat model
chat_service = ServiceChatModule(service_name="GEMINI")
chat_model = chat_service.get_chat_model()

# Define Deep Eval model
model = StandardlizedDeepEvalLLM(model = chat_model)

# Generates golden from documents
synthesizer = Synthesizer(model = model)
synthesizer.generate_goldens_from_docs(
    document_paths=['example.txt', 'example.docx', 'example.pdf'],
    max_goldens_per_document=2
)

# Generates golden from provided context
# synthesizer.generate_goldens(
#     contexts=[
#         ["The Earth revolves around the Sun.", "Planets are celestial bodies."],
#         ["Water freezes at 0 degrees Celsius.", "The chemical formula for water is H2O."],
#     ]
# )

# Saved as files
synthesizer.save_as(
    file_type='json', # or 'csv'
    directory="./synthetic_data"
)