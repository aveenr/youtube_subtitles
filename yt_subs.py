with open("subtitles.txt", "r") as handle:
    line = handle.readlines()
print(len(line))
linecount = []
timestamp = []
textstamp = []
stamps = []
split_time = []
stamps_raw = []
# 0 linecount 1 timestamp 2 text 3 blank 4

for i in range(0,len(line),4):
    linecount.append(line[i].strip('\n'))
print(linecount)

for i in range(1,len(line),4):
    timestamp.append(line[i].strip('\n'))
    stamps_raw.append(((line[i].strip('\n')).split(' ')))
print(timestamp)

for i in range(2,len(line),4):
    textstamp.append(line[i].strip('\n'))
print(textstamp)

for i in range(1,len(line),4):
    stamps.append(line[i].strip('\n'))
    stamps_raw.append(((line[i].strip('\n')).split(' ')))
for i in range(0,len(stamps_raw)-1):
    stamps_raw[i][2] = stamps_raw[i+1][0]

for i in range(0,len(linecount)):
    with open('my_subs.srt','a') as the_file:
        print(linecount[i] + '\n' + ' '.join(stamps_raw[i]) + '\n' + textstamp[i] + '\n', file=the_file)
        # print(*stamps_raw[i],file=the_file)

