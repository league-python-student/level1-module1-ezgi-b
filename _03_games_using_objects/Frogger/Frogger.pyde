
def setup():
    # 1. Use the size function to set the size of your sketch
    size(700, 500)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    global bg, frog, frog_x, frog_y, cars
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    frog_x = 350
    frog_y = 450
    cars = list()
    for i in range(5):
        cars.append(Car(random(0, 700), 125 + i*65, 120, random(-5, 5)))
    
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(700, 500)
    frog.resize(40, 40)
    
def draw():
    global bg, frog, frog_x, frog_y, cars

    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    move()
    image(frog, frog_x, frog_y)

    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    for car in cars:
        car.update()
        car.draw()
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    for car in cars:
        if frog_x + 40 > car.x and frog_x < car.x + car.length and frog_y + 40 > car.y and frog_y < car.y + car.length/3:
            frog_x = 350
            frog_y = 450
    # 9. Create more car objects of different lengths, speed, and size

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
    
def move():
    global frog_y, frog_x
    if key == CODED:
        if keyCode == UP:
            frog_y -= 1
        elif keyCode == DOWN:
            frog_y += 1
        elif keyCode == LEFT:
            frog_x -= 1
        elif keyCode == RIGHT:
            frog_x += 1
    
