def input_deserializer(input) -> list[list[str]]:
    """Parse input from string to list"""
    with open(input, "r") as f:
        data = f.read()
    data = data.split("\n")
    raw_data = []
    for row in data:
        raw_data.append(row.split())
    return raw_data


def output_serializer(records):
    """Serialize records to string"""
    serialized_output = ""
    for record in records:
        serialized_record = f"{record.name}: {record.time} minutes"
        if record.days > 0:
            suffix = "days" if record.days > 1 else "day"
            serialized_record += f" in {record.days} {suffix}"
        serialized_record += "\n"
        serialized_output += serialized_record
    return serialized_output
