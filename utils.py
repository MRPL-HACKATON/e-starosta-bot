data = {
    'Информатика': {
        'КБ-001': {
            '24.10.2020': {
                '09:00': 'Информатика',
                '09:50': 'Математика'
            }
        },
        'КБ-002': {
            '24.10.2020': {
                '09:00': 'Информатика',
                '09:50': 'Математика'
            }
        }
    }
}


def get_facultets():
    return data.keys()


def get_all_groups():
    groups = []
    for facultet in data:
        groups = groups + list(data[facultet].keys())
    return groups


def get_groups(facultet):
    return data[facultet]


def get_by_group_for_date(group, date):
    facultet = find_facultet_for_group(group)
    return data[facultet][group][date]


def find_facultet_for_group(group):
    facultet = None
    for facultet in data:
        if group in facultet:
            facultet = facultet
            break

    return facultet
