# save_urls.py


def save_urls_to_file(file_path, urls):
    
    with open(file_path, "w") as file:
        for url in urls:
            file.write(url + "\n")


def main():
    
    urls = [
        "https://www.opodo.com/flights/airline/ME/middle-east-airlines/",
        "https://writer.com/",
        "https://www.bayut.com/",
        "https://www.geeksforgeeks.org/",
        
    ]

    
    file_path = "urls.txt"
    save_urls_to_file(file_path, urls)
    print(f"URLs have been saved to {file_path}")


if __name__ == "__main__":
    main()
