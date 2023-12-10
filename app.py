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
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

model_path = expanduser("~/OneDrive/Documents/File/Semester 8/website-creation-agent/models/llama-2-13b-chat.Q4_0.gguf")

llm = LlamaCpp(
    model_path=model_path,
    streaming=False,
)

model = Llama2Chat(llm=llm)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)

print(
    chain.run(
        text="What can I see in Vienna? Propose a few locations. Names only, no details."
    )
)
toc = time.time()