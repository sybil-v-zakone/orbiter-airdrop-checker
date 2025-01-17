import requests
import json

def fetch_token_count(wallet_address):
    url = f"https://api.orbiter.finance/sdk/opoints/user/{wallet_address}"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en,en-US;q=0.9,ru;q=0.8",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("result", 0).get("points", 0)
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON для адреса {wallet_address}")
            return 0
    else:
        print(f"Ошибка запроса для адреса {wallet_address}: {response.status_code}")
        return 0

def main():
    total_tokens = 0

    try:
        with open("wallets.txt", "r") as file:
            wallets = [line.strip() for line in file if line.strip()]

        for wallet in wallets:
            tokens = fetch_token_count(wallet)
            if tokens < 40:
                tokens = 0
            else:
                tokens = int(tokens * 5.5970149254)
            print(f"{wallet}: {tokens}")
            total_tokens += tokens

        print(f"Общее количество токенов: {total_tokens}")

    except FileNotFoundError:
        print("Файл wallets.txt не найден")

if __name__ == "__main__":
    main()
