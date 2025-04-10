from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Course database
course_database = {
    "programming": {
        "introductory": [
            {"name": "Python for Beginners", "duration": "8 weeks", "level": "Beginner", "topics": ["Basic Python", "Data Types", "Control Flow", "Functions"]},
            {"name": "JavaScript Fundamentals", "duration": "6 weeks", "level": "Beginner", "topics": ["Basic JS", "DOM Manipulation", "Events", "Async Programming"]}
        ],
        "intermediate": [
            {"name": "Advanced Python Development", "duration": "10 weeks", "level": "Intermediate", "topics": ["OOP", "Decorators", "Generators", "Testing"]},
            {"name": "Full Stack Web Development", "duration": "12 weeks", "level": "Intermediate", "topics": ["Frontend", "Backend", "Database", "APIs"]}
        ]
    },
    "data_science": {
        "introductory": [
            {"name": "Data Science Fundamentals", "duration": "8 weeks", "level": "Beginner", "topics": ["Python", "Statistics", "Data Analysis", "Visualization"]},
            {"name": "Machine Learning Basics", "duration": "10 weeks", "level": "Beginner", "topics": ["ML Concepts", "Scikit-learn", "Neural Networks", "Model Evaluation"]}
        ],
        "intermediate": [
            {"name": "Advanced Machine Learning", "duration": "12 weeks", "level": "Intermediate", "topics": ["Deep Learning", "NLP", "Computer Vision", "MLOps"]},
            {"name": "Big Data Analytics", "duration": "10 weeks", "level": "Intermediate", "topics": ["Hadoop", "Spark", "Data Warehousing", "ETL"]}
        ]
    },
    "design": {
        "introductory": [
            {"name": "UI/UX Design Fundamentals", "duration": "8 weeks", "level": "Beginner", "topics": ["Design Principles", "Wireframing", "Prototyping", "User Research"]},
            {"name": "Graphic Design Basics", "duration": "6 weeks", "level": "Beginner", "topics": ["Color Theory", "Typography", "Layout", "Adobe Tools"]}
        ],
        "intermediate": [
            {"name": "Advanced UI/UX Design", "duration": "10 weeks", "level": "Intermediate", "topics": ["Design Systems", "Accessibility", "Motion Design", "Design Thinking"]},
            {"name": "Brand Identity Design", "duration": "8 weeks", "level": "Intermediate", "topics": ["Brand Strategy", "Logo Design", "Visual Identity", "Brand Guidelines"]}
        ]
    }
}

def get_gemini_response(query):
    # Create a focused course recommendation prompt
    prompt = f"""
    You are a specialized course recommendation expert. Your primary focus is helping users find the right courses based on their interests, experience level, and career goals.
    
    User Query: "{query}"
    
    Available Course Information:
    {course_database}
    
    Please provide a detailed, helpful response that:
    1. Focuses specifically on course recommendations and learning paths
    2. Understands the user's experience level (beginner/intermediate)
    3. Recommends specific courses from the available options
    4. Explains why these courses would be beneficial for their goals
    5. Suggests a logical learning path or sequence
    6. Uses a friendly, engaging tone with emojis where appropriate
    
    If the query is not directly about courses, try to relate it back to relevant courses or learning opportunities.
    Format your response in a clear, easy-to-read way with proper spacing.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "I apologize, but I encountered an error processing your request. Please try again."

def get_relevant_courses(query):
    query = query.lower()
    relevant_courses = {}
    
    if any(word in query for word in ["programming", "coding", "developer", "software", "code"]):
        relevant_courses["programming"] = course_database["programming"]
    if any(word in query for word in ["data", "analytics", "machine learning", "ai", "artificial intelligence"]):
        relevant_courses["data_science"] = course_database["data_science"]
    if any(word in query for word in ["design", "ui", "ux", "graphic", "visual"]):
        relevant_courses["design"] = course_database["design"]
    
    return relevant_courses if relevant_courses else course_database

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '')
    
    # Get AI-generated response for any query
    response_message = get_gemini_response(user_message)
    
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)