import requests

def fetch_json(url, params=None, headers=None, timeout=10):
    """
    Generic helper to fetch JSON from a URL.

    Returns:
        dict: Parsed JSON on success
        None: On failure (prints error)
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"[API Client] Request error: {e}")
    except ValueError as e:
        print(f"[API Client] JSON decode error: {e}")
    return None
