def input_deserializer(input) -> list[list[str]]:
    """Parse input from string to list"""
    with open(input, "r") as f:
        data = f.read()
    data = data.split("\n")
    raw_data = []
    for row in data:
        raw_data.append(row.split())
    return raw_data


def output_serializer(report):
    pass
