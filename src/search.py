import os  # noqa: INP001, D100, I001
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def search_prompt(question=None):  # noqa: ANN201, D103, ARG001, ANN001
    for k in ("OPENAI_API_KEY", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME"):
        if not os.getenv(k):
            raise RuntimeError(f"Environment variable {k} is not set")  # noqa: TRY003, EM102

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")  # noqa: COM812
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    results = store.similarity_search_with_score(question, k=10)  # noqa: F841

    prompt_template = PromptTemplate.from_template(
        template="""
        CONTEXTO:
        {contexto}

        REGRAS:
        - Responda somente com base no CONTEXTO.
        - Se a informação não estiver explicitamente no CONTEXTO, responda:
        "Não tenho informações necessárias para responder sua pergunta."
        - Nunca invente ou use conhecimento externo.
        - Nunca produza opiniões ou interpretações além do que está escrito.

        EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
        Pergunta: "Qual é a capital da França?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."

        Pergunta: "Quantos clientes temos em 2024?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."

        Pergunta: "Você acha isso bom ou ruim?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."

        PERGUNTA DO USUÁRIO:
        {pergunta}

        RESPONDA A "PERGUNTA DO USUÁRIO"
        """,
    )

    model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

    chain = prompt_template | model

    result = chain.invoke({"contexto": results, "pergunta": question})
    return result.content
