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


import webbrowser
import random
import pyttsx3
# # engine = pyttsx3.init('dummy')
engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()
    

# listSimilarity to compare the voice data with every fxn's list


#CREATING A GLOBAL MAXIMUM_VAL TO STORE THE INDEX OF SELECTED FUNCTION

selectedFxnIndex = -1


def listSimilarity(fxn_data,index, voice_data):
    # max value of count till now

    global selectedFxnIndex
    maxCount= 0
    simList= list(set(fxn_data) & set(voice_data))
    # count of similar elements in both the lists
    count= len(simList)
    if(count>maxCount):
        selectedFxnIndex= index
        maxCount= count

    # return index


# greeting fxn
def greeting():

    ind= 1
    l1= ['hey','hi','hola','hello','wassup']
    return ind, l1

def playYoutube():

    # change ind to 6 later on
    ind= 2
    l6= (["search","youtube","play","song"])
    return ind, l6

lemmatized_output= ['search','song',"astronaut",'in','the','ocean']
voice_data= "search for the song astronaut in the ocean"

# greetings
ind1,l1= greeting()
# index variable to check if this function will be executed or not
listSimilarity(l1,ind1,lemmatized_output)

print(selectedFxnIndex)

#youtube (temporary)
ind2,l2= playYoutube()
# index variable to check if this function will be executed or not
listSimilarity(l2,ind2,lemmatized_output)


print(selectedFxnIndex)


if(selectedFxnIndex== ind1):
    greetings=["Hi sir, What we gonna do today?", "Hi sir, what are we doing today?", "Hi sir, How can i help you?"]
    greet=greetings[random.randint(0,len(greetings)-1)]
    engine_speak(greet)



elif(selectedFxnIndex== ind2):
    search_term=voice_data.split("for")[-1]
    print("search term is " ,search_term)
    url="https://www.youtube.com/results?search_query="+ search_term
    webbrowser.get().open(url)
    engine_speak("Here is what i found for "+ search_term + "on youtube")