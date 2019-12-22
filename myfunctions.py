import pandas as pd
import datetime as dt


def fed_holiday(df):
    """
    Determining the dates of Federal Holidays for each year.
    :param df: file containing the date column.
    :return: federal holiday.

    >>> t = dt.datetime(2018, 11, 22)
    >>> d1 = pd.DataFrame({"Date": [t]})
    >>> a = fed_holiday(d1)
    >>> a # doctest: + ELLIPSIS
    "Thanksgiving Day"
    """

    if (df["Date"].month == 1) & (df["Date"].day == 1):
        return "New Year's Day"
    elif (df["Date"].month == 1) & (15 <= df["Date"].day <= 21) & (df["Date"].dayofweek == 1):
        return "Martin Luther King Day"
    elif (df["Date"].month == 2) & (df["Date"].day == 18):
        return "President's Day"
    elif (df["Date"].month == 5) & (25 <= df["Date"].day <= 31) & (df["Date"].dayofweek == 1):
        return "Memorial Day"
    elif (df["Date"].month == 7) & (df["Date"].day == 4):
        return "Independence Day"
    elif (df["Date"].month == 9) & (1 <= df["Date"].day <= 7) & (df["Date"].dayofweek == 1):
        return "Labor Day"
    elif (df["Date"].month == 10) & (8 <= df["Date"].day <= 14) & (df["Date"].dayofweek == 1):
        return "Columbus Day"
    elif (df["Date"].month == 11) & (df["Date"].day == 11):
        return "Veterans Day"
    elif (df["Date"].month == 11) & (22 <= df["Date"].day <= 28) & (df["Date"].dayofweek == 4):
        return "Thanksgiving Day"
    elif (df["Date"].month == 12) & (df["Date"].day == 25):
        return "Christmas Day"
    else:
        return "Non-holidays"


def daily_temp(dft):
    """
    Calculate daily mean temperature.
    The temperature from the files is in tenths of degree C.
    :param dft: file containing temperatures
    :return: value of the mean temperature

    >>> d2 = pd.DataFrame({"T_Max": [200], "T_Min": [-100]})
    >>> v = daily_temp(d2)
    >>> v # doctest: + ELLIPSIS
    5
    """

    tavg = (dft["T_Max"] + dft["T_Min"]) / 20  # tenths of degree C
    return tavg


def daily_incidents(df2):
    """
    Distinguish federal holidays and normal days to find the average number of daily crime incidents.
    :param df2: file containing number of crime incidents by holidays.
    :return: average number of crime incidents for each holiday.

    >>> d3 = pd.DataFrame({"Holiday": ["Christmas Day"], "Total": [18000]})
    >>> x = daily_incidents(d3)
    >>> x # doctest: + ELLIPSIS
    1000
    """

    if (df2["Holiday"] == "Thanksgiving Day") | (df2["Holiday"] == "Christmas Day"):
        d_inc = df2["Total"] / 18
    elif df2["Holiday"] == "Non-holidays":
        d_inc = df2["Total"] / 6712
    else:
        d_inc = df2["Total"] / 19

    return d_inc
