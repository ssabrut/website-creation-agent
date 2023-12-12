from os.path import expanduser
from langchain_experimental.chat_models import Llama2Chat
from langchain.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
import time

template_messages = [
    SystemMessage(content="You are a web developer that masters HTML and CSS."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

model_path = expanduser(
    "~/OneDrive/Documents/File/Semester 8/website-creation-agent/models/llama-2-7b-chat.Q5_K_M.gguf"
)

llm = LlamaCpp(
    model_path=model_path,
    streaming=True,
)

model = Llama2Chat(llm=llm)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)
prompt = """Make a simple landing page website for coffeeshop using HTML and CSS"""

tic = time.time()
result = chain.run(text=prompt)
print(result)
toc = time.time()
minute, second = divmod(toc - tic, 60)
print(f"Time: {int(minute)} minutes {int(second)} seconds")
