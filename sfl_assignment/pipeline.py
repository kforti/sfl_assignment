

def run_etl_pipeline(file_name, data_access, unit_of_work):
    records = extract(file_name, data_access)
    transformed_records = uppercase_name_transform(records)
    load(transformed_records, unit_of_work)


def extract(file_name, data_access):
    records = data_access.get(file_name)
    return records


def uppercase_name_transform(records):
    for record in records:
        record['first_name'] = record['first_name'].upper()
        record['last_name'] = record['last_name'].upper()
    transformed_records = records
    return transformed_records


def load(records, unit_of_work):
    with unit_of_work:
        for record in records:
            unit_of_work.repository.add(record)
        unit_of_work.commit()
    return None
