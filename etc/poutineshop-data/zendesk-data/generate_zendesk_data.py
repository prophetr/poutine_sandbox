from generate_data_table import GenerateDataTables

if __name__ == '__main__':

    SCHEMA_FILE_PATH = 'zendesk_schema.yml'
    gen_table = GenerateDataTables(SCHEMA_FILE_PATH)
    gen_table.generate_all_tables_to_csv()
