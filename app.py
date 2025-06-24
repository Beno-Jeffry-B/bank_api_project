import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from models import db,Bank

load_dotenv() 

app = Flask(__name__)
load_dotenv()
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD").replace("@", "%40").replace("#", "%23") 
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return jsonify({"message": "Bank API is live!"})

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    result = [{"id": bank.id, "name": bank.name} for bank in banks]
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)


    
