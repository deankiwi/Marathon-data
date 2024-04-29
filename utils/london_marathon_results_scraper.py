import random
import time
import requests
from bs4 import BeautifulSoup


def scrape_marathon_data(
    url: str,
    pages: int,
    table_html_tag: str,
    table_class_name: str,
    cell_html_tag: str,
    file_path: str,
):
    for page in range(1, pages + 1):
        print(f"Page: {page}")

        # URL of the website
        # url = f"https://results.tcslondonmarathon.com/2024/?page={page}&event=MAS&num_results=1000&pid=list&pidp=start&search%5Bsex%5D=W&search%5Bage_class%5D=%25"
        url_update = url.format(page=page)

        print(f"URL: {url_update}")

        # Send a GET request to the URL
        response = requests.get(url_update)

        # wait for 5 second
        wait = random.randint(1, 10)
        print(f"Waiting for {wait} seconds")
        time.sleep(wait)

        # Check if the request was successful
        if response.status_code == 200:
            print("Webpage retrieved successfully.")
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the unordered list with class "list-group list-group-multicolumn"
            # unordered_list = soup.find("ul", class_="list-group list-group-multicolumn")
            unordered_list = soup.find(table_html_tag, class_=table_class_name)

            # Check if the unordered list is found
            if unordered_list:
                # Iterate through the list items and print the text
                for item in unordered_list.find_all(cell_html_tag):
                    # append data to file london_marathon.txt
                    with open(file_path, "a") as f:
                        f.write(item.text + "\n")
                    # print(item.text)
            else:
                print("Unordered list not found on the webpage.")
        else:
            print(
                f"Failed to retrieve the webpage. Status code: {response.status_code}"
            )


if __name__ == "__main__":
    # mens 2010
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2010/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        25,
        "table",
        "list-table",
        "td",
        "london_marathon_2010_mens_raw.txt",
    )

    # mens 2011
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2011/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        23,
        "table",
        "list-table",
        "td",
        "london_marathon_2011_mens_raw.txt",
    )

    # mens 2012
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2012/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        24,
        "table",
        "list-table",
        "td",
        "london_marathon_2012_mens_raw.txt",
    )

    # mens 2013
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2013/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        23,
        "table",
        "list-table",
        "td",
        "london_marathon_2013_mens_raw.txt",
    )

    # mens 2014
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2014/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        23,
        "table",
        "list-table",
        "td",
        "london_marathon_2014_mens_raw.txt",
    )

    # mens 2015
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2015/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        24,
        "table",
        "list-table",
        "td",
        "london_marathon_2015_mens_raw.txt",
    )

    # mens 2016
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2016/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        24,
        "table",
        "list-table",
        "td",
        "london_marathon_2016_mens_raw.txt",
    )

    # mens 2017
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2017/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        24,
        "table",
        "list-table",
        "td",
        "london_marathon_2017_mens_raw.txt",
    )

    # mens 2018
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2018/index.php?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search_sort=place_nosex&split=time_finish_netto",
        24,
        "table",
        "list-table",
        "td",
        "london_marathon_2018_mens_raw.txt",
    )

    # mens 2019
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2019/?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search%5Bnation%5D=%25&search_sort=place_nosex",
        25,
        "ul",
        "list-group list-group-multicolumn",
        "li",
        "london_marathon_2019_mens_raw.txt",
    )

    # mens 2021
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2021/?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search%5Bnation%5D=%25&search_sort=place_nosex",
        22,
        "ul",
        "list-group list-group-multicolumn",
        "li",
        "london_marathon_2021_mens_raw.txt",
    )

    # mens 2022
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2022/?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search%5Bnation%5D=%25&search_sort=place_nosex",
        24,
        "ul",
        "list-group list-group-multicolumn",
        "li",
        "london_marathon_2022_mens_raw.txt",
    )

    # mens 2023
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2023/?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search%5Bnation%5D=%25&search_sort=place_nosex",
        29,
        "ul",
        "list-group list-group-multicolumn",
        "li",
        "london_marathon_2023_mens_raw.txt",
    )

    # mens 2024
    scrape_marathon_data(
        "https://results.tcslondonmarathon.com/2024/?page={page}&event=MAS&num_results=1000&pid=search&search%5Bsex%5D=M&search%5Bnation%5D=%25&search_sort=place_nosex",
        31,
        "ul",
        "list-group list-group-multicolumn",
        "li",
        "london_marathon_2024_mens_raw.txt",
    )
