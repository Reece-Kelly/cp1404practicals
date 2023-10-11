FILE_NAME = "wimbledon.csv"


def main():
    """Get records from a file and process and display information about records."""
    records = get_records(FILE_NAME)
    champion_countries, champion_to_count = process_records(records)
    display_processed_records(champion_countries, champion_to_count)


def display_processed_records(champion_countries, champion_to_count):
    """Display the countries of champions and the champions names and how many times they have won"""
    print("Wimbledon Champions:")
    for champion_name, count in champion_to_count.items():
        print(f"{champion_name} {count}")
    print(f"\nThese {len(champion_countries)} have won Wimbledon:")
    print(", ".join(champion_countries for champion_countries in sorted(champion_countries)))


def process_records(records):
    """Return a set of champions countries and a dictionary of champions names to the amount of times they've won"""
    champion_to_count = {}
    champion_countries = set()
    for record in records:
        champion_countries.add(record[1])
        if record[2] in champion_to_count:
            champion_to_count[record[2]] += 1
        else:
            champion_to_count[record[2]] = 1
    return champion_countries, champion_to_count


def get_records(file_name):
    """Read a file and store each line as a list in a list"""
    records = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            record_parts = line.strip().split(",")
            records.append(record_parts)
    return records


main()
