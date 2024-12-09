# AI-Powered Diet Assistant  

## Author: David Nyakawa  

## Table of Contents  

- [Introduction](#introduction)  
- [Methods and Results](#methods-and-results)  
- [Discussion](#discussion)  
- [Interactive Elements](#interactive-elements)
- [Running Locally](#running-locally)

## Introduction  

### Overview  
Healthy Way is an AI-Powered Diet Assistant designed to provide users with personalized nutrition guidance. By combining cutting-edge AI technologies, this tool empowers individuals to make healthier dietary choices with minimal effort. Its primary features include a chatbot for answering diet-related queries and a food classifier that identifies food items based on fine-tuned AI models.  

### Significance  
With increasing awareness of the importance of healthy eating, there is a growing demand for tools that simplify nutritional planning. The AI-Powered Diet Assistant bridges this gap by offering an accessible, AI-driven approach to understanding dietary habits and fostering a healthier lifestyle.  

## Methods and Results  

### Methods  
1. **Chatbot**:  
   - Built using **Retrieval-Augmented Generation (RAG)** with the **LangChain framework** and **Azure OpenAI services**.  
   - Offers reliable and customized answers to diet and nutrition questions.  
2. **Food Classifier**:  
   - Utilizes a fine-tuned ResNet50 model to classify food items into 4 categories.  
   - Training Time: Approximately 9 hours for the chosen dataset.  

### Results  
1. **Chatbot**: Successfully answers user queries, providing dietary recommendations.  
2. **Food Classifier**: Accurately identifies and categorizes food items into the predefined classes.  

#### Sample Output  
- **Chatbot Example**:  
  _"What are some healthy snack options?"_  
  _Response: "Some healthy snack options include whole fruits, nuts, seeds, low-fat dairy products like yogurt and cheese, and vegetables. You can also consider whole grains, legumes such as beans and peas, and protein-rich foods like seafood, lean meats, and soy products. It's beneficial to eat a variety of these options to ensure a range of nutrients."_  

- **Food Classifier Example**:  
  Input: Image of an steak  
  Output: _"Classified as steak."_
  [Check out the jupyter notebook](food_classifier_complete.ipynb).  
  
  

## Discussion  

### Challenges  
1. **Chatbot Hallucinations**:  
   - Mitigation: Implemented strict domain filtering and rigorous testing with diverse queries.  
2. **Compute Limitations for Training**:  
   - Training the ResNet50 for 4 food categories required 9 hours. Scaling up to hundreds of categories would require significantly more resources. To address this, the project focuses on a smaller classification task while leveraging the chatbot's broader dietary insights.  

### Lessons Learned  
- Identifying bottlenecks like compute power early could be useful to help determine the scope of the project. 

### Future Work  
- Using a more advance pretrained image classifier to offload the work of having to fine tune a model significantly and just focus on rating the foods based on their categories. 
- Adding more data to the model so that it has more information to pull from when answering users diet related questions.

## Interactive Elements  

### Deployment Link  
The AI-Powered Diet Assistant is live and accessible here: [Healthy Way Deployment](https://healthywayapp3.azurewebsites.net/).  


## Running Locally 

### 0. Note

This chatbot uses Azure Open AI's GPT-4 base model and you will need a deployment for this model on Azure to be able to use the chatbot and run the app locally. Without this deployments your application will be unable to run. If you want to see a demo of the app, I suggest you use my deployed version [here](https://healthywayapp3.azurewebsites.net/). Otherwise if you are checking out this repo for development purposes, feel free to deploy the Azure resources and set up the necessary API keys to integrate with the application locally for development.

### 1. Clone the Repository

Clone this repository using the following command:

```bash
git clone https://github.com/davidisinta/healthy_way
```

### 2. Navigate to the Project Directory

```bash
cd healthy_way
```

### 3. Set Up a Virtual Environment

for macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

for Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Running the Application

```bash
uvicorn main:app --reload
```







