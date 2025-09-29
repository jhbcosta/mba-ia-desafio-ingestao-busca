from search import search_prompt  # noqa: INP001, D100, I001

def main():  # noqa: ANN201, D103
    while True:
        pergunta = input("Pergunta (ou digite 'sair' para finalizar): ")
        if pergunta.strip().lower() in ["sair", "exit", "fim"]:
            print("Chat finalizado.")
            break
        print("Resposta:", search_prompt(pergunta))  # noqa: T201

if __name__ == "__main__":
    main()  # noqa: W292, RUF100