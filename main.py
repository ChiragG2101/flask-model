from flask import Flask,jsonify
from model import main,load_recommend
app = Flask(__name__)

input_data={
        "call_id": "101",
        "company_name": "BluJay Solutions",
        "company_description": "BluJay Solutions provides transportation management and global trade network solutions.",
        "customer": {
            "offerings": "Their software optimizes logistics and customs processes, ensuring smooth and compliant cross-border operations.",
            "icp": {
            "target_industry": "Manufacturing, Retail, Logistics",
            "employee_count": "15000",
            "region": "India",
            "roles": "Manager",
            "min_pricing": "301847"
            }
        },
        "vendor": {
            "requirements": "Global Trade and Supply Chain Management Solutions",
            "ivp": {
            "vendor_industry": "Transportation, Logistics, Retail",
            "clients_count": "100",
            "region": "India",
            "max_pricing": "500000",
            "year_of_establishment": "3"
            }
        }
        }


@app.route("/")
def modelRun():
    result = main(input_data)
    return result




if __name__ == "__main__":
    app.run(debug=True)