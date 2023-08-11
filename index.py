import requests
import json
import click
from classes import MobileFood 
from urllib.parse import urlparse, quote




  
def print_response(response):
    print(response)
    content = response.json()
    for entry in content:
        items = MobileFood.from_dict(entry)
        print(items)

def attach_params(applicant_name: str, status: str, street_name: str,latitude: str, longitude: str)-> dict:
    params = {}
    if applicant_name:
        params['applicant'] = applicant_name
    if street_name:
        params['address'] = street_name
    if latitude and longitude:
        params['latitude'] = latitude
        params['longitude'] = longitude
        params['status'] = 'APPROVED'
    if status:
        params['status'] = status
    return params

@click.command()
@click.option('--applicant-name', type=str, required=False)
@click.option('--status', type=str,required=False)
@click.option('--street_name', type=str,required=False)
@click.option('--latitude', type=str,required=False)
@click.option('--longitude', type=str,required=False)
def main(applicant_name: str, status: str, street_name: str,latitude: str, longitude: str) -> None:

    url = "https://data.sfgov.org/resource/rqzj-sfat.json"
    
    params = attach_params(applicant_name, status, street_name, latitude, longitude)
    response = requests.get(url, params=params)
    print_response(response)

if __name__ == '__main__':
    main()