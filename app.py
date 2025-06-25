import os
from dotenv import load_dotenv
from flask import Flask, jsonify,request
from models import db,Bank,Branch

load_dotenv() 

app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:+?yryWcN66_89*M@db.afvbqqpqokxpelfxpfem.supabase.co:5432/postgres"

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

@app.route('/branches/<ifsc>', methods=['GET'])
def get_branch_by_ifsc(ifsc):
    branch = Branch.query.filter_by(ifsc=ifsc).first()

    if not branch:
        return jsonify({"error": "Branch not found"}), 404

    result = {
        "ifsc": branch.ifsc,
        "bank_id": branch.bank_id,
        "branch": branch.branch,
        "address": branch.address,
        "city": branch.city,
        "district": branch.district,
        "state": branch.state,
        "bank_name": branch.bank.name  
    }

    return jsonify(result), 200

# Search by bank and city by implementing joins
@app.route('/branches', methods=['GET'])
def get_branches():
    bank_name = request.args.get('bank_name')
    city = request.args.get('city')

    if not bank_name or not city:
        return jsonify({"error": "Both 'bank_name' and 'city' query parameters are required."}), 400

    # Performing JOIN query
    branches = Branch.query.join(Bank).filter(
        Bank.name.ilike(bank_name),
        Branch.city.ilike(city)
    ).all()

    result = []
    for b in branches:
        result.append({
            "ifsc": b.ifsc,
            "branch": b.branch,
            "address": b.address,
            "city": b.city,
            "district": b.district,
            "state": b.state,
            "bank_name": b.bank.name
        })

    return jsonify(result), 200



if __name__ == "__main__":
    app.run()


    
