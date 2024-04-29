from math import e
import typer
import csv
import re


app = typer.Typer()


@app.command()
def remove_empty_lines(filename):
    # Read the file and store its lines in a list
    with open(filename, "r") as file:
        lines = file.readlines()

    # Filter out empty lines
    non_empty_lines = [line for line in lines if line.strip() != ""]

    # Write non-empty lines back to the file
    with open(filename, "w") as file:
        file.writelines(non_empty_lines)


@app.command()
def txt_to_csv(txt_file, csv_file):
    # Open the .txt file for reading
    with open(txt_file, "r") as infile:
        # Read lines from the .txt file
        lines = infile.readlines()

        # Remove any leading or trailing whitespace from each line
        lines = [line.strip() for line in lines]
        remove = [
            "Place (Overall)",
            "Place (Gender)",
            "Place (Category)",
            "Name",
            "ClubClub",
            "Runner NumberRunner Number",
            "CategoryCategory",
            "HalfHalf",
            "FinishFinish",
            "EventMass",
            "EventEvent",
            "",
        ]
        lines = [line for line in lines if line not in remove]

     

        # Open the .csv file for writing
        with open(csv_file, "w", newline="") as outfile:
            # Create a CSV writer object
            csv_writer = csv.writer(outfile)

            # add the header
            csv_writer.writerow(
                [
                    "place_overall",
                    "place_gender",
                    "place_category",
                    "name",
                    "club",
                    "bib",
                    "category",
                    "half",
                    "finish",
                ]
            )

            for i in range(0, len(lines), 9):
                place_overall = int(lines[i])
                place_gender = int(lines[i + 1])
                place_category = int(lines[i + 2]) if lines[i + 2].isdigit() else None
                name = lines[i + 3]
                club = lines[i + 4].replace("Club", "")
                bib = int(lines[i + 5].replace("Runner Number", ""))
                category = lines[i + 6].replace("Category", "")
                half = lines[i + 7].replace("Half", "")
                finish = lines[i + 8].replace("Finish", "")
                add = [
                    place_overall,
                    place_gender,
                    place_category,
                    name,
                    club,
                    bib,
                    category,
                    half,
                    finish,
                ]
                print(add)
                csv_writer.writerow(add)


@app.command()
def txt_to_csv2(txt_file, csv_file):
    # there is a different format in 2010 as there is no club or event
    # Open the .txt file for reading
    with open(txt_file, "r") as infile:
        # Read lines from the .txt file
        lines = infile.readlines()

        # Remove any leading or trailing whitespace from each line
        lines = [line.strip() for line in lines]

        # Open the .csv file for writing
        with open(csv_file, "w", newline="") as outfile:
            # Create a CSV writer object
            csv_writer = csv.writer(outfile)

            # add the header
            csv_writer.writerow(
                [
                    "place_overall",
                    "place_gender",
                    "place_category",
                    "name",
                    "bib",
                    "category",
                    "half",
                    "finish",
                ]
            )

            # Write each line to the .csv file
            for i in range(0, len(lines), 9):
                place_overall = int(lines[i])
                place_gender = int(lines[i + 1])
                place_category = int(lines[i + 2]) if lines[i + 2].isdigit() else None
                name = lines[i + 3].replace("» ", "")
                bib = int(lines[i + 4])
                category = lines[i + 5]
                half = lines[i + 6]
                finish = lines[i + 7]

                add = [
                    place_overall,
                    place_gender,
                    place_category,
                    name,
                    bib,
                    category,
                    half,
                    finish,
                ]
                print(add)
                csv_writer.writerow(add)


@app.command()
def txt_to_csv3(txt_file, csv_file):
    # there is a different format in 2011, 12, 13, 14
    # Open the .txt file for reading
    with open(txt_file, "r") as infile:
        # Read lines from the .txt file
        lines = infile.readlines()

        # Remove any leading or trailing whitespace from each line
        lines = [line.strip() for line in lines]

        # Open the .csv file for writing
        with open(csv_file, "w", newline="") as outfile:
            # Create a CSV writer object
            csv_writer = csv.writer(outfile)

            # add the header
            csv_writer.writerow(
                [
                    "place_overall",
                    "place_gender",
                    "place_category",
                    "name",
                    "bib",
                    "category",
                    "half",
                    "finish",
                ]
            )

            # Write each line to the .csv file
            for i in range(0, len(lines), 10):
                place_overall = int(lines[i])
                place_gender = int(lines[i + 1])
                place_category = int(lines[i + 2]) if lines[i + 2].isdigit() else None
                name = lines[i + 3].replace("» ", "")
                bib = int(lines[i + 5])
                category = lines[i + 6]
                half = lines[i + 7]
                finish = lines[i + 8]

                add = [
                    place_overall,
                    place_gender,
                    place_category,
                    name,
                    bib,
                    category,
                    half,
                    finish,
                ]
                print(add)
                csv_writer.writerow(add)


@app.command()
def txt_to_csv4(txt_file, csv_file):
    # there is a different format in 2015, 16, 17, 18
    # Open the .txt file for reading
    with open(txt_file, "r") as infile:
        # Read lines from the .txt file
        lines = infile.readlines()

        # Remove any leading or trailing whitespace from each line
        lines = [line.strip() for line in lines]

        # Open the .csv file for writing
        with open(csv_file, "w", newline="") as outfile:
            # Create a CSV writer object
            csv_writer = csv.writer(outfile)

            # add the header
            csv_writer.writerow(
                [
                    "place_overall",
                    "place_gender",
                    "place_category",
                    "name",
                    "club",
                    "bib",
                    "category",
                    "half",
                    "finish",
                ]
            )

            # Write each line to the .csv file
            for i in range(0, len(lines), 11):
                place_overall = int(lines[i])
                place_gender = int(lines[i + 1])
                place_category = int(lines[i + 2]) if lines[i + 2].isdigit() else None
                name = lines[i + 3].replace("» ", "")
                club = lines[i + 5]
                bib = int(lines[i + 6])
                category = lines[i + 7]
                half = lines[i + 8]
                finish = lines[i + 9]

                add = [
                    place_overall,
                    place_gender,
                    place_category,
                    name,
                    club,
                    bib,
                    category,
                    half,
                    finish,
                ]
                print(add)
                csv_writer.writerow(add)


def is_valid_time(time_str):
    """Check if the string matches the time format hh:mm:ss"""
    pattern = re.compile(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$")
    return bool(pattern.match(time_str))


@app.command()
def fix_time_lines(filename, output_filename):
    """
    2010 had a lot of missing half marathon times, this script will fix the missing times
    """
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()

    fixed_lines = []
    i = 0

    while i < len(lines):
        time_line = lines[i + 7].strip()
        if not is_valid_time(time_line):
            fixed_lines.extend(lines[i : i + 6] + ["--\n"] + lines[i + 6 : i + 7])
            i += 7
        else:

            fixed_lines.extend(lines[i : i + 8])

            i += 8

    with open(output_filename, "w") as file:
        file.writelines(fixed_lines)


if __name__ == "__main__":
    # app()
    txt_to_csv2(
        "london_marathon_2010_mens_raw.txt",
        "data/london_marathon_2010_mens.csv",
    )
    for year in [2011, 2012, 2013, 2014]:
        txt_to_csv3(
            f"london_marathon_{year}_mens_raw.txt",
            f"data/london_marathon_{year}_mens.csv",
        )
    for year in [2015, 2016, 2017, 2018]:
        txt_to_csv4(
            f"london_marathon_{year}_mens_raw.txt",
            f"data/london_marathon_{year}_mens.csv",
        )
    for year in [2019, 2021, 2022, 2023, 2024]:

        txt_to_csv(
            f"london_marathon_{year}_mens_raw.txt",
            f"data/london_marathon_{year}_mens.csv",
        )
