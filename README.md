# self_awareness_assistant
This is your friendly assistant for self-awareness, which is a RAG app built as part of the LLM- Zoomcamp

## Running it 
We use pipenv for managing dependecies and Python 3.12.

Make sure you have pipenv installed. If not then :

```bash
pip install pipenv
```



# Self-Awareness Assistant

## Problem Description

Emotional intelligence (EI) plays an important role in how people understand themselves, manage their emotions, and interact with others. One of its fundamental components is **self-awareness** — the ability to recognize what we are feeling, understand the reasons behind those feelings, and identify how our emotions may influence our thoughts, decisions, and behavior.

However, developing self-awareness is not always easy. 

People may experience emotions such as stress, frustration, anxiety, or uncertainty without fully understanding where those feelings come from or how they affect their actions. Although there is a large amount of information available about emotional intelligence, finding relevant and practical guidance for a specific situation can be difficult. Traditional search engines may return large amounts of information without providing a focused answer to the user's question.

The **Self-Awareness Assistant** aims to address this problem by providing an interactive way for users to explore and improve their self-awareness. 

Instead of requiring the user to search through long articles or videos, the application allows them to ask questions in natural language and receive answers based on a curated knowledge base about emotional intelligence and self-awareness.

For example, a user can ask questions such as:

- *What does it mean to be self-aware?*
- *How can self-awareness help me make better decisions?*
- *Why should I pay attention to distressing emotions?*
- *How can I better understand what I am feeling?*
- *What can I do to improve my self-awareness?*

The project uses a **Retrieval-Augmented Generation (RAG)** approach. When a user asks a question, the system retrieves relevant information from the project's knowledge base and uses that information to generate a contextual answer. 

This allows the assistant to provide responses grounded in the project's curated sources rather than relying only on the language model's general knowledge.

The goal of the project is therefore to build a focused conversational assistant that helps users **learn about self-awareness, understand their emotions, and explore practical ways to develop greater self-awareness**.

## Data

The knowledge base contains **100 question-and-answer pairs** related to emotional intelligence, with a particular focus on self-awareness.

Each record contains three main fields:

```json
{
  "question": "How can self-awareness help you make better decisions?",
  "answer": "Recognizing your feelings helps you understand how they may be influencing your judgment and choices.",
  "video_id": "BqF50IuR3_c"
}