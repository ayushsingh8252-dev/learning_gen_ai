from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    provider="hf-inference",
    max_new_tokens=100,
)

result = llm.invoke("Who is the CEO of OpenAI?")
print(result)
