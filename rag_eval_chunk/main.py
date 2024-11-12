from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.evaluation import (
	DatasetGenerator,
	FaithfullnessEvaluator,
	RelevancyEvaluator,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

from rag_eval_chunk.utils import get_project_path

llm = Ollama(model="llama3.1", request_timeout=300.0)
Settings.llm = llm
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# load data
documents = SimpleDirectoryReader(
	input_files=[get_project_path("docs/2307.09288v2.pdf")]
).load_data()

eval_documents = documents[:3]
data_generator = DatasetGenerator.from_documents(eval_documents)
eval_questions = data_generator.generate_questions_from_nodes()
