def getLogPass(txt_file, type = 'dict'):
    lp = open(txt_file, 'r')

    if type == 'dict':
        log_pass = {}

    elif type == 'mass':
        log_pass = []

    while True:
        line = lp.readline()

        while line == '\n':
            line = lp.readline()

        if not line:
            break

        if type == 'dict':
            line = line.replace('\n', '').split(':')
            log_pass[line[0]] = line[1]

        elif type == 'mass':
            log_pass.append(line.replace('\n', ''))

    lp.close()

    return log_pass