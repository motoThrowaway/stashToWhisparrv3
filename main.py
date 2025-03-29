import requests

# 🔹 Whisparr API Config
WHISPARR_BASE_URL = "YOUR URL HERE"
WHISPARR_API_KEY = "YOUR API KEY HERE"

# 🔹 Headers for Whisparr API
WHISPARR_HEADERS = {"X-Api-Key": WHISPARR_API_KEY, "Content-Type": "application/json"}

# 🔹 List of Stash IDs to monitor
def read_ids_from_file(file_path):
    """Read stash IDs from a text file."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def fetch_whisparr_movies():
    """Fetch all movies in Whisparr"""
    response = requests.get(f"{WHISPARR_BASE_URL}/api/v3/movie", headers=WHISPARR_HEADERS)
    return response.json() if response.ok else None


def check_scene_in_whisparr(stash_id):
    """Check if a scene (movie) with the given stash ID exists in Whisparr"""
    movies = fetch_whisparr_movies()
    if not movies:
        return None

    for movie in movies:
        if "stashId" in movie and movie["stashId"] == stash_id:
            return movie  # Scene exists

    return None  # Scene not found


def add_scene_to_whisparr(stash_id):
    """Add a new scene to Whisparr"""
    payload = {
        "title": "Added via Python Script",
        "foreignId": stash_id,
        "stashId": stash_id,
        "monitored": False,
        "qualityProfileId": 1,
        "rootFolderPath": "/media/lane/storage/whisparr/sv3",
        "tags": [1],
        "addOptions": {"monitor": "none", "searchForMovie": False},
    }
    response = requests.post(f"{WHISPARR_BASE_URL}/api/v3/movie", headers=WHISPARR_HEADERS, json=payload)
    return response.json() if response.ok else None


def monitor_scene(whisparr_id, monitor=True):
    """Monitor or unmonitor a scene in Whisparr"""
    movie = requests.get(f"{WHISPARR_BASE_URL}/api/v3/movie/{whisparr_id}", headers=WHISPARR_HEADERS).json()

    payload = {
        "title": movie["title"],
        "foreignId": movie["foreignId"],
        "stashId": movie["stashId"],
        "monitored": monitor,
        "qualityProfileId": movie["qualityProfileId"],
        "rootFolderPath": movie["rootFolderPath"],
        "tags": movie["tags"],
        "path": movie["path"],
    }

    response = requests.put(f"{WHISPARR_BASE_URL}/api/v3/movie/{whisparr_id}", headers=WHISPARR_HEADERS, json=payload)
    return response.json() if response.ok else None


def main():
    """Main function to check and manage stash scenes in Whisparr"""
    stash_ids = read_ids_from_file('idsToMonitor.txt')
    for stash_id in stash_ids:
        print(f"\n🔍 Checking Stash ID: {stash_id}")

        scene = check_scene_in_whisparr(stash_id)
        if not scene:
            print("⚠️ Scene not found in Whisparr, adding it...")
            scene = add_scene_to_whisparr(stash_id)
            if scene:
                print("✅ Scene added successfully!")
            else:
                print("❌ Failed to add scene.")
                continue

        whisparr_id = scene["id"]

        # Check if monitored
        if scene["monitored"]:
            print("👁️ Scene is currently monitored.")
        else:
            print("➕ Monitoring scene...")
            monitor_scene(whisparr_id, monitor=True)
            print("✅ Scene is now monitored.")

        # Wait a bit before checking the next stash ID
        #time.sleep(2)


if __name__ == "__main__":
    main()
