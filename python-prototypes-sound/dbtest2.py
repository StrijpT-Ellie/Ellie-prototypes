import audioop
import time
from math import log10

import matplotlib
import pyaudio
from PIL import Image

# matplotlib.use('TkAgg')

from scipy.signal import hilbert, chirp

p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 0.002
print(p.get_default_input_device_info())

def slope(y1, y2):
    #delta x is time between signals, for now that's 0,5s
    slope=(y2-y1)/(0.5)
    return slope

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

y1 = None
while stream.is_active():
    if rms != 0:
        db = 20 * -(log10(rms))
    else:
        db=60
    print(f"RMS: {rms} DB: {db}")
    y2 = db
    if db < 20:
        print("Het is stil")
    elif db > 60:
        print("Het is luid")
        print()
        img = Image.open('fobbys.png')
        img.show()
        time.sleep(1)
        img.close()
        time.sleep(1)
    # refresh every 0.5 seconds
    time.sleep(0.1)
    # print(y1)
    # print(y2)
    # if type(y1) == float:
    #     print("Helling:", slope(y1, y2))
    y1 = y2
    # print(type(y1))

stream.stop_stream()
stream.close()

p.terminate()
