# Brainsoft use case study

## install dependencies
```bash
pip install poetry
poetry install
```
## run frontend locally
```bash
export PYTHONPATH=.
python src/ui/ui.py
```

## Approach to indexation and QA
### Indexation
- Vectara vector database was chosen as a vector store
- this vector store provides few nice features, such as
- - ability to store vectors in a database
- - ability to search for similar vectors
- - grounded generation - reduces hallucinations
- - built-in vectorizer - no need for additional vectorization step
- - ability to store additional metadata
- - automating chunking of long texts - no need to split long texts into smaller chunks manually
- - lambda search - ability to combine both neural search and text based search

Documents are indexed in the following way:
1. Each HTML page is loaded via Langchain document loader
2. then its indexed via lanchain based wrapper into Vectara

### Question answering
Question answering is done in the following way:
1. to answer question also with sources, we need a special type of chain which is called question answering with sources
2. because vectara retriever is already quite capable retriever, we dont have to use state of the art model for answer postprocessing
3. so for that reason, GPT3.5 turbo model is used, which is capable enough to condense retrieved document/s into a single answer
4. also to return the source field from lanchain indexed document a custom postprocessing document prompt template is used
5. the StuffDocumentChain class is used to enable retriever agent to combine multiple retrieved documents and also provided conversation context
6. conversation context is "injected" to the user question via a custom prompt which is created from the conversation context and the user follow-up question


## Chatbots clients
1. Cli client
- This client enables you to chat with the bot from the command line.
2. UI Frontend client - streamlit
- This client enables you to chat with the bot from the browser.
3. REST API client - FastAPI
- This client enables you to chat with the bot via API.

MVC architecture pattern is used for the overal structure of the project.
Where:
1. clients are the "views"
2. controller is Controller class
3. model are the classes which handle question and answer data storage