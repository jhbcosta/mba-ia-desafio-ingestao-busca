# Projeto: Ingestão e Busca Semântica com LangChain e pgvector

Este projeto permite a ingestão de documentos PDF, geração de embeddings com LangChain, armazenamento em PostgreSQL com pgvector e busca semântica via CLI.

---

## Pré-requisitos

- Python 3.10 ou superior
- Docker e Docker Compose
- PostgreSQL com extensão pgvector
- (Opcional) Ambiente virtual Python

---

## 1. Instalação

1. **Clone o repositório:**
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   ```

2. **Crie e ative um ambiente virtual (opcional):**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

---

## 2. Configuração do Banco de Dados

1. **Suba o PostgreSQL com pgvector usando Docker Compose:**
   ```sh
   docker-compose up -d
   ```

2. **Verifique se o banco está rodando:**
   ```sh
   docker ps
   ```

---

## 3. Configuração do Ambiente

1. **Copie o arquivo `.env.example` para `.env` e edite conforme necessário:**
   ```sh
   copy .env.example .env
   ```
   - Ajuste as variáveis de conexão e caminhos conforme seu ambiente.
   - Exemplo:
     ```
     DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
     PDF_PATH=./document.pdf
     ```

2. **Coloque o PDF desejado no caminho especificado em `PDF_PATH`.**

---

## 4. Execução

### 4.1. Ingestão do Documento

Execute o script de ingestão para processar o PDF e armazenar os embeddings no banco:

```sh
python ingest.py
```

### 4.2. Inicialização do Chat

Execute o script do chat para iniciar a conversa:

```sh
python chat.py
```

---

## Exemplos de Perguntas e Respostas

| Pergunta                                                                 | Resposta                                                                                                 |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Qual é a capital da França?                                              | Não tenho informações necessárias para responder sua pergunta.                                           |
| Quantos clientes temos em 2024?                                          | Não tenho informações necessárias para responder sua pergunta.                                           |
| Você acha isso bom ou ruim?                                              | Não tenho informações necessárias para responder sua pergunta.                                           |
| Qual o faturamento da Empresa SuperTechIABrazil?                         | R$ 10.000.000,00                                                                                         |
| Qual o ano de fundação da empresa mais velha?                            | 1931                                                                                                     |
| Qual o ano de fundação da empresa mais nova?                             | 2023                                                                                                     |
| Qual a empresa com maior faturamento e em que ano se deu?                | Aliança Esportes ME, com faturamento de R$ 4.485.320.049,16; ano de fundação: 2002.                      |

---

## Observações

- Sempre execute primeiro o `ingest.py` para garantir que o conteúdo esteja no banco antes de iniciar o chat.
- Para adicionar novos PDFs, atualize o arquivo e execute novamente o `ingest.py`.
- Em caso de erros de conexão, revise as variáveis do `.env` e se o container do banco está ativo.

---

## Suporte

Em caso de dúvidas, abra uma issue ou entre em contato com o responsável pelo projeto.
