import streamlit as st
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from openai import OpenAI
import time

# Set API key (Make sure it's set in your environment)
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"  # Or set it in your terminal

# Load FAISS index
faiss_index_path = "faiss_index"
embeddings = OpenAIEmbeddings()
vector_store = FAISS.load_local(faiss_index_path, embeddings, allow_dangerous_deserialization=True)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# Function to retrieve relevant chunks from FAISS
def retrieve_context(query, k=15):
    """
    Retrieve the most relevant document chunks for the given query.
    Ensures proper formatting to avoid vertical text issues.
    """
    docs = vector_store.similarity_search(query, k=k)
    
    formatted_context = "\n\n---\n\n".join(
        [doc.page_content.replace("\n", " ").strip() for doc in docs]
    )

    return formatted_context

# ✅ Function to generate answers using FAISS + GPT-4
def ask_document(query):
    start_time = time.time()
    context = retrieve_context(query)

    prompt = f"""
    You are an AI assistant that answers questions based only on the given document.
    If the answer is not found in the document, say "Sorry, no relevant information found."

    Ensure your response is formatted correctly, using full sentences. 
    DO NOT return text one letter per line.

    Context:
    {context}

    Question: {query}

    Answer:"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    end_time = time.time()
    latency = end_time - start_time
    print(f"⚡ Query processed in {latency:.2f} seconds")

    return response.choices[0].message.content.strip()

# ✅ Streamlit UI
st.title("📄 RAG-Based AI Assistant")

st.write("Enter a question related to the document, and the AI will respond based on the retrieved content.")

# User input
user_query = st.text_input("🔍 Ask a question:", "")

if user_query:
    st.write("⏳ Retrieving relevant document sections...")
    answer = ask_document(user_query)

    st.subheader("💡 AI Answer:")
    st.write(answer)

    # Show retrieved context for transparency
    st.subheader("📚 Retrieved Context:")
    st.write(retrieve_context(user_query))
