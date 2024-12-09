# AI-Powered Diet Assistant  

## Author: David Nyakawa  

## Table of Contents  

- [Introduction](#introduction)  
- [Methods and Results](#methods-and-results)  
- [Discussion](#discussion)  
- [Interactive Elements](#interactive-elements)  
- [Technical Risks and Mitigations](#technical-risks-and-mitigations)  

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
  _Response: "Here are a few options: almonds, Greek yogurt, apple slices with peanut butter."_  

- **Food Classifier Example**:  
  Input: Image of an apple  
  Output: _"Classified as Fruit."_  

## Discussion  

### Challenges  
1. **Chatbot Hallucinations**:  
   - Mitigation: Implemented strict domain filtering and rigorous testing with diverse queries.  
2. **Compute Limitations for Training**:  
   - Training the ResNet50 for 4 food categories required 4 hours. Scaling up to hundreds of categories would require significantly more resources. To address this, the project focuses on a smaller classification task while leveraging the chatbot's broader dietary insights.  
3. **Deployment Challenges**:  
   - Mitigation: Leveraged Docker for seamless deployment and scalability.  

### Lessons Learned  
- Fine-tuning existing models like ResNet50 saves time and resources compared to building models from scratch.  
- Containerization significantly simplifies the deployment process for AI-driven web applications.  

### Future Work  
- Expanding the food classifier to support additional categories.  
- Enhancing the chatbot's contextual understanding to provide even more personalized recommendations.  
- Integrating a mobile application for on-the-go dietary guidance.  

## Interactive Elements  

### Deployment Link  
The AI-Powered Diet Assistant is live and accessible here: [Healthy Way Deployment](https://healthywayapp3.azurewebsites.net/).  

## Technical Risks and Mitigations  

1. **Chatbot Hallucinations**:  
   - Mitigation: Implement strict domain filtering and test the chatbot with varied queries.  
2. **Compute Requirements for Training**:  
   - To train a ResNet50 for 4 different classes of food, it took approximately 4 hours. Training for hundreds of categories would be computationally expensive, so the project focuses on a smaller classification task while leveraging the chatbot for broader dietary guidance.  
3. **Deployment Challenges**:  
   - Mitigation: Use containerization (Docker) for seamless deployment and scalability.  
