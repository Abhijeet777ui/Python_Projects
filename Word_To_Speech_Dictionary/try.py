import pyttsx3
from PyDictionary import PyDictionary


class Speaking:

	def speak(self, audio):
	
		
		engine = pyttsx3.init('sapi5')
		
		voices = engine.getProperty('voices')
		
		engine.setProperty('voice', voices[0].id)
		engine.say(audio)
		engine.runAndWait()


class GFG:
	def Dictionary(self):
		speak = Speaking()
		dic = PyDictionary()
		speak.speak("What's Your Word?")
		
		query = str(input()) # Taking the string input
		word = dic.meaning(query)
		print(len(word))
		
		for state in word:
			print(word[state])
			speak.speak("the meaning is" + str(word[state]))


if __name__ == '__main__':
	GFG()
	GFG.Dictionary(self=None)
