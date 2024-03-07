import requests

# Replace these with your client ID and client secret obtained from the Spotify Developer Dashboard
client_id = 'e5e16e1bba8545ae821ded70700f951f'
client_secret = '2517d6fb1e35439286936322fa6e0757'

def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_track_availability(track_id, token):
    track_url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    track_response = requests.get(track_url, headers=headers)
    track_data = track_response.json()

    if 'available_markets' in track_data:
        available_markets = track_data['available_markets']
        if len(available_markets) == 0:
            print("This track is not available in any market.")
        else:
            print(f"Track is available in {len(available_markets)} market(s).")
            print("This track is available in: " + ", ".join(available_markets) + "...")
    else:
        print("Invalid Track ID provided.")

if __name__ == '__main__':
    token = get_spotify_token(client_id, client_secret)
    spotify_track_id = input("Enter Spotify Track ID: ")  # Or extract it from a URL
    get_track_availability(spotify_track_id, token)
