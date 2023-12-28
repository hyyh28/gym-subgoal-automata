from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
import openai
chat_model = AzureChatOpenAI(openai_api_key="f825f61246354ec090c5703ca4f76418", openai_api_version="2023-05-15",
                             openai_api_type="azure", openai_api_base="https://midivi-main-scu1.openai.azure.com",
                             deployment_name="gpt-35-turbo", temperature=0, max_tokens=10)
