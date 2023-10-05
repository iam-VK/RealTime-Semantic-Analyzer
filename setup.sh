#!/bin/bash
echo Setting up virtual environment
python3 -m venv venv
source venv/bin/activate

echo Installing git-lfs
./setup_dependencies/git-lfs-3.4.0/install.sh

echo Downloading NLP models from HuggingFace Hub
git clone https://huggingface.co/SamLowe/roberta-base-go_emotions
git clone https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

echo Installing Python libraries
pip install -r requirements.txt

echo Setting up Web application
cd frontend
npm install