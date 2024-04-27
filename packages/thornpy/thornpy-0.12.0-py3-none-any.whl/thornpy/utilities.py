"""Miscellaneous tools.

"""
import csv
import os
import re
from numbers import Number
from pathlib import Path
from subprocess import Popen
from typing import Union

import pandas as pd

from scipy.io import loadmat


def open_in_explorer(path: os.PathLike) -> None:
    if Path(path).is_dir():
        _ = Popen(f'explorer.exe /root,"{path}"')
    elif Path(path).is_file():
        _ = Popen(f'explorer.exe /select,"{path}"')
    else:
        raise FileNotFoundError()


def num_to_ith(num):
    """Converts an integer to a string containing an ordinal number (1st, 2nd, 3rd, ect.)

    Parameters
    ----------
    num : int
        Number

    Returns
    -------
    str
        Ordinal number

    """
    if num == -1:
        return 'last'
    elif num < -1:
        value = str(num+1).replace('-', '')
    else:
        value = str(num)

    last_digit = value[-1]

    if len(value) > 1 and value[-2] == '1':
        suffix = 'th'
    elif last_digit == '1':
        suffix = 'st'
    elif last_digit == '2':
        suffix = 'nd'
    elif last_digit == '3':
        suffix = 'rd'
    else:
        suffix = 'th'

    if num < -1:
        suffix += ' to last'

    return value + suffix


def num_to_str(num: Number,
               places: int,
               allow_less=False,
               use_scientific: Union[bool, float] = False) -> str:
    """Converts a number to a string with a given number of significant figures.

    Parameters
    ----------
    num : Number
        Number to be converted
    places : int
        Number of decimal places to use
    allow_less : bool, optional
        If True, allows the number to be converted to a string with less decimal places than 
        `places`, by default False
    use_scientific : bool or Number, optional
        If True, uses scientific notation. If False, uses decimal notation. 
        If a number is passed, uses scientific notation if `num` is greater 
        than `use_scientific`, by default False

    Returns
    -------
    str
        Number converted to a string with a given number of decimal places

    """
    if not isinstance(use_scientific, bool) and isinstance(use_scientific, Number):
        if use_scientific > 1:
            use_scientific = abs(num) >= abs(use_scientific)
        else:
            use_scientific = abs(num) <= abs(use_scientific)

    if use_scientific:
        string = f'{num:.{places}e}'
    else:
        string = f'{num:.{places}f}'

    if allow_less and '.' in string:

        left, right, *exp = re.split(r'\.|e', string, flags=re.IGNORECASE)
        right = str(round(float(f'0.{right}'), places)).replace('0.', '.')
        if right == '.0':
            right = ''
        string = 'e'.join([f'{left}{right}', *exp])

    return string


def read_data_string(text, delimiter=',', newline='\n', has_headerline=True):
    """Reads a delimited string into a list of dictionaries.  Functions very similar to :meth:`numpy.genfromtxt`, but for strings instead of text files.

    Parameters
    ----------
    text : str
        String of row/column data with delimiters and new line indicators given in `delimiter` and `newline`.
    delimiter : str, optional
        Delimiter used in `text`, by default ','
    newline : str, optional
        New line indicator used in `text`, by default '\n'
    has_headerline : bool, optional
        If True, treats the first line of `text` as headers. If False, treats the first line of `text` as data and makes generic headers, by default True

    Returns
    -------
    :obj:`list` of :obj:`dict`
        A list of dictionaries containing the data from `text`

    """
    lines = text.split(newline)

    # Generate headers
    if has_headerline:
        # If the text has headerlines, get them
        headers = lines.pop(0).split(delimiter)

    else:
        # If the text doesn't have headerlines, make generic ones
        headers = [str(i+1) for i in range(len(lines[0].split(delimiter)))]

    data = []
    for line in lines:
        # For each line, check if data is missing

        if len(line.split(delimiter)) == len(headers):
            # If there is no missing data on this line, initialize a dictionary for the line data
            line_data = {}

            for header, value in zip(headers, line.split(delimiter)):
                # For each column in the line, add to the line_data dict (header as key and value as value)
                line_data[header] = value

            # Append the line_data dict to the data list
            data.append(line_data)

    return data


def convert_path(filepath):
    """Converts the slashes in `filepath` to whatever is appropriate for the current OS.

    Parameters
    ----------
    filepath : str
        Filepath to be converted

    Returns
    -------
    str
        Converted filepath

    """
    return os.path.normpath(filepath.replace('\\', os.sep).replace('/', os.sep))


def mat_to_pd(filename, data_start=None, data_end=None):
    """Creates a pandas dataframe from a .mat file

    Parameters
    ----------
    filename : str
        Filename of a .mat file

    Returns
    -------
    dataframe
        Pandas datafrom of data in `filename`

    """
    mat = loadmat(filename)  # load mat-file

    dataframes = []

    for variable in [var for var in mat if var not in ['__header__', '__globals__', '__version__']]:

        if mat[variable].shape[1] == 1:
            array = mat[variable]
        elif mat[variable].shape[0] == 1:
            array = mat[variable].transpose()
        else:
            raise ValueError(f'{filename} does not contain the expected data!')

        # Figure out data start and end indices if given
        if data_start is None:
            data_start = 0
        if data_end is None:
            data_end = len(array)

        dataframes.append(pd.DataFrame(array[data_start:data_end], columns=[variable]))

    dataframe = pd.concat(dataframes, axis=1)

    return dataframe


def dict_to_csv(data, filename):
    """Writes data in `dict` to a csv file with the keys as headers and the values as columns.

    Parameters
    ----------
    data : dict
        Dictionary of data
    filename : str
        Name of file to write data to. (include extension)

    """
    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))


def display_df_side_by_side(df1: pd.DataFrame, df2: pd.DataFrame):
    """Displays two `pd.DataFrames` side by side in a jupyter notebook

    Note
    ----
    Only works in a jupyter notebook

    Parameters
    ----------
    df1 : pd.DataFrame
        Left `pd.DataFrame`
    df2 : pd.DataFrame
        Right `pd.DataFrame`
    """
    from IPython.display import display_html
    df1_styler = df1.style.set_table_attributes("style='display:inline'").set_caption('df1')
    df2_styler = df2.style.set_table_attributes("style='display:inline'").set_caption('df2')

    display_html(df1_styler._repr_html_() + df2_styler._repr_html_(), raw=True)
