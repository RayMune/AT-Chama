from flask import Flask, request

app = Flask(__name__)

# Sample list of member IDs and their savings
member_savings = {
    "12345678": 50000,
    "87654321": 25000,
    "11223344": 75000
}

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route("/ussd", methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    print("phone number", phone_number)

    if text == '':
        response = "CON Welcome to the Chama-Bot, We are a platform that streamlines informal sacco services, whilst utilizing AI to bring services closer to Mwananchi \n"
        response += "1. Choose your Chama \n"
        response += "2. Learn about Chamas/Table Banking in Kenya \n"

    elif text == '1':
        response = "CON Please Choose your specific Chama \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    # ... (other code blocks omitted for brevity)

    elif text == '1*1':
        response = "CON Welcome to Chania Open Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*1*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*1*1*'):
        id_number = text.split('*')[3]
        if len(id_number) != 8 or not id_number.isdigit():
            response = "END Invalid ID number. Please try again."
        else:
            response = f"END Thank you for providing your ID number {id_number}. You have successfully registered for the AfricasTalking Open Chama."
        return response

    elif text == '1*1*2':
        response = "CON Please Choose your specific chama  \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*2':
        response = "CON Welcome to Utumishi Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*2*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*2*1*'):
        id_number = text.split('*')[3]
        if id_number in member_savings:
            response = f"END Your total savings in the Utumishi Chama is KES {member_savings[id_number]} \n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Utumishi Chama first. \n"
        return response

    elif text == '1*2*2':
        response = "CON Please Choose your specific Chama \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*3':
        response = "CON Welcome to Kibera Women Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*3*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*3*1*'):
        id_number = text.split('*')[3]
        # Assume the same member_savings dictionary for Kibera Women Chama
        if id_number in member_savings:
            response = f"END Your total savings in the Kibera Women Chama is KES {member_savings[id_number]}, the next meeting is on 1st April 2024 at Melissa Weru's House, You have a loan facility of Ksh 240,000 due in 90 Days. Current Chama co-ordinator is Felix Odwuor(07265753345) \n Thank you. \n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Kibera Women Chama first. \n"
        return response

    elif text == '1*3*2':
        response = "CON Please Choose your specific Region/county \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*4':
        response = "CON Welcome to Muthaiga Residents Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*4*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*4*1*'):
        id_number = text.split('*')[3]
        # Assume the same member_savings dictionary for Muthaiga Residents Chama
        if id_number in member_savings:
            response = f"END Your total savings in the Muthaiga Residents Chama is KES {member_savings[id_number]} \n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Muthaiga Residents Chama first. \n"
        return response

    elif text == '1*4*2':
        response = "CON Please Choose your specific Region/county \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*1':
        response = "CON Welcome to Chania Open Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*1*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*1*1*'):
        id_number = text.split('*')[3]
        if len(id_number) != 8 or not id_number.isdigit():
            response = "END Invalid ID number. Please try again."
        else:
            response = f"END Thank you for providing your ID number {id_number}. You have successfully registered for the Chania Open Chama."
        return response

    elif text == '1*1*2':
        response = "CON Please Choose your specific ch \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*2':
        response = "CON Welcome to Utumishi Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*2*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*2*1*'):
        id_number = text.split('*')[3]
        if id_number in member_savings:
            response = f"END Your total savings in the Utumishi Chama is KES {member_savings[id_number]} , The next meeting is scheduled for Monday 30th March at Patrick Obonya's official residence\n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Utumishi Chama first. \n"
        return response

    elif text == '1*2*2':
        response = "CON Please Choose your specific Chama \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*3':
        response = "CON Welcome to Kibera Women Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*3*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*3*1*'):
        id_number = text.split('*')[3]
        # Assume the same member_savings dictionary for Kibera Women Chama
        if id_number in member_savings:
            response = f"END Your total savings in the Kibera Women Chama is KES {member_savings[id_number]} , The next meeting is scheduled for Wednesday 18th April at Melissa Weru's official residence\n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Kibera Women Chama first. \n"
        return response

    elif text == '1*3*2':
        response = "CON Please Choose your specific Chama \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

    elif text == '1*4':
        response = "CON Welcome to Muthaiga Residents Chama, We appreciate your interest \n"
        response += "1. Enter ID number \n"
        response += "2. Go back \n"

    elif text == '1*4*1':
        response = "CON Please enter your valid national ID number \n"

    elif text.startswith('1*4*1*'):
        id_number = text.split('*')[3]
        # Assume the same member_savings dictionary for Muthaiga Residents Chama
        if id_number in member_savings:
            response = f"END Your total savings in the Muthaiga Residents Chama is KES {member_savings[id_number]}, Next chama meeting is scheduled for 28-04-2024 at Brian Lokipim's official Residence \n"
        else:
            response = "END Your ID number is not found in our records. Please sign up for the Muthaiga Residents Chama first. \n"
        return response

    elif text == '1*4*2':
        response = "CON Please Choose your specific Region/county \n"
        response += "1. Chania Open Chama \n"
        response += "2. Utumishi Chama \n"
        response += "3. Kibera Women Chama \n"
        response += "4. Muthaiga Residents Chama \n"

  
    elif text == '2':
        response = "CON Please enter your phone number to learn about Chamas/Table Banking in Kenya \n"

    elif text.startswith('2*'):
        user_phone_number = text.split('*')[1]
        if len(user_phone_number) != 10 or not user_phone_number.isdigit():




          
            response = "END Invalid phone number. Please try again."
        else:
            response = f"END Thank you for providing your phone number ({user_phone_number}). To get detailed information about Chamas/Table Banking in Kenya, kindly visit www.chamaskenya.org \n"
        return response

    else:
        response = "CON Invalid input, please try again"

    print(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)