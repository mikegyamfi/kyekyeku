import re
import secrets
import json
import requests
from datetime import datetime
from decouple import config

ishare_map = {
    2: 50,
    4: 52,
    7: 2000,
    10: 3000,
    12: 4000,
    15: 5000,
    18: 6000,
    22: 7000,
    25: 8000,
    30: 10000,
    45: 15000,
    60: 20000,
    75: 25000,
    90: 30000,
    120: 40000,
    145: 50000,
    285: 100000,
    560: 200000
}


def ref_generator():
    now_time = datetime.now().strftime('%H%M%S')
    secret = secrets.token_hex(6)

    return f"KYE{now_time}KYE{secret}KU".upper()


def top_up_ref_generator():
    now_time = datetime.now().strftime('%H%M')
    secret = secrets.token_hex(1)

    return f"TOPUP-{now_time}{secret}".upper()


def send_bundle(user, receiver, bundle_amount, reference, amount):
    url = "https://www.geosams.com/controller/api/send_bundle/"

    payload = json.dumps({
        "phone_number": str(receiver),
        "amount": int(bundle_amount),
        "reference": str(reference),
        "network": "AT"
    })
    headers = {
        'Authorization': config("CONTROLLER_TOKEN"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response




