import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

# returns rage number
def anylasis(number):
    '''
    rage = 1 / (1 + (np.e ** (number * -1)))
    rage = rage * 1000
    '''

    rage = number / 60
    # rage = number

    return rage



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
    tempRage = anylasis(raw[0])
    totalRage = 0
    values = 0
    for i in raw:
        if anylasis(i) > tempRage:
            tempRage = anylasis(i)
        if i >= 0:
            #print(i, end=' ')
            totalRage = totalRage + anylasis(i)
            values = values + 1
        else:
            #print(-i, end=' ')
            totalRage = totalRage - anylasis(i)
            values = values + 1

    maxRage = tempRage
    avgRage = totalRage / values
    #print(maxRage)

    Time = np.linspace(0,len(raw) / sampleRate, num=len(raw))

    plt.title("MaxRage = " + str(maxRage) + ", AvgRage = " + str(avgRage))
    plt.plot(Time, anylasis(raw), color="red")
    plt.ylabel("Rage")
    plt.show()




    wav.close()


# maxium rage = 1000




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
