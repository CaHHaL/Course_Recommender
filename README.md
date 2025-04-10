# AI Course Advisor

A Flask-based web application that uses Google's Gemini AI to provide personalized course recommendations and educational guidance.

## Features

- Interactive chat interface with AI
- Personalized course recommendations
- Educational guidance and support
- Course database with detailed information

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```
     source venv/bin/activate
     ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the root directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Type your questions or requests in the chat interface
2. The AI will respond with relevant course recommendations and educational guidance
3. You can ask about:
   - Course recommendations
   - Educational paths
   - Career guidance
   - Learning resources
   - And more!

## Technologies Used

- Flask
- Google Gemini AI
- HTML/CSS/JavaScript
- Python-dotenv for environment management 