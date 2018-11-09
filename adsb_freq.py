def hexToDec(hexdec):
    dec = int(hexdec, 16)
    return bin(dec)[2:].zfill(56)

def df(frame):
    bin_frame = hexToDec(frame)
    df = int(bin_frame[0:5], 2)
    return df

fhandle = open('adsb_20181108_0.txt')
fr = dict()
for line in fhandle:
    fr[line[1:len(line)-2]] = fr.get(line[1:len(line)-2], 0) + 1
dict = list()
for hex, freq in fr.items():
    dict.append((hex, df(hex), freq))

for frame_hex, df_hex, frequency in dict:
    print("Frame:", frame_hex, "DF:", df_hex, "frequency: ", frequency)
