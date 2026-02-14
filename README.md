# Expense Tracking System

This project is an expense Tracking system that consists of a Streamlit frontend application and a FastAPI backend server.

## 📷 App Interface
<p align="center">
  <img src="images/image2.jpg" alt="Image 2" width="300"/>
  <img src="images/image1.jpg" alt="Image 1" width="300"/>
  <img src="images/image3.jpg" alt="Image 3" width="300"/>
</p>

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Expense_Tracking_System.git
   cd Expense_Tracking_System
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```




