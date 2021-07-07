# import pyaudio
# import speech_recognition as sr
# print(sr.Microphone.list_microphone_names())


# print('\navailable devices:')

# for i in range(pyaudio_instance.get_device_count()):
#     dev = pyaudio_instance.get_device_info_by_index(i)
#     name = dev['name'].encode('utf-8')
#     print(i, name, dev['maxInputChannels'], dev['maxOutputChannels'])

# print('\ndefault input & output device:')
# print(pyaudio_instance.get_default_input_device_info())
# print(pyaudio_instance.get_default_output_device_info())

# import pyttsx3
# engine = pyttsx3.init('dummy')

import pyttsx3
# engine = pyttsx3.init('dummy')
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()