from flask import Flask, request, render_template_string

# Initialize the Flask app
app = Flask(__name__)

# Index route to serve the homepage
@app.route('/')
def index():
    return render_template_string('''
        <h1>Welcome to Farmer's Hub USSD System</h1>
        <p>This platform helps farmers get quick access to crucial information through USSD.</p>
        <p><b>Dial the USSD code *384*17040# on your phone, or use the form below to simulate USSD inputs.</b></p>
        <a href="/ussd-input">Simulate USSD Input</a><br><br>
        <h3>Additional Functionality:</h3>
        <a href="/weather">Check Weather</a><br>
        <a href="/marketplaces">View Marketplaces</a><br>
        <a href="/products">View Available Products</a><br>
        <a href="/contact-farmer">Contact a Farmer</a>
    ''')

# USSD home page with a text box for input
@app.route('/ussd-input', methods=['GET', 'POST'])
def ussd_input():
    if request.method == 'POST':
        ussd_code = request.form.get('ussd_code')

        # Simulate a USSD session based on the user's input
        if ussd_code == "*384*17040#":
            response = "CON Welcome to Farmer's Hub\n"
            response += "1. Weather Info\n"
            response += "2. Marketplaces\n"
            response += "3. Products (Fertilizer, Seeds)\n"
            response += "4. Contact Farmer\n"
        elif ussd_code == "1":
            response = "END Current weather: Sunny 27°C\n"
        elif ussd_code == "2":
            response = "END Marketplaces:\n1. Nairobi Market\n2. Eldoret Market\n"
        elif ussd_code == "3":
            response = "END Available Products:\n1. Fertilizer\n2. Seeds\n"
        elif ussd_code == "4":
            response = "END You will be connected to a farmer shortly."
        else:
            response = "END Invalid option. Please try again."
        
        # Render the result on the same page
        return render_template_string('''
            <h1>USSD Response</h1>
            <p>{{ response }}</p>
            <a href="/ussd-input">Back</a>
        ''', response=response)

    # Render the input form
    return render_template_string('''
        <h1>Enter USSD Code</h1>
        <form method="POST">
            <label for="ussd_code">USSD Code:</label>
            <input type="text" name="ussd_code" placeholder="Enter USSD Code" required>
            <input type="submit" value="Submit">
        </form>
        <br>
        <a href="/">Go back to Home</a>
    ''')

# Check weather route
@app.route('/weather')
def weather():
    weather_info = "Sunny, 27°C"
    return render_template_string('''
        <h1>Weather Information</h1>
        <p>The current weather is: {{ weather_info }}</p>
        <a href="/">Go back to Home</a>
    ''', weather_info=weather_info)

# View marketplaces route
@app.route('/marketplaces')
def marketplaces():
    marketplace_list = [
        "1. Nairobi Market",
        "2. Eldoret Market",
        "3. Mombasa Market"
    ]
    return render_template_string('''
        <h1>Available Marketplaces</h1>
        <ul>
            {% for market in marketplace_list %}
            <li>{{ market }}</li>
            {% endfor %}
        </ul>
        <a href="/">Go back to Home</a>
    ''', marketplace_list=marketplace_list)

# View products route
@app.route('/products')
def products():
    product_list = [
        "1. Fertilizer",
        "2. Seeds",
        "3. Pesticides"
    ]
    return render_template_string('''
        <h1>Available Products</h1>
        <ul>
            {% for product in product_list %}
            <li>{{ product }}</li>
            {% endfor %}
        </ul>
        <a href="/">Go back to Home</a>
    ''', product_list=product_list)

# Contact farmer route
@app.route('/contact-farmer')
def contact_farmer():
    # Simulate contacting a farmer
    return render_template_string('''
        <h1>Contacting Farmer</h1>
        <p>You will be connected to a farmer shortly.</p>
        <a href="/">Go back to Home</a>
    ''')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
