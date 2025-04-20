from flask import Blueprint, render_template, request, redirect
from app import mongo  # ✅ import once at the top
from .models import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_data = request.form.to_dict(flat=False)
            user = User(user_data)

            # Check if MongoDB is initialized
            if mongo.db is None:
                return "MongoDB not initialized", 500

           # ✅ mongo.db is safe here because Flask app context exists
            mongo.db.survey_responses.insert_one(user.to_dict())
            #db.survey_responses.insert_one(user.to_dict())

            # Save to CSV using internal method
            user.save_to_csv()

            return redirect('/')
        
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template('index.html')
