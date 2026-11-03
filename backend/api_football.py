
import os
import requests
from datetime import date

BASE_URL = "https://v3.football.api-sports.io"


def get_fixtures(match_date=None):
    """Recupera le partite di una data da API-Football."""

    api_key = os.getenv("API_FOOTBALL_KEY")

    if not api_key:
        raise RuntimeError(
            "Chiave API mancante: API_FOOTBALL_KEY"
        )

    if match_date is None:
        match_date = date.today().isoformat()

    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers={"x-apisports-key": api_key},
        params={"date": match_date},
        timeout=30,
    )

    response.raise_for_status()
    data = response.json()

    if data.get("errors"):
        raise RuntimeError(f"Errore API: {data['errors']}")

    return data.get("response", [])


if __name__ == "__main__":
    fixtures = get_fixtures()

    print(f"Partite trovate: {len(fixtures)}")

    for match in fixtures[:10]:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        print(f"{home} - {away}")
