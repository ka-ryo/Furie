import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt

def ReadWavFile(FileName):
    try:
        wr = wave.open(FileName, "r")
    except FileNotFoundError: #ファイルが存在しなかった場合
        print("[Error 404] No such file or directory: " + FileName)
        return 0
    data = wr.readframes(wr.getnframes())
    wr.close()
    x = np.frombuffer(data, dtype="int16") / float((2^15))

    #音声波形表示
    plt.figure(figsize=(15,3))
    plt.plot(x)
    plt.show()
    

    #--------------------------------------------------------------------------
    #        おまけ：numpyで高速フーリエ変換して、グラフ表示
    #--------------------------------------------------------------------------
    x = np.fft.fft(np.frombuffer(data, dtype="int16"))
    plt.figure(figsize=(15,3))
    plt.plot(x.real[:int(len(x)/2)])
    plt.show()
    
    
if __name__ is "__main__":
    ReadWavFile("original.wav") 