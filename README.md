# AI Personal Coach 

This is a Retrieval-Augmented Generation (RAG) based chatbot application that combines a retrieval component and a generative language model to provide informative and context-aware responses.

## Overview

This application is an advanced, AI-powered fitness advice system that provides personalized health and fitness recommendations. It utilizes the power of LLM, NLP, vector embeddings, Vector databases, RAG and other advanced technologies to process fitness-related documents and user queries, delivering tailored advice through an interactive chat interface.


## Features

- **Retrieval-Augmented Generation**:
- **Knowledge Base Integration**:
- **User authentication and personalization**:
- **Customizable Retrieval Strategies**:
- **Interactive Chatbot Interface**:
- **API endpoints for document upload, user management, and chat functionality**:


## Architecture 

The application follows the Model-View-Controller (MVC) pattern and is built using the following technologies:


Document Processing: Langchain
Embeddings: Hugging Face
Vector Database: Chroma DB
User Data Storage: MongoDB
Frontend: Mesop (for chat interface), Streamlit for prototyping
Containerization: Docker
Backend: FastAPI

## System Flow Diagram
![alt text](<System Design.drawio.png>)

This diagram illustrates the data flow and processing steps in the application, including:

- Document chunking and embedding
- User query processing
- Vector similarity search
- Personalized response generation using LLM


## UML Class Diagram
![alt text](<System UML Diagram2.png>)
This diagram shows the structure of the application's codebase, including:

Assets (Chroma collections and document files)
Models (BaseDataModel for document processing)
Utils (Configuration and database utilities)
Controllers (ProcessController, BaseController, DocumentController)
Views (mesop_chat_view, streamlitchatview)
Routes (API endpoints)
Deployment files

**System Components**

1. Document Processing Pipeline
2. User Query Processing
3. Vector Similarity Search
4. Personalization Engine
5. LLM Integration
6. API Layer
7. User Interface

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Abdallahelraey/Fitness-Chatbot.git
   ```

2. Install the required dependencies:

   ```
   $ python setup.py develop 
   ```

## Installation using docker

Prerequisites

Docker
Docker Compose

Setup

Clone the repository:
```
git clone https://github.com/Abdallahelraey/Fitness-Chatbot.git
```


Build and run the Docker containers:
```
Copydocker-compose up --build
```


## Usage

### Run the FastAPI server

```
uvicorn main:app  --reload --host 0.0.0.0 
```

### Run the Mesop chat interface
```
mesop chatbot\src\viewers\MesopChat.py
```
#### Mesop Chat demo
![alt text](<mesop chat view.png>)


For detailed API documentation, visit http://localhost:8000/docs after starting the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache License](LICENSE).
