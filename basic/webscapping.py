import os
import requests
from bs4 import BeautifulSoup
import json
import csv

def get_domain_name(url):
    # Extracts a simplified domain name to use as a filename
    if "www." in url:
        domain_name = url.split("www.")[1].split("/")[0]
    else:
        domain_name = url.split("//")[1].split("/")[0]
    return domain_name.replace(".", "_")

def save_content_to_file(folder, filename, content):
    # Ensures the directory exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Saves content to a file
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
        file.write(content)

def fetch_page_content():
    url = input("Enter the URL to fetch content: ")
    response = requests.get(url)
    if response.status_code == 200:
        domain_name = get_domain_name(url)
        filename = f"{domain_name}.txt"
        save_content_to_file("basic/webscrapped_files", filename, response.text)
        print(f"Page content saved to {filename}")
    else:
        print("Failed to retrieve the webpage")

def extract_titles():
    url = input("Enter the URL to extract titles: ")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')  # Adjust tag as per your target webpage
        titles_text = "\n".join([title.text for title in titles])
        domain_name = get_domain_name(url)
        filename = f"{domain_name}_titles.txt"
        save_content_to_file("webscrapped_files", filename, titles_text)
        print(f"Titles extracted and saved to {filename}")
    else:
        print("Failed to retrieve the webpage")

def main():
    print("Web Scraping Suite")
    while True:
        print("\nOptions:")
        print("1. Fetch Page Content")
        print("2. Extract Titles")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            fetch_page_content()
        elif choice == '2':
            extract_titles()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
