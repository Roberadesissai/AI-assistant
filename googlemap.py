import googlemaps


def where_to_go(tts):
    # Load API key from file
    with open("google_maps_api_key.txt", "r") as f:
        api_key = f.read()

    # Create client object
    gmaps = googlemaps.Client(key=api_key)

    # Ask the user where they want to go
    tts.speak("Where would you like to go?")
    destination = input("Where would you like to go? ")

    # Use the Google Maps API to find the location
    geocode_result = gmaps.geocode(destination)

    # Check if a location was found
    if len(geocode_result) == 0:
        tts.speak("I'm sorry, I could not find that location.")
        print("I'm sorry, I could not find that location.")
        return

    # Get the latitude and longitude of the location
    location = geocode_result[0]['geometry']['location']

    # Tell the user the name and address of the location
    name = geocode_result[0]['formatted_address']
    tts.speak("I found " + name + " on the map.")
    print("I found " + name + " on the map.")

    return location




def find_nearby_places(api_key, place_type):
    gmaps = googlemaps.Client(key=api_key)

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Use the latitude and longitude of the address to search for nearby places
    location = geocode_result[0]['geometry']['location']
    nearby_places_result = gmaps.places_nearby(location=location, radius=10000, type=place_type)

    # Get the name and address of the first result
    if len(nearby_places_result['results']) > 0:
        name = nearby_places_result['results'][0]['name']
        address = nearby_places_result['results'][0]['vicinity']
        return f"The nearest {place_type} is {name} at {address}"
    else:
        return f"No {place_type} found nearby"