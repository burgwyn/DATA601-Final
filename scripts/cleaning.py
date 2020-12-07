# load pandas for data analysis
import pandas as pd

from utils import format_date, format_time

# load dataset
parking_violations = pd.read_csv(
    'data/sample/Parking_Violations_Issued_in_August_2018.csv')


def clean_data(parking_violations):

    # drop null columns
    parking_violations.drop(['VEHICLE_TYPE', 'PENALTY_1',
                             'PENALTY_2', 'PENALTY_3',
                             'PENALTY_4', 'PENALTY_5'],
                            axis=1, inplace=True)

    # drop disposition columns
    parking_violations.drop(['DISPOSITION_TYPE', 'DISPOSITION_DESC',
                             'DISPOSITION_DATE'], axis=1, inplace=True)

    parking_violations.drop('MULTI_OWNER_NUMBER', axis=1, inplace=True)

    # column has a single value, drop it
    parking_violations.drop('GIS_LAST_MOD_DTTM', axis=1, inplace=True)

    parking_violations.drop('PLATE_STATE', axis=1, inplace=True)

    parking_violations.drop('VIOLATION_PROC_DESC', axis=1, inplace=True)

    parking_violations.drop(['XCOORD', 'YCOORD',
                             'MAR_ID', 'OBJECTID'], axis=1, inplace=True)

    parking_violations.dropna(subset=['ISSUE_TIME'], inplace=True)

    parking_violations['FORMAT_DATE'] =\
        parking_violations.apply(lambda x:
                                 format_date(x['ISSUE_DATE']), axis=1)

    parking_violations['DAY_OF_MONTH'] =\
        parking_violations.apply(lambda x: x['FORMAT_DATE'].day, axis=1)

    parking_violations['MONTH'] = \
        parking_violations.apply(lambda x: x['FORMAT_DATE'].month, axis=1)

    parking_violations['FORMAT_TIME'] =\
        parking_violations.apply(lambda x:
                                 format_time(x['ISSUE_TIME']), axis=1)

    parking_violations['HOUR'] =\
        parking_violations.apply(lambda x: x['FORMAT_TIME'].hour, axis=1)

    parking_violations['DISPOSITION_RESULT'] =\
        parking_violations.apply(lambda x:
                                 1 if (x['DISPOSITION_CODE'] > 0) else 0,
                                 axis=1)

    # drop rows with nulls in meaningful dimensions
    parking_violations.dropna(subset=['ISSUING_AGENCY_CODE',
                                      'LATITUDE', 'LONGITUDE'],
                              inplace=True)

    # cast ISSUING_AGENCY_CODE to int
    parking_violations['ISSUING_AGENCY_CODE'] =\
        parking_violations['ISSUING_AGENCY_CODE'].astype('int')

    # cast FINE_AMOUNT to int
    parking_violations['FINE_AMOUNT'].fillna(0, inplace=True)
    parking_violations['FINE_AMOUNT'] =\
        parking_violations['FINE_AMOUNT'].astype('int')

    # cast DISPOSITION_CODE to int
    parking_violations['DISPOSITION_CODE'].fillna(0, inplace=True)
    parking_violations['DISPOSITION_CODE'] =\
        parking_violations['DISPOSITION_CODE'].astype('int')

    return parking_violations
