#The goal of this exercise is to make a game entirely on our own
#The requirements are that we;
#Use more than one file, utilizing import to use them,
#Use one class PER room
import rooms
from textwrap import dedent

#This class is a map of all the scenes we will be utilizing
class Map(object):

    #Dict of scene strings to actual scenes
    scenes = {
        'death': rooms.Death(),
        'finished': rooms.Finished(),
        'pannitto_house': rooms.PannittoHouse(),
        'outside': rooms.Outside(),
        'simons_room': rooms.SimonsRoom(),
        'parents_room': rooms.ParentsRoom(),
        'julias_room': rooms.JuliasRoom()
    }

    def __init__(self, startScene):
        #Set the first scene
        self.startScene = startScene

    #Method for getting the next scene
    def nextScene(self, sceneName):
        name = Map.scenes.get(sceneName)
        return name

    #Method to get the starting scene
    def openingScene(self):
        return self.nextScene(self.startScene)

#This class is what plays each scene
class Engine(object):
    #initialize the engine with a map of scenes to use
    def __init__(self, sceneMap):
        self.sceneMap = sceneMap

    #This method starts the game and plays each scene
    def play(self):
        currentScene = self.sceneMap.openingScene()
        #Set the last scene to be the 'finished' scene
        lastScene = self.sceneMap.nextScene("finished")

        #loop until you receive info that says the game should
        #be done
        while currentScene != lastScene:
            #Set the next scene to be whatever is returned
            #by the current scene
            nextSceneName = currentScene.enter()
            #Move to next scene
            currentScene = self.sceneMap.nextScene(nextSceneName)

        #Play out the final scene
        currentScene.enter()

#Create a map of the pannitto house scenes with the
#opening scene being the 'PannittoHouse' scene
pannittoMap = Map("pannitto_house")
pannittoGame = Engine(pannittoMap)
pannittoGame.play()
