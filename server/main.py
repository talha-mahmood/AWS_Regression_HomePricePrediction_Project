import requests

url = 'http://127.0.0.1:5000/predict_home_price'
data = {
    'location': '1st Phase JP Nagar',
    'total_sqft': 1000,
    'bhk': 2,
    'bath': 2
}


response = requests.post(url, json=data)

print(response.text)