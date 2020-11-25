import json
import os

CHECKLIST_FILENAME = 'd2checklist-tags.json'
DIM_FILENAME = 'dim-data.json'
DIM_RESULT_FILENAME = 'dim-data-result.json'

DIM_PLATFORM_MEMBERSHIP_ID = '4611686018461090495'
DIM_DESTINY_VERSION = 2

TAG_MAPPING = {
    'upgrade': 'favorite',
    'keep': 'keep',
    'infuse': 'infuse',
    'junk': 'junk',
}

if __name__ == '__main__':
    try:
        dim_file = open(DIM_FILENAME, 'r')
        dim_data = json.loads(dim_file.read())

        checklist_file = open(CHECKLIST_FILENAME, 'r')
        checklist_data = json.loads(checklist_file.read())
    except FileNotFoundError:
        exit(f'Put {CHECKLIST_FILENAME} and {DIM_FILENAME} in the directory.')

    dim_data['tags'] = [
        {
            'platformMembershipId': DIM_PLATFORM_MEMBERSHIP_ID,
            'destinyVersion': DIM_DESTINY_VERSION,
            'annotation': {
                'id': id,
                'tag': TAG_MAPPING[tag],
            },
        }
        for id, tag in checklist_data['marked'].items()
    ]

    dim_result_file = open(DIM_RESULT_FILENAME, 'w')
    dim_result_file.write(json.dumps(dim_data))

    os.remove(CHECKLIST_FILENAME)
    os.remove(DIM_FILENAME)
