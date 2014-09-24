def read_sql(path):
    with open(path) as fo:
        for line in fo:
            if 'CREATE TABLE' in line:
                print('\n\n')
                print('----------------------------')
                print(line.strip().split(' ')[2])
                print('----------------------------')
            elif ',' in line and line.strip().startswith(','):
                print(line.strip().split(' ')[1])
            elif ',' in line:
                print(line.strip().split(' ')[0])