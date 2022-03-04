import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

# returns rage number
def anylasis(number):

    rage = 1 / (1 + (np.e ** ((number/100000) * -1)))
    rage = rage * 1000

    return rage

def output(text):
    print(text)

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

    print("processing sample.wav")
    tempRage = anylasis(raw[0])
    totalRage = 0
    values = 0
    for i in raw:
        if anylasis(i) > tempRage:
            tempRage = anylasis(i)
        if i >= 0:
            totalRage = totalRage + anylasis(i)
            values = values + 1
        else:
            totalRage = totalRage - anylasis(i)
            values = values + 1

    maxRage = tempRage
    avgRage = totalRage / values

    Time = np.linspace(0,len(raw) / sampleRate, num=len(raw))

    plt.title("Highest Spike = " + str(maxRage) + ", Average Rage = " + str(avgRage))
    plt.plot(Time, anylasis(raw), color="red")
    plt.ylabel("Rage")
    plt.show()

    wav.close()


# maximum rage = 1000
