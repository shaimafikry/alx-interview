#!/usr/bin/python3
""" script that reads stdin line by line and
computes metrics
"""

len_input = 0
dict_data = {}
i = 0
while True:
    data = input()
    len_input += len(data)
    status = data.split(' ')[-2]
    # if a status code doesn’t appear or is not an integer,
    # don’t print anything for this status code
    if status.isdigit():
        dict_data.update({status: i})
    # print (data )
    if i == 10 or data == KeyboardInterrupt:
        print(f"File size: {len_input}")
        # status codes should be printed in ascending order
        for k, v in sorted(dict_data.items()):
            print(f"{k}: {v}")
        i = 0
    i += 1
