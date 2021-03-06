#kyDoleuc04
#Final Project

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame, TextAsset

pink = Color(0xFF00FF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x39ff14, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
yellow = Color(0xffff00, 1.0)

print("Press Space to propel your bird upwards")
print("Use the arrow keys to move your bird left and right")

class Bird(Sprite):
    side = LineStyle(1,black)
    poly = RectangleAsset(10,10,side,yellow)
    def __init__(self,position):
        super().__init__(Bird.poly,position)
        self.vx = 0
        self.vy = 0
        self.deltavy = 0.1
        
        Game.listenKeyEvent("keydown", "space", self.up)
        Game.listenKeyEvent("keyup", "space", self.down)
        Game.listenKeyEvent("keydown", "right arrow",  self.right)
        Game.listenKeyEvent("keyup", "right arrow",  self.rightstop)
        Game.listenKeyEvent("keydown", "left arrow",  self.left)
        Game.listenKeyEvent("keyup", "left arrow",  self.leftstop)
        
    def up(self, event):
        self.vy += -0.12
        self.deltavy = 0
    
    def down(self, event):
        self.deltavy = 0.06
        self.vy += 0.08
        
    def right(self, event):
        self.vx += 0.1
    
    def rightstop(self, event):
        self.vx += 0
        
    def left(self, event):
        self.vx += -0.1
        
    def leftstop(self, event):
        self.vx += 0
        
    def step(self):
        global restrict
        self.y += self.vy
        self.x += self.vx
        self.vy += self.deltavy
        if self.y >= 613:
            self.y = 613
            self.deltavy = -0.05
        elif self.y <=8:
            self.y = 8
            self.deltavy = 0.05
        if self.x <= 10:
            self.x = 10
        elif self.x >= 1125:
            self.x = 1125

class Block(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(30,30,side,green)
    def __init__(self,position):
        super().__init__(Block.square,position)

class Bottom(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(1300,10,side,black)
    def __init__(self,position):
        super().__init__(Bottom.square,position)

class Top(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(1300,10,side,black)
    def __init__(self,position):
        super().__init__(Top.square,position)

class LeftSide(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(10,800,side,black)
    def __init__(self,position):
        super().__init__(LeftSide.square,position)

class RightSide(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(10,800,side,black)
    def __init__(self,position):
        super().__init__(RightSide.square,position)

class Start(Sprite):
    side = LineStyle(1,blue)
    square = RectangleAsset(30,10,side,blue)
    def __init__(self,position):
        super().__init__(Start.square,position)

class Finish(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(130,10,side,yellow)
    def __init__(self,position):
        super().__init__(Finish.square,position)

class Text(Sprite):
    text = TextAsset("Flappy Bird XTREME", style = "bold 40pt Arial", width=250, fill=yellow)
    def __init__(self,position):
        super().__init__(Text.text,position)

class FinishText(Sprite):
    text = TextAsset("Finish!", style = "bold 20pt Arial", width=250, fill=black)
    def __init__(self,position):
        super().__init__(FinishText.text,position)

class Game(App):
    def __init__(self):
        super().__init__()
        self.player1 = Bird((10,250))
        for x in range(0,15):
            Block((100,(x*30)))
        for x in range(18,30):
            Block((100,(x*30)))
        for x in range(0,10):
            Block((250,(x*30)))
        for x in range(13,30):
            Block((250,(x*30)))
        for x in range(0,8):
            Block((400,(x*30)))
        for x in range(11,30):
            Block((400,(x*30)))
        for x in range(0,17):
            Block((550,(x*30)))
        for x in range(20,30):
            Block((550,(x*30)))
        for x in range(0,4):
            Block((700,(x*30)))
        for x in range(7,30):
            Block((700,(x*30)))
        for x in range(0,3):
            Block((850,(x*30)))
        for x in range(6,30):
            Block((850,(x*30)))
        
        Bottom((0,625))
        Top((0,-2))
        LeftSide((-2,0))
        RightSide((1137,0))
        #Start((12,300))
        Finish((950,300))
        Text((900,30))
        FinishText((975,310))
    
    def step(self):
        global restrict
        self.player1.step()
        if self.player1.collidingWithSprites(Block):
            self.player1.destroy()
            print("GAME OVER :(((")

        #if self.player1.collidingWithSprites(Start):
            #self.player1.y = 290
            #self.player1.deltavy = -0.01

        if self.player1.collidingWithSprites(Finish):
            self.player1.y = 290
            print("You Win!!!!")

myapp = Game()
myapp.run()