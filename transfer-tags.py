import json
import csv


CHECKLIST_FILENAME = 'd2checklist-tags.json'
DIM_FILENAME = 'dim.csv'

TAG_MAPPING = {
    'upgrade': 'favorite',
    'keep': 'keep',
    'infuse': 'infuse',
    'junk': 'junk',
}


if __name__ == '__main__':
    with open(CHECKLIST_FILENAME, 'r') as checklist_file:
        checklist_data = json.loads(checklist_file.read())
        dim_rows = [('Id', 'Hash', 'Tag', 'Notes')] + [
            (
                id,
                '',
                TAG_MAPPING[tag],
                '',
            )
            for id, tag in checklist_data['marked'].items()
        ]

    with open(DIM_FILENAME, 'w') as dim_file:
        dim_writer = csv.writer(dim_file, delimiter=',')
        dim_writer.writerows(dim_rows)
