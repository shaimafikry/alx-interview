#!/usr/bin/python3
'''script that reads stdin line by line and
computes metrics
'''
import sys
# libray deals with regex
import re

# pattern to be checked
log_patt = re.compile(
  r'^(\S+) - \[(.*?)\] "GET /projects/\d+ HTTP/1.1" (\d{3}) (\d+)$'
)


def check_format(line):
    """check format of input"""
    # .strip to remove any trailing whitespaces and \n
    return log_patt.match(line.strip()) is not None


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
            if not data:
                break
            # print (data)
            # check the format
            # print(check_format(data))
            if not check_format(data):
                continue

            parts = data.split()
            # to skip lines that doesnt meet the criteria
            try:
                data_size = int(parts[-1])
                status = parts[-2]
            except (IndexError, ValueError):
                continue  # Skip malformed lines
            # if a status code doesn’t appear or is not an integer,
            # don’t print anything for this status code

            if status in dict_data:
                dict_data[status] += 1
                len_input += data_size

            i += 1
            # print (data )
            if i % 10 == 0:
                print(f"File size: {len_input}")
                # status codes should be printed in ascending order
                for k, v in sorted(dict_data.items()):
                    if v > 0:
                        print(f"{k}: {v}")

                # return to zero
                dict_data = {key: 0 for key in dict_data}
                len_input = 0
                i = 0

    except KeyboardInterrupt:
        print(f"File size: {len_input}")
        # status codes should be printed in ascending order
        for k, v in sorted(dict_data.items()):
            if v > 0:
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
