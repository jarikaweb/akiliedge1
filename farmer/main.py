from flask import Flask, request
import africastalking

# Initialize the Flask app
app = Flask(__name__)

# Africa's Talking credentials
username = "sandbox"  # For sandbox, it's usually 'sandbox'
api_key = "atsk_540abf0e247c0d7d9718250124230967b03fd71d8752a5ab53d149f4812e67eccbbdb8f5"

# Initialize the Africa's Talking SDK
africastalking.initialize(username, api_key)

# Define the SMS service (if you need SMS functionality later)
sms = africastalking.SMS

# Index route to serve the homepage
@app.route('/')
def index():
    return """
    <h1>Welcome to Farmer's Hub USSD System</h1>
    <p>Use the USSD code to access real-time weather info, marketplaces, and products like fertilizer.</p>
    <p>This platform helps farmers get quick access to crucial information through USSD.</p>
    <p><b>Dial the USSD code to access services.</b></p>
    """

# Handle USSD requests
@app.route('/ussd', methods=['POST'])
def ussd():
    # Get the necessary data from the USSD request
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", None)

    # Handle the USSD session progression based on user input
    if text == "":
        # Initial Menu
        response = "CON Welcome to Farmer's Hub\n"
        response += "1. Weather Info\n"
        response += "2. Marketplaces\n"
        response += "3. Products (Fertilizer, Seeds)\n"
        response += "4. Contact Farmer\n"
    elif text == "1":
        # Simulating weather information
        response = "END Current weather: Sunny 27°C\n"
    elif text == "2":
        # Display list of marketplaces
        response = "END Marketplaces:\n1. Nairobi Market\n2. Eldoret Market\n"
    elif text == "3":
        # Display list of products
        response = "END Available Products:\n1. Fertilizer\n2. Seeds\n"
    elif text == "4":
        # Simulate connecting the user to a farmer (you can use the Voice API for calls)
        response = "END You will be connected to a farmer shortly."
    else:
        response = "END Invalid option. Please try again."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
