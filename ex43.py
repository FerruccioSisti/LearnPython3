#Exercise to understand object-oriented analysis through a game

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, sceneMap):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class ControlCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, startScene):
        pass

    def nextScene(self, sceneName):
        pass

    def openingScene(self):
        pass


aMap = Map("centralCorridor")
aGame = Engine(aMap)
aGame.play()
