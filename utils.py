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


def getFacultets():
    return data.keys()


def getAllGroups():
    groups = []
    for facultet in data:
        groups = groups + list(data[facultet].keys())
    return groups


def getGroups(facultet):
    return data[facultet]


def getByGroupForDate(group, date):
    facultet = findFacultetForGroup(group)
    return data[facultet][group][date]


def findFacultetForGroup(group):
    facultet = None
    for facultet in data:
        if group in facultet:
            facultet = facultet
            break

    return facultet
