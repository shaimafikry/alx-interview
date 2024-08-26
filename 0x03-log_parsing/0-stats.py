#!/usr/bin/python3
'''script that reads stdin line by line and
computes metrics
'''
import sys


def check_format(line):
    """check format of input"""
    check = 0
    s_line = line.split(' ')
    # print(s_line)
    # <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    # <status code> <file size>
    if not len(s_line[0].split('.')) == 4:
        check += 1
    if not s_line[1] == '-':
        check += 1
    if not s_line[2].startswith('['):
        check += 1
    if not s_line[3].endswith(']'):
        check += 1
    if not s_line[4].startswith('"G'):
        check += 1
    if not s_line[6].startswith('HT'):
        check += 1
    if not s_line[7].isdigit():
        check += 1
    if not (s_line[8].replace('\n', "")).isdigit():
        check += 1
    return check == 0


def main():
    """ func main"""
    len_input = 0
    dict_data = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
    i = 0
    try:
        while True:
            # take the input
            data = sys.stdin.readline()
            # print (data)
            # check the format
            # print(check_format(data))
            if not check_format(data):
                continue
            data_size = data.split(' ')[-1]
            len_input += int(data_size)
            status = data.split(' ')[-2]
            # if a status code doesn’t appear or is not an integer,
            # don’t print anything for this status code
            v = dict_data[status] + 1
            dict_data.update({status: v})
            # print (data )
            if i == 10:
                print(f"File size: {len_input}")
                # status codes should be printed in ascending order
                for k, v in sorted(dict_data.items()):
                    if v > 0:
                        print(f"{k}: {v}")
                i = 0
            i += 1
    except KeyboardInterrupt:
        print(f"File size: {len_input}")
        # status codes should be printed in ascending order
        for k, v in sorted(dict_data.items()):
            if v > 0:
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
