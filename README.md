# Real-Time Semantic Analyzer and Corrector for Negative Sentences

## Abstract

This project introduces a real-time semantic analyzer and corrector for negative sentences, integrating a pretrained NLP model from Hugging Face's Transformers library. The objective is to develop a Python-based API that seamlessly connects with a ReactJS web application, allowing users to input text for emotion analysis, correction, and transformation. The project empowers users to analyze and modify text in various forms, including sentences, letters, and emails, by customizing the emotional tone of the output text.

## Project Overview

In this project, we leverage the power of modern NLP technology to create a dynamic and user-friendly platform that enhances written communication. The following modules and features are integral to the system:

1. **Emotion Analysis:**
   - Utilizing a pretrained NLP model, the system accurately detects and classifies the emotional tone of user-provided text.
   - Users receive real-time feedback on the emotional content of their input, helping them better understand the sentiment conveyed.

2. **Text Correction:**
   - The system includes a semantic analysis component to identify and correct negative sentences, improving clarity and conciseness.
   - Corrections are processed promptly, guaranteeing a seamless and efficient user experience.

3. **Emotion Transformation:**
   - Users have the option to customize the emotional tone of their text.
   - The pretrained model can transform input text to convey a different emotion, as per the user's preference, while maintaining coherence and readability.

4. **ReactJS Web Application:**
   - The frontend is built on ReactJS, providing an interactive and responsive user interface.
   - Users can easily input text, choose the desired emotion, and view the transformed output in real-time.

5. **Online Hosting:**
   - The web application is hosted online, ensuring accessibility to users from anywhere with an internet connection.

## Installation

**Pre-requisites**
   > - python3 
   > - pip
   > - python venv (virtual environment support)

**Clone the repo**

````bash
git clone https://github.com/iam-VK/Sematic-analysis-and-corrector-for-negative-sentence.git
cd Sematic-analysis-and-corrector-for-negative-sentence
````

**Download Dependencies and libraries**
```bash
sudo ./setup.sh 
```
>This process will take time to complete and requires good internet connectivity

**Run the setup script**
```bash
sudo ./run.sh 
```
**Front-end Web page**

The Front-end is not hosted currently so as of now the html file has to be manually be opened from the path using browser.
````
 /frontend/index.html 
````