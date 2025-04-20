from flask import Blueprint, render_template, request, redirect
from app import mongo  # no circular import because it's imported after init in create_app()
from .models import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        try:
            user_data = request.form.to_dict(flat=False)
            user = User(user_data)

            # Save to MongoDB
           # mongo.db.survey_responses.insert_one(user.to_dict())

            if mongo.db is None:
                return "MongoDB not initialized", 500

            db = mongo.db  # Access after init_app has run
            db.survey_responses.insert_one(user.to_dict())

            # Save to CSV using internal method
            user.save_to_csv()

            return redirect('/')
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template('index.html')
