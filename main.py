import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def output(text):
    # Use a breakpoint in the code line below to debug your script.
    print(text)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wav = wave.open('sample.wav', 'r')

    raw = wav.readframes(-1)
    raw = np.frombuffer(raw, dtype='int16')
    sampleRate = wav.getframerate()

    '''
    if wav.getnchannels() == 2:
        print("Use Mono")
        wav.close()
        sys.exit(0)
    '''



    print("sample.wav is : ")
    tempRage = raw[0]
    totalRage = 0
    values = 0
    for i in raw:
        if i > tempRage:
            tempRage = i
        if i >= 0:
            print(i, end=' ')
            totalRage = totalRage + i
            values = values + 1
        else:
            print(-i, end=' ')
            totalRage = totalRage - i
            values = values + 1

    maxRage = tempRage
    avgRage = totalRage / values
    #print(maxRage)

    Time = np.linspace(0,len(raw) / sampleRate, num=len(raw))

    plt.title("MaxRage = " + str(maxRage) + ", AvgRage = " + str(avgRage))
    plt.plot(Time, raw, color="red")
    plt.ylabel("Rage")
    plt.show()




    wav.close()


# maxium rage = 1000




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
