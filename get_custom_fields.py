import requests
import json

subdomain = input['subdomain']
sub_id = input['sub_id']

def get_custom_fields(subdomain, sub_id):
    subdomain = subdomain 
    sub_id = sub_id
    url = "https://{subdomain}.chargify.com/subscriptions/{subscription_id}/metadata.json".format(subdomain=subdomain, subscription_id=sub_id)
    headers = {
    'content-type': "application/json",
    'authorization': "Basic API-KEY-GOES-HERE"
    }
    response = requests.request("GET", url, headers=headers)
    response_dict = response.json()
    return response_dict

def make_response_dict(subdomain, sub_id):
    field_dict = {}
    resp_dict = get_custom_fields(subdomain, sub_id)
    for i in range(len(resp_dict['metadata'])):
        field_dict[resp_dict['metadata'][i]['name']] = resp_dict['metadata'][i]['value']
    return field_dict

return make_response_dict(subdomain, sub_id)
