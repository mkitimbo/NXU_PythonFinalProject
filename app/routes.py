from flask import Blueprint, render_template, request, redirect
from .models import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    from app import mongo  # ✅ import inside the function to avoid early import before init_app

    if request.method == 'POST':
        try:
            user_data = request.form.to_dict(flat=False)
            user = User(user_data)

            # Check if MongoDB is initialized
            if mongo.db is None:
                return "MongoDB not initialized", 500

            # Save to MongoDB
            db = mongo.db
            db.survey_responses.insert_one(user.to_dict())

            # Save to CSV using internal method
            user.save_to_csv()

            return redirect('/')
        
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template('index.html')
