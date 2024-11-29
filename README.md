# AI-Powered Diet Assistant  

## Author: David Nyakawa  

---

## Project Overview  

### What  
The AI-Powered Diet Assistant is a web application that:  
1. **Answers diet-related questions**: Provides users with fast, reliable, and customized nutrition information via a chatbot.  
2. **Analyzes food images**: Classifies food items based on healthiness and provides a health rating on a scale of 1–5.  

### Why  
This project bridges a gap between health-conscious individuals and quick, AI-driven dietary insights. It enables users to understand and improve their eating habits with minimal effort, fostering healthier lifestyles.  

### How  
- **Chatbot**: Built with Retrieval-Augmented Generation (RAG) using the Langchain framework and Azure OpenAI.  
- **Image Classifier**: A convolutional neural network (CNN) trained on diverse food datasets to analyze and rate food healthiness.  

---

## Development Plan  

### MVP (Minimum Viable Product)  
- **Chatbot**: Answers general diet and nutrition-related questions.  
- **Image Classifier**: Rates food images on a healthiness scale of 1–5.  

### Stretch Goals  
1. Add a calorie estimation feature for uploaded food images.  
2. Integrate a searchable nutritional database.  

---

## Sprints  

### **Sprint 1: Data Collection (Week 1)**  
- **Objective**: Gather datasets for chatbot and image classifier.  
- **Tasks**:  
  - Identify and scrape nutrition-related documents for chatbot knowledge base.  
  - Curate diverse food image datasets, ensuring inclusion of multiple cuisines.  
- **Estimated Time**: 10 hours of active work.  

### **Sprint 2: Build Chatbot (Weeks 2–3)**  
- **Objective**: Develop a RAG-based chatbot for answering diet-related questions.  
- **Tasks**:  
  - Implement custom orchestration of RAG pipeline to limit out-of-domain queries.  
  - Address potential model hallucinations by refining prompt engineering.  
- **Estimated Time**: 20 hours of active work.  

### **Sprint 3: Train Image Classifier (Week 4)**  
- **Objective**: Train and evaluate a CNN for food image classification.  
- **Tasks**:  
  - Train CNN using curated datasets.  
  - Fine-tune the model for accuracy across diverse food types.  
- **Estimated Time**: 10 hours of active work.  

### **Sprint 4: Integration and Deployment (Week 5)**  
- **Objective**: Combine chatbot and classifier into a unified web app and deploy.  
- **Tasks**:  
  - Build a simple Flask-based interface.  
  - Deploy app to a cloud platform (e.g., AWS, Heroku).  
- **Estimated Time**: 5 hours of active work.  

---

## Technical Risks and Mitigations  

1. **Chatbot hallucinations**:  
   - Mitigation: Implement strict domain filtering and test the chatbot with varied queries.  

2. **Insufficient training data for the image classifier**:  
   - Mitigation: Source open datasets like Food-101 or build an augmented dataset.  

3. **Deployment challenges**:  
   - Mitigation: Use containerization (Docker) for seamless deployment and scalability.  

---
