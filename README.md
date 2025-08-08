# Langchain_Advisor

A flexible AI-powered advisor built using the LangChain framework.

## Overview
Langchain_Advisor uses the LangChain framework to build conversational agents. It processes user queries, maintains conversational context, and executes logic through modular agent workflows.

## Project Structure
- `main.py`: Entry point that handles user input, invokes LLMs, and orchestrates agent workflows.
- `llm_utils.py`: Utilities for setting up LLMs and interacting with them.
- `graph.py`: (Optional) Defines task flows or chained logic (if applicable).
- `state.py`: Manages conversation or application state, such as session memory.
- `nodes/`: Directory for modular components or tools used within agent chains.
- `requirements.txt`: Defines required dependencies.
- `README.md`: Documentation (this file).

## Features
- Agent-driven conversational workflows using LangChain.
- Contextual memory across conversations.
- Extensible structure for adding custom tools or logic.
- Clean modular design for maintainability.

## Installation

```bash
git clone git@github.com:jyotirmoybanerjiportfolio771/Langchain_Advisor.git
cd Langchain_Advisor
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
