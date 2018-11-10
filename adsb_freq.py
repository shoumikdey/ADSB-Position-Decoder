def hexToDec(hexdec):
    dec = int(hexdec, 16)
    return bin(dec)[2:].zfill(56)

def df(frame):
    bin_frame = hexToDec(frame)
    df = int(bin_frame[0:5], 2)
    return df

def getTC(frame):
    #frame = "8D40621D58C382D690C8AC2863A7"
    data = frame[8:22]
    bin = hexToDec(data)
    return int(bin[0:5],2)

fhandle = open('adsb_20181108_0.txt')
fr = dict()
for line in fhandle:
    fr[line[1:len(line)-2]] = fr.get(line[1:len(line)-2], 0) + 1
dict = list()
for hex, freq in fr.items():
    if df(hex) == 17:
        dict.append((hex, df(hex), getTC(hex), freq))
    else:
        dict.append((hex, df(hex), "NIL", freq))


for frame_hex, df_hex, tc, frequency in dict:
    if df_hex == 17:
        print("Frame:", frame_hex, "DF:", df_hex, "TC:", tc, "frequency: ", frequency)
