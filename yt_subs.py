FILE_SOURCE = './fiverr/trans.txt'
FILE_DESTINATION = './fiverr/trans_corrected.srt'

with open(FILE_SOURCE, "r") as handle:
    source_lines = handle.readlines()

linecount = []
timestamp = []
textstamp = []
timestamp_corrected = []
timestamp_split = []

# COUNT LINES IN YOUTUBE SUBTITlE FILE
for count in range(0, len(source_lines), 4):
    linecount.append(source_lines[count].strip('\n'))
    timestamp.append(source_lines[count + 1].strip('\n'))
    textstamp.append(source_lines[count + 2].strip('\n'))
    timestamp_split.append(((source_lines[count + 1].strip('\n')).split(' ')))
    timestamp_corrected.append(((source_lines[count + 1].strip('\n')).split(' ')))

# CORRECT TIMESTAMPS
for count in range(0, len(timestamp_corrected)-1):
    timestamp_corrected[count][2] = timestamp_corrected[count + 1][0]

# WRITE CORRECTED TIMESTAMPS
for count in range(0, len(linecount)):
    with open(FILE_DESTINATION,'a') as the_file:
        print(linecount[count] + '\n' + ' '.join(timestamp_corrected[count]) + '\n' + textstamp[count] + '\n', file=the_file)






        # print(*stamps_raw[i],file=the_file)


# print('Total Number of lines in YouTube subtitles : \t\t' +len(line))
# print('Number of lines in YouTube subtitles : \t\t' +linecount[len(linecount)-1])
# print(timestamp)
# print(timestamp_split)
# print(textstamp)
# print(timestamp_corrected)
# print(x)
#
# for i in range(0,len(linecount)):
#     with open('./fiverr/subtitles.srt','a') as the_file:
#         print(linecount[i] + '\n' + ' '.join(stamps_raw[i]) + '\n' + textstamp[i] + '\n', file=the_file)
#         # print(*stamps_raw[i],file=the_file)
#
# output
# 0 linecount
# 1 timestamp
# 2 text
# 3 blank 4
