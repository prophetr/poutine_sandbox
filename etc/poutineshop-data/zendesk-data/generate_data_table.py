import numpy as np
import pandas as pd
import yaml

from generate_data import GenerateData
from alive_progress import alive_bar


class GenerateDataTables:
    def __init__(self, yaml_file_path):
        self.schemas = self._load_yaml_file(yaml_file_path)
        self.primary_keys = {}
        self.cache_col_dict = {}
        self.cache_table_dict = {}
        self.generate = GenerateData()

    @staticmethod
    def _load_yaml_file(yaml_file_path):
        f = open(yaml_file_path, 'r')
        schemas = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return schemas['tables']

    def generate_all_tables_to_csv(self):
        for table in self.schemas:
            table_name = table['name']
            self.generate_table_to_csv(table_name)

    def generate_table_to_csv(self, table_name):

        table_schema = self._find_table_schema(table_name)
        number_of_records = table_schema['number_of_records']
        table_series = {}

        with alive_bar(
                len(table_schema['columns']),
                title=f'Creating: {table_name}',
                title_length=40,
                bar='filling',
                spinner='classic'
        ) as bar:
            for column in table_schema['columns']:

                config = column['generate_config']
                data_column = self._column_builder(number_of_records, table_name, config)

                table_series[column['name']] = data_column

                # Save if is primary key
                if column.get('pk'):
                    self.primary_keys[table_name] = data_column

                # Save if is cache_column is true
                if column.get('cache_column'):
                    self.cache_col_dict[table_name] = {column['name']: data_column}

                bar()
                # print(f'\tColumn added: {column["name"]}')

        table_df = pd.DataFrame(table_series)
        table_df.to_csv(f'{table_name}.csv')
        if table_schema.get('cache_table'):
            self.cache_table_dict[table_name] = table_df

    def _find_table_schema(self, table_name):
        for table_schema in self.schemas:
            if table_schema['name'] == table_name:
                return table_schema

        raise ValueError(f'Sorry, {table_name} is not one of the listed table in the inputted schema .yml file')

    def _column_builder(self, number_of_records, table_name, field_config):
        column_series = None
        data_type = field_config['data_type']

        if data_type == 'int':
            method = field_config['method']
            min_range = field_config['min']
            max_range = field_config['max']

            if method == 'sequence':
                column_series = self.generate.int_range_sequence(
                    number_of_records=number_of_records,
                    min=min_range,
                    max=max_range
                )
            elif method == 'random':
                column_series = self.generate.random_int(
                    number_of_records=number_of_records,
                    min=min_range,
                    max=max_range
                )

        elif data_type == 'accepted_values':
            accepted_values = field_config['accepted_values']
            weights = field_config.get('weights')
            column_series = self.generate.random_accepted_values(
                number_of_records=number_of_records,
                accepted_values=accepted_values,
                weights=weights
            )

        elif data_type == 'text':
            size = field_config['size']
            column_series = self.generate.random_text(
                number_of_records=number_of_records,
                size=size
            )

        elif data_type == 'date':
            start_date = field_config['start_date']
            end_date = field_config['end_date']
            timestamp = field_config.get('timestamp')
            column_series = self.generate.random_date(
                number_of_records=number_of_records,
                start_date=start_date,
                end_date=end_date,
                timestamp=timestamp
            )

        elif data_type == 'phone':
            column_series = self.generate.random_phone_number(
                number_of_records=number_of_records
            )

        elif data_type == 'name':
            column_series = self.generate.random_name(
                number_of_records=number_of_records
            )

        elif data_type == 'email':
            column_series = self.generate.random_email(
                number_of_records=number_of_records
            )
        elif data_type == 'fk':

            referenced_table = field_config['referenced_table']
            repeat = field_config['repeat']

            try:
                referenced_ids = self.primary_keys[referenced_table]
            except KeyError:
                raise KeyError(
                    f'Sorry the table "{field_config["referenced_table"]}" has not been created in this session. '
                    'To fix this error, include the referenced table before this referenced field'
                )

            column_series = pd.Series(
                np.random.choice(
                    a=referenced_ids,
                    size=number_of_records,
                    replace=repeat
                )
            )
        elif data_type == 'mapped_values':
            referenced_table = field_config['referenced_table'] if field_config.get('referenced_table') is not None \
                else table_name
            referenced_column = field_config['referenced_column']
            mapped_values = field_config['mapped_values']

            cached_list = self._get_cached_column_value(referenced_table, referenced_column)

            mapped_list = [mapped_values[element] for element in cached_list]
            column_series = pd.Series(mapped_list)

        elif data_type == 'from_date':
            referenced_column = field_config['referenced_column']
            referenced_table = field_config['referenced_table'] if field_config.get('referenced_table') is not None\
                else table_name
            max_seconds_apart = 31536000 if field_config.get('max_seconds_apart') is None \
                else field_config.get('max_seconds_apart')
            timeline = field_config['timeline']

            cached_list = self._get_cached_column_value(referenced_table, referenced_column)

            column_series = self.generate.random_date_from_existing_col(
                timeline=timeline,
                referenced_column=cached_list,
                max_seconds_apart=max_seconds_apart
            )

        else:
            raise ValueError(f'Sorry, {data_type} is not a valid data type')

        return column_series

    def _get_cached_column_value(self, table_name, column_name):
        try:
            return self.cache_col_dict[table_name][column_name]
        except KeyError:
            raise KeyError(
                f'Sorry the column "{column_name}" in table "{table_name}" is not cached. '
                f'Apply the "cache_column" property to the column you want to reference to'
            )
