from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI
from .settings import settings
from .schemas import UserInput
from .logging import logger

qa_prompt_template = """
Your task is to write a formal letter addressed to a person named {person}. 
In the letter, clearly state the reason for your appeal based on {reason}, 
maintaining a polite and professional tone throughout. Ensure the letter 
includes an appropriate greeting, a clear explanation of the purpose, and a courteous closing.

Answer:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=qa_prompt_template
)

async def write_letter(user_message: UserInput) -> str:
    logger.info("write letter function")
    formatted_prompt = prompt.format(person=user_message.name, reason=user_message.reason)
    logger.debug(f"Formatted prompt: {formatted_prompt}")
    try:
        messages = [HumanMessage(content=formatted_prompt)]
        result = await settings.llm.ainvoke(messages)
        return result.content if hasattr(result, "content") else str(result)
    except Exception as e:
        raise 
