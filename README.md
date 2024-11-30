# AI-Powered Diet Assistant  

## Author: David Nyakawa  

---

## Project Overview  

### What  
The AI-Powered Diet Assistant is a web application that:  
1. **Answers diet-related questions**: Provides users with fast, reliable, and customized nutrition information via a chatbot.  
2. **Food Ratings**: Classifies food items based on healthiness and provides a health rating on a scale of 1–5 & gives estimated calories per serving.  

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

2. **Insufficient training data for the image classifier**:  
   - Mitigation: Source open datasets like Food-101 or build an augmented dataset.  

3. **Deployment challenges**:  
   - Mitigation: Use containerization (Docker) for seamless deployment and scalability.  

---
