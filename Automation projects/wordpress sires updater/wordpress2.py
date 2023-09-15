import requests
from bs4 import BeautifulSoup

def replace_word_in_website(url, old_word, new_word):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        content = response.text
        replaced_content = content.replace(old_word, new_word)

        return replaced_content

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    websites = [
        'https://recurpost.com/blog/all-about-twitter-fake-news-and-how-bots-spread-lies/',
        'https://recurpost.com/agorapulse-alternatives/',
        'https://recurpost.com/best-publer-alternative/',
    ]
    old_word = 'Twitter'
    new_word = 'X'

    for site in websites:
        print(f"Processing {site}...")
        updated_content = replace_word_in_website(site, old_word, new_word)

        if updated_content:
            # Here you can save the updated content, display it, or push it to the server.
            # For demonstration purposes, I'm just saving it to a local file.
            filename = site.replace('https://', '').replace('http://', '').replace('/', '_') + '.html'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(updated_content)
        print(f"Completed processing {site}.\n")

if __name__ == "__main__":
    main()
