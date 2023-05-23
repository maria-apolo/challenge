from datetime import datetime
import pandas as pd
import numpy as np

def get_period_day(date):
    """
    Gets date of operated flight

    Args:
        date (datetime): date of operated flight.

    Returns:
        str: the period of day [mañana, tarde, noche]
    """

    date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').time()
    morning_min = datetime.strptime("05:00", '%H:%M').time()
    morning_max = datetime.strptime("11:59", '%H:%M').time()
    afternoon_min = datetime.strptime("12:00", '%H:%M').time()
    afternoon_max = datetime.strptime("18:59", '%H:%M').time()
    #night_min = datetime.strptime("19:00", '%H:%M').time()
    #night_max = datetime.strptime("4:59", '%H:%M').time()
    
    if(date_time >= morning_min and date_time <= morning_max):
        return 'mañana'
    elif(date_time >= afternoon_min and date_time <= afternoon_max):
        return 'tarde'
    #elif(date_time >= night_min and date_time <= night_max):
    else:
        return 'noche'
    

def is_high_season(date):
    """
    Determine if is high season

    Args:
        fecha (datetime): date of operated flight.

    Returns:
        int: 1 if is high season, 0 otherwise
    """

    fecha_año = int(fecha.split('-')[0])
    fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    range1_min = datetime.strptime('15-Dec', '%d-%b').replace(year = fecha_año)
    range1_max = datetime.strptime('3-Mar', '%d-%b').replace(year = fecha_año)
    range2_min = datetime.strptime('15-Jul', '%d-%b').replace(year = fecha_año)
    range2_max = datetime.strptime('31-Jul', '%d-%b').replace(year = fecha_año)
    range3_min = datetime.strptime('11-Sep', '%d-%b').replace(year = fecha_año)
    range3_max = datetime.strptime('30-Sep', '%d-%b').replace(year = fecha_año)
    
    if ((fecha >= range1_min and fecha <= range1_max) or 
        (fecha >= range2_min and fecha <= range2_max) or 
        (fecha >= range3_min and fecha <= range3_max)):
        return 1
    else:
        return 0
    
def get_min_diff(data):
    """
    Difference between operated and programmed flight

    Args:
        data (pd.dataFrame): flights dataframe.

    Returns:
        int: diffence in minutes between operated
        and programmed date 
    """

    fecha_o = datetime.strptime(data['Fecha-O'], '%Y-%m-%d %H:%M:%S')
    fecha_i = datetime.strptime(data['Fecha-I'], '%Y-%m-%d %H:%M:%S')
    min_diff = ((fecha_o - fecha_i).total_seconds())/60
    return min_diff


def get_rate_from_column(data, column):
    """
    Computes delay rates by column

    Args:
        data (pd.dataFrame): flights dataframe.

    Returns:
        pd.dataFrame: Each different column value
        and its respective delay rate
    """


    data_delayed = data.loc[data['delay'] == 1]
    delays = dict(data_delayed[column].value_counts())
    total = data[column].value_counts().to_dict()

    rates = {}
    for name, total in total.items():
        if name in delays:
            rates[name] = round(delays[name]/total, 2)*100
        else:
            rates[name] = 0
    return pd.DataFrame.from_dict(data = rates, orient = 'index', columns = ['Tasa (%)'])

