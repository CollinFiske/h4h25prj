import requests
import json
from datetime import datetime

api_key = ""

def fetch_properties(beds, baths, min_price, max_price):
    
    url = "https://api.rentcast.io/v1/listings/rental/long-term"
    
    params = {
        "city": "Los Angeles",
        "state": "CA",
        "limit": 330,
        "bedrooms": beds,
        "bathrooms": baths
    }
    
    headers = {
        "Accept": "application/json",
        "X-Api-Key": api_key
    }
    
    matching_properties = []
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        
        properties = response.json()
        
        for prop in properties:
            if 'price' in prop and min_price <= prop['price'] <= max_price:
                property_info = {}
                
                # Add available fields to property_info
                if 'formattedAddress' in prop:
                    property_info['address'] = prop['formattedAddress']
                
                if 'bedrooms' in prop:
                    property_info['bedrooms'] = prop['bedrooms']
                
                if 'bathrooms' in prop:
                    property_info['bathrooms'] = prop['bathrooms']
                
                if 'squareFootage' in prop:
                    property_info['square_footage'] = prop['squareFootage']
                
                if 'latitude' in prop and 'longitude' in prop:
                    property_info['coordinates'] = (prop['latitude'], prop['longitude'])
                
                if 'price' in prop:
                    property_info['price'] = prop['price']
                
                matching_properties.append(property_info)

        return matching_properties

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return []
