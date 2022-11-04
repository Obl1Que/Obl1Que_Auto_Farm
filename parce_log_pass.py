def getLogPass(txt_file):
    lp = open(txt_file, 'r')
    log_pass_dict = {}

    while True:
        line = lp.readline()

        if not line:
            break

        line = line.replace('\n', '').split(':')
        log_pass_dict[line[0]] = line[1]

    lp.close()

    return log_pass_dict
