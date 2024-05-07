import pandas as pd
import requests
import json


def getGenres(dataPath: str, outLocation: str) -> None:
    """
    This function gets the genres from dataPath and writes them, appending column for genres, to outLocation.
    """
    # Read the data
    data = pd.read_csv(dataPath)

    # we can use openlibrary ISBN api to get the "subjects" of the book
    # then we can use some sort of clustering to get the genres
    data["Genres"] = None
    # TODO: make the range of this the length of the data so it can be run on the whole dataset
    # FIXME: current api seems to fail on some ISBNs - switch to google books api
    for i in range(0, 5):
        # get the isbn
        isbn = data.at[i, "ISBN"]

        response = requests.get("https://openlibrary.org/isbn/" + str(isbn) + ".json")
        jsonOutput = response.json()
        # making a set of all the subjects of the book
        subjects = set()
        try:
            for subject in jsonOutput["subjects"]:
                for s in subject.split(" -- "):
                    subjects.add(s)
        except KeyError:
            print("No subjects for ISBN: " + str(isbn))

        data["Genres"].at[i] = " -- ".join(subjects)
        print("Done with row " + str(i))

    # write the data
    data.to_csv(outLocation)
