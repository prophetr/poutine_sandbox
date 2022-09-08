import datetime
import lorem
import numpy as np
import pandas as pd
import random

from pydbgen import pydbgen


class GenerateData:
    def __init__(self):
        self._random_db = pydbgen.pydb()
        np.random.seed(0)
        random.seed(1)

    @staticmethod
    def int_range_sequence(number_of_records: int, min: int, max: int):
        """
        Generate a pandas series of ordered integers between the min and max value

        :param number_of_records: The number of records to create
        :type number_of_records: int
        :param min: The first value of the sequence
        :type min: int
        :param max: The last value of the sequence
        :type max: int
        :return: Series of ordered integers between the min and max value
        :rtype: pandas series
        """

        ids = [i for i in range(min, max)]

        if len(ids) != number_of_records:
            raise Exception('Sorry min max range does not equal to the expected number of records')

        return pd.Series(ids)

    @staticmethod
    def random_int(number_of_records: int, min: int, max: int):
        """
        Generate a pandas series of random integers between the min and max value


        :param number_of_records: The number of records to create
        :type number_of_records: int
        :param min: The lowest possible integer that can be generated in the column
        :type min: int
        :param max: The highest possible integer that can be generated in the column
        :type max: int
        :return: Series of random integers between the min and max value
        :rtype: pandas series
        """

        ids = [random.randint(min, max) for i in range(number_of_records)]
        return pd.Series(ids)

    @staticmethod
    def random_text(number_of_records: int, size: str):
        """
        Generate a pandas series of random generated text

        :param number_of_records: The number of records to create
        :type number_of_records: int
        :param size: The text size to generate
        :type size: String
        :return: Series of random generated text
        :rtype: pandas series
        """

        if size.lower() == 'small':
            text = lorem.sentence
        elif size.lower() == 'medium':
            text = lorem.paragraph
        elif size.lower() == 'large':
            text = lorem.text
        else:
            raise ValueError(
                f'Sorry, {size} is not a size option. Available options are: small, medium, large'
            )

        texts = [text() for i in range(number_of_records)]
        return pd.Series(texts)

    @staticmethod
    def random_accepted_values(number_of_records: int, accepted_values: list, weights: list = None):
        """
        Generate a pandas series of random elements from a list of accepted values

        :param number_of_records: The number of records to create
        :type number_of_records: int
        :param accepted_values: List of accepted values
        :type accepted_values: list
        :param weights: List of weighted distribution in respect to the element in accepted_values list. Total must
        sum to 1
        :type weights: list
        :return: Series of random distributed elements from the accepted_values list
        :rtype: pandas series
        """

        accepted_values_list = random.choices(
            accepted_values,
            k=number_of_records,
            weights=weights
        )
        return pd.Series(accepted_values_list)

    @staticmethod
    def random_date(number_of_records: int, start_date, end_date, timestamp: bool = False):

        # Parse Date
        start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        # Days between start and end
        time_between_dates = end_date_parse - start_date_parse
        days_between_dates = time_between_dates.days

        date_list = []

        # Generate random date between start and end date
        for i in range(number_of_records):
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date_parse + datetime.timedelta(days=random_number_of_days)

            if timestamp:
                random_second = random.randrange(86400)
                random_datetime = random_date + datetime.timedelta(seconds=random_second)
                date_list.append(random_datetime)
            else:
                date_list.append(random_date)

        return pd.Series(date_list)

    @staticmethod
    def random_date_from_existing_col(
            timeline: str,
            referenced_column,
            max_seconds_apart=31536000 # default 1 year
    ):
        date_list = []

        for date in referenced_column:
            random_second = random.randrange(max_seconds_apart)
            if timeline == 'after':
                random_time = date + datetime.timedelta(seconds=random_second)
            elif timeline == 'before':
                random_time = date - datetime.timedelta(seconds=random_second)
            else:
                raise ValueError('Sorry, invalid period: {period}. Try "before" or "after"')
            date_list.append(random_time)

        return pd.Series(date_list)

    def random_email(self, number_of_records: int):
        # TODO: match email with name
        return self._random_db.gen_data_series(number_of_records, 'email')

    def random_phone_number(self, number_of_records: int):
        return self._random_db.gen_data_series(number_of_records, 'phone_number_simple')

    def random_name(self, number_of_records: int):
        return self._random_db.gen_data_series(number_of_records, 'name')
