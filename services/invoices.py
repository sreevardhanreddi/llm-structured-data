import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mistralai import ChatMistralAI

from models import Address, Invoice

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")


def parse_address(address: str):
    # Define a custom prompt to provide instructions and any additional context.
    # 1) You can add examples into the prompt template to improve extraction quality
    # 2) Introduce additional parameters to take context into account (e.g., include metadata
    #    about the document from which the text was extracted.)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
            # Please see the how-to about improving performance with
            # reference examples.
            # MessagesPlaceholder('examples'),
            ("human", "{text}"),
        ]
    )

    llm = ChatMistralAI(
        mistral_api_key=MISTRAL_API_KEY, model="mistral-large-latest", temperature=0
    )

    structured_output = llm.with_structured_output(Address)

    output = prompt | structured_output

    parsed_output = output.invoke(address)
    return parsed_output


def parse_invoice(file_path: str):
    # Define a custom prompt to provide instructions and any additional context.
    # 1) You can add examples into the prompt template to improve extraction quality
    # 2) Introduce additional parameters to take context into account (e.g., include metadata
    #    about the document from which the text was extracted.)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
            # Please see the how-to about improving performance with
            # reference examples.
            # MessagesPlaceholder('examples'),
            ("human", "{text}"),
        ]
    )

    llm = ChatMistralAI(
        mistral_api_key=MISTRAL_API_KEY, model="mistral-large-latest", temperature=0
    )

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    content = [doc.page_content for doc in docs]

    structured_output = llm.with_structured_output(Invoice)

    output = prompt | structured_output

    parsed_output = output.invoke(content)
    return parsed_output
