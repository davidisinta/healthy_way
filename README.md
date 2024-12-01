# AI-Powered Diet Assistant  

## Author: David Nyakawa  

---

## Project Overview  

### What  
The AI-Powered Diet Assistant is a web application that:  
1. **Answers diet-related questions**: Provides users with fast, reliable, and customized nutrition information via a chatbot.  
2. **Food Identification**: Classifies food items into 4 different classes based on fine tuning the ResNet50 model.  

### Why  
This project bridges a gap between health-conscious individuals and quick, AI-driven dietary insights. It enables users to understand and improve their eating habits with minimal effort, fostering healthier lifestyles.  

### How  
- **Chatbot**: Built with Retrieval-Augmented Generation (RAG) using the Langchain framework and Azure OpenAI.  

---

## Development Plan  

### MVP (Minimum Viable Product)  
- **Chatbot**: Answers general diet and nutrition-related questions.  
---

## Technical Risks and Mitigations  

1. **Chatbot hallucinations**:  
   - Mitigation: Implement strict domain filtering and test the chatbot with varied queries.  

2. **Lots of compute required to train a food classifier from scratch**:  
   - To train a ResNet 50 to be able to categorize 4 different classes of foods, it took approximately 4 hours, so to train for pretty much hundreds of thousands of foods it would take up plenty of time. So I just built a notebook that can distinguish for 4 different types of foods and kept the QnA interface to the chatbot. The chatbot can still tell you which foods are healthy. 

3. **Deployment challenges**:  
   - Mitigation: Use containerization (Docker) for seamless deployment and scalability.  

---
