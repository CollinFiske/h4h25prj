from flask import Flask, render_template, request
from rentals import fetch_properties
from aiStuff import getAIStuff

app = Flask(__name__)

propertiesGlobal = []

@app.route('/landingPage')
def landing_page():
    return render_template('landingpage.html')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check which form was submitted
        if 'form_type' in request.form:
            if request.form['form_type'] == 'ai_request':
                address = request.form.get('aiResponseAddy')
                price = request.form.get('aiResponsePrice')
                #print(f"AI Request - Address: {address}, Price: {price}")
                ai_response = getAIStuff(address, price) if address and price else []
                propertiesLocal = propertiesGlobal
                return render_template("index.html", properties=propertiesLocal, ai_response=ai_response)
            
            elif request.form['form_type'] == 'property_search':
                # Initialize default values
                beds = 1
                baths = 1
                min_price = 100000
                max_price = 0
                
                try:
                    if request.form.get("beds"):
                        beds = int(request.form["beds"])
                    if request.form.get("baths"):
                        baths = int(request.form["baths"])
                    if request.form.get("min_price"):
                        min_price = int(request.form["min_price"])
                    if request.form.get("max_price"):
                        max_price = int(request.form["max_price"])
                except ValueError:
                    pass
                
                properties = fetch_properties(beds, baths, min_price, max_price)
                return render_template("index.html", properties=properties, ai_response=[])
    
    # Default page load
    return render_template("index.html", properties=[], ai_response=[])


if __name__ == "__main__":
    app.run(debug=True)