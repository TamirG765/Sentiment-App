# Sentiment Analysis Using Hugging Face Model 🤗

This project showcases a sentiment analysis application developed using modern machine learning and web development tools. The main components of the project include a simple frontend app built with Streamlit, a backend powered by FastAPI, and a small research notebook for model exploration and fine-tuning. This project demonstrates my skills in integrating various technologies and my ability to perform end-to-end machine learning tasks.

## Project Overview

1. **Frontend**: A user-friendly web application built with Streamlit to provide an interactive interface for sentiment analysis.
2.	**Backend**: A robust backend server developed using FastAPI to handle API requests and serve the sentiment analysis model.
3.	**Model Research and Fine-Tuning**: A Jupyter notebook for researching and comparing different sentiment analysis models, including models in English and Hebrew. The English model was fine-tuned using the IMDB dataset and published on Hugging Face Hub.

## How to Run The Project

Use python version `3.12.3`.

1. Clone the repo:

`git clone https://github.com/TamirG765/sentiment-app.git
cd sentiment-app`

2. Install dependencies:

`pip install -r requirements.txt`

3. Run Streamlit app:

`cd streamlit_app
streamlit run streamlit_app.py`

4. Run FastAPI Server:

`cd fatapi_app
uvicorn fastapi_app:app --reload`

Hope you guys like it! 🦾
