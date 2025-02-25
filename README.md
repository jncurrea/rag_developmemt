# **RAG-Based LLM Assistant**

## **Overview**
This project implements a **Retrieval-Augmented Generation (RAG) system** that allows a **Large Language Model (LLM)** to answer questions based on a given document. The system utilizes **FAISS for vector storage, OpenAI GPT-4 for text generation, and Streamlit for the user interface.**

## **Features**
- Loads and processes a document by splitting it into chunks.
- Stores document embeddings in a FAISS vector database.
- Retrieves relevant document chunks based on user queries.
- Generates responses using GPT-4 based on the retrieved text.
- Provides an interactive **web UI** for user interaction.

## **Installation**
### **1. Clone the Repository**
```bash
git clone https://github.com/jncurrea/rag_developmemt.git
cd rag_developmemt
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up API Keys**
Create a `.env` file in the project root and add:
```bash
OPENAI_API_KEY=your-openai-api-key
```

### **5. Run the Application**
```bash
streamlit run app.py
```

## **Project Workflow**
### **1. Document Processing**
- The document is loaded and split into chunks for efficient processing.
- FAISS stores these chunks as embeddings using OpenAI’s embedding model.

### **2. Query Processing**
- The system retrieves the most relevant document chunks using FAISS.
- GPT-4 generates responses based on the retrieved text.

### **3. User Interface**
- Streamlit provides an interactive UI where users can input queries and receive responses.

## **Technologies Used**
- **LangChain**: For handling document processing and retrieval.
- **FAISS**: For storing and searching vector embeddings.
- **OpenAI GPT-4**: For generating responses.
- **Streamlit**: For creating the user interface.

## **Test Cases**
Example queries tested with the system:
| **Question** | **Response** |
|-------------|-------------|
| Who wrote the document? | Ramnath Balasubramanian, Ari Libarikian, and Doug McElhaney |
| What is the document about? | The impact of AI in the insurance industry and how companies should adapt. |
| What does the document mention about neural networks? | It discusses convolutional neural networks for AI applications. |
| How can insurers prepare for AI-driven changes? | By optimizing data strategies and adopting AI technologies. |

## **Future Improvements**
- Support for multiple documents.
- Deploy on **Google Cloud** for scalability.
- Optimize chunking strategies for better retrieval.
- Track accuracy and response latency for performance monitoring.

## **Contributors**
- Jose Currea

For any questions or suggestions, feel free to open an issue or reach out!

