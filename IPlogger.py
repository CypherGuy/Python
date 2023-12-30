from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr
    print(f"IP Address: {ip_address}")
    response = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key=3403b50376be48109fc0f90e94d173fe&ip_address={ip_address}")
        
    data = response.json()
    country = data['city']
    if country is None:
        country = "Notfound"
    with open('log.txt', "a") as file:
        file.write(f"\nIP: {ip_address} Country: {country}")

    return f"Your IP address has been logged as {ip_address}."

if __name__ == '__main__':
    app.run()