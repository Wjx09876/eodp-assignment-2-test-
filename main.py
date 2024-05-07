import pip

from GetGenres import getGenres

""" 
To run the project, run this file in command line with "python main.py"
"""

# path for raw data to be read from
rawDataPath = "data/raw/"

# path for processed data to be saved
processedDataPath = "data/processed/"

# path for graphs to be saved
graphOutPath = "graphs/"

# names of the dependencies to be installed - note that i tried skikit-
# learn but it was a little fucky probably not worth fixing
dependencies = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "requests": "requests",
}


def InstallDependencies():
    """
    Install all the dependencies for the project
    """

    def install(package):
        if hasattr(pip, "main"):
            pip.main(["install", package])
        else:
            pip._internal.main(["install", package])

    for package in dependencies:
        try:
            __import__(package)
        except ImportError as e:
            # print error
            print(e)
            install(package)


def RunAll():
    """
    Run all the functions in the project - paths for everything included in this file
    """

    getGenres(
        rawDataPath + "BX-Books.csv", processedDataPath + "BX-Books-with-Genres.csv"
    )


if __name__ == "__main__":
    InstallDependencies()
    RunAll()
