from app.redirect import redirect2method

def main():
    get_url = input("Enter the URL of the API: ")
    redirect2method(get_url)


if __name__ == "__main__":
    main()
