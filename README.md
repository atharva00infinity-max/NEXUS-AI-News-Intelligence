NEXUS AI — News Intelligence

An AI-powered news summarization application built using Python, Streamlit, Hugging Face Transformers and a fine-tuned T5 model.

NEXUS AI uses a fine-tuned sequence-to-sequence model to generate concise summaries of news content through a simple web interface.

Features

- AI-powered news summarization
- Fine-tuned T5 transformer model
- Hugging Face model integration
- Interactive Streamlit web interface
- Remote model loading from Hugging Face Hub

Tech Stack

- Programming Language: Python
- Frontend: Streamlit
- Model Architecture: T5
- Deep Learning: Hugging Face Transformers
- Model Hosting: Hugging Face Hub

Model

The fine-tuned model is hosted separately on Hugging Face.

Model Repository:
https://huggingface.co/atharva1405/NEXUS-News-Summarizer

The application loads the model directly from Hugging Face, avoiding the need to store large model checkpoints inside the GitHub repository.

Installation & Setup

1. Clone the repository

git clone https://github.com/atharva00infinity-max/NEXUS-AI-News-Intelligence.git

2. Navigate to the project directory

cd NEXUS-AI-News-Intelligence

3. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Run the application

python -m streamlit run app/app.py

The application will be available at:

http://localhost:8501

Note: The first launch may take longer because the fine-tuned model needs to be downloaded from Hugging Face.

Project Structure

NEXUS-AI-News-Intelligence/
│
├── app/
│   └── app.py
│
├── notebook/
│   └── models/
│
├── requirements.txt
├── .gitignore
└── README.md

Note: Large model checkpoints are hosted separately on Hugging Face and are not included in this GitHub repository.

Future Scope

- Deployment as a publicly accessible web application
- Further improvements in summarization quality
- Additional news analysis capabilities

Author

Atharva

GitHub: https://github.com/atharva00infinity-max

Hugging Face: https://huggingface.co/atharva1405