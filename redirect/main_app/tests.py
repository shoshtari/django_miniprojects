from django.test import TestCase
import requests

# Create your tests here.
def url_shorting(url):
    destination_url = r"http://localhost:8000/shorter/"
    data = {
        "full_url" : url
    }
    resp = requests.post(url = destination_url, json = data)
    return resp
def url_redirecting(key):
    destination_url = f"http://localhost:8000/redirect_user/{key}"
    resp = requests.get(url = destination_url)
    return resp
def test(query):
    resp = url_shorting(query)
    key = resp.json()['short_url']
    resp = url_redirecting(key)
    return resp