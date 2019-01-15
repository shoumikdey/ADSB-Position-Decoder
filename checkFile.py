from functions import *
from crc import crcheck
fhandle = open('adsb_test.txt')
while True:
    line1 = fhandle.readline().strip()
    line2 = fhandle.readline().strip()
    if not line2: break  # EOF
    #print(hexToDec(line1), line2)
    frame_1 = hexToDec(line1[8:22])[21]
    frame_2 = hexToDec(line2[8:22])[21]
    frame_1_1 = hexToDec(line1[8:22])
    frame_2_2 = hexToDec(line2[8:22])
    #print(frame_1, frame_2)
    bin_alt = frame_2_2[8:20]
    if(frame_1 != frame_2):
        if(frame_2 == "1"):
            bin_lat_odd = frame_2_2[22:39]
            bin_lat_even = frame_1_1[22:39]
            bin_long_even = frame_1_1[39:]
            bin_long_odd = frame_2_2[39:]
            print("ICAO", line1[2:7])
            print(line1)
            print(line2)
            crcheck(line1)
            crcheck(line2)
            print("latitude:", latitude(bin_lat_even, bin_lat_odd, 0, 1))
            print("longitude:", longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 0, 1, latitude(bin_lat_even, bin_lat_odd, 0, 1)))
            print("Altitude:",altitude(bin_alt),"ft OR", (altitude(bin_alt)*0.3048),"m")
        elif(frame_2 == "0"):
            bin_lat_odd = frame_1_1[22:39]
            bin_lat_even = frame_2_2[22:39]
            bin_long_even = frame_2_2[39:]
            bin_long_odd = frame_1_1[39:]
            print("ICAO", line1[2:7])
            print(line1)
            print(line2)
            crcheck(line1)
            crcheck(line2)
            print("latitude:", latitude(bin_lat_even, bin_lat_odd, 1, 0))
            print("longitude:", longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 1, 0, latitude(bin_lat_even, bin_lat_odd, 1, 0)))
            print("Altitude:",altitude(bin_alt),"ft OR", (altitude(bin_alt)*0.3048),"m")
        print()
fhandle.close()
