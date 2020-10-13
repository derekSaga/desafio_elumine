import pandas as pd


def extension_file(filename):
    return filename.rsplit(".", 1)[1].lower()


def load_file_df(file, sep=",", usecols=None, skiprows=None):
    extension = extension_file(file.filename)
    print(extension)
    if extension == "csv" or extension == "txt":
        df = pd.read_csv(file, sep=sep)
    elif extension == "xlsx":
        if skiprows is None:
            df = pd.read_excel(file, usecols=usecols)
        else:
            df = pd.read_excel(file, usecols=usecols, skiprows=skiprows)
    else:
        return None
    return df
