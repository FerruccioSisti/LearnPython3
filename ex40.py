#This exercise is meant to help gain an understanding of how classes work
class Song(object):
    #This is like a constructor (note that there are TWO underscores on each side of init)
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singASong(self):
        for line in self.lyrics:
            print(line)

happyBDay = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bullsOnParade = Song(["They rally around tha family", "With pockets full of shells"])

happyBDay.singASong()
bullsOnParade.singASong()
