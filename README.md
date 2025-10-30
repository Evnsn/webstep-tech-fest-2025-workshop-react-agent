# Webstep Tech Fest 2025 - Workshop: ReAct Agents
This repository is associated with a workshop held at WTF25.

## Workshop Setup
There are three ways to set up the workshop.

### 1. Run the workshop via the web
**Requirements:**
- None

**Steps:**  
The workshop app is hosted via Azure.  
1. Go to: [https://ca-wtf-25-app.proudbeach-3290d5a8.norwayeast.azurecontainerapps.io/](https://ca-wtf-25-app.proudbeach-3290d5a8.norwayeast.azurecontainerapps.io/)

### 2. Run locally via `docker-compose`
**Requirements:**
- Git
- Docker

**Steps:**
1. Clone the repository:  
   `git clone https://github.com/Evnsn/webstep-tech-fest-2025-workshop-react-agent.git`
2. Navigate to the cloned repository and run in terminal:  
   `docker-compose up -d`
3. Open `http://localhost:7860` in your browser.
4. Stop *docker-compose*:
   `docker-compose down`

### 3. Run in a Dev Container
**Requirements:**  
- Git
- Docker
- VS Code
- VS Code extension: *Dev Containers* by *Microsoft*

**Steps:**
1. Clone the repository:  
   `git clone https://github.com/Evnsn/webstep-tech-fest-2025-workshop-react-agent.git`
2. Open the local repository in VS Code.
3. Open the *Command Palette* (`Ctrl+Shift+P` on Windows) and run:  
   `Rebuild and Reopen in Container`
4. Open `http://localhost:7860` in your browser.

## Tech stack
A Python-based application utilizing UV for package management and Gradio to provide an intuitive user interface that integrates with the OpenAI API for intelligent agent interactions.

## Source code structure

- `/src`  
  Directory contains the main source code for the workshop application. 

   - `app.py`  
     Main file that runs the Gradio app and manages the agent's flow.

   - `agent.py`  
     Implements the core logic for the ReAct agent, including reasoning, acting, and interaction with the OpenAI API.

   - `tools.py`  
     Provides utility functions for the agent to call for performing tasks and fetch info.

   - `tools_description.json`
     Contains the definitions and parameters for the functions/tools available to the agent. This is what the OpenAI sees and reads.