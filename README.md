# RAG Project
This project is an implementation of a Retrieval-Augmented Generation (RAG) system designed to handle question and answer tasks across multiple documents.  
It maintains an ongoing chat history to provide context for each interaction, enhancing the relevance of responses based on previous conversations.

## Features:

RAG-based Q&A: Uses a retrieval model to fetch relevant documents and a generation model to produce meaningful answers based on the content of the documents.

Multiple File Support: Capable of handling and retrieving information from multiple files, making it versatile for different datasets.

Chat History: Retains chat history to provide contextual answers based on prior interactions, improving the conversational flow.

## Requirements
- Python 3.11.5 or later

## Installation

### Install requieed packages
```bash
$ pip install -r requirements.txt
```

### Set up the environment variables
```bash
$ copy .env.example .env
```

Set enviroment variable in the `.env` file, such as `OPENAI_API_KEY` value

## Run Docker Compose Services
```bash
$ cd docker
$ copy .env.example .env
```

Then update .env with your credentials

## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## (Optional) Run Ollama Local LLM Server using Colab + Ngrok
[colab-notebook](https://colab.research.google.com/drive/1GUnm9Gt8eDuPRCEF0op_98p0ywrDGtZJ?usp=sharing)