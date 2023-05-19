import requests

def get_ada_response(user_input):
    ada_api_key = 'YOUR_ADA_API_KEY'  # Replace with your ADA API key
    ada_endpoint = 'https://api.ada.com/chat'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ada_api_key}'
    }

    data = {
        'text': user_input
    }

    response = requests.post(ada_endpoint, headers=headers, json=data)
    response_json = response.json()

    ada_response = response_json['text']['content']

    return ada_response

# Example usage
user_input = input("Enter your message: ")
ada_response = get_ada_response(user_input)
print("ADA's response:", ada_response)
