class Paddle():
    def __init__(self, x, y=None, paddle_width=30, paddle_height=150):
        self.x = x
        self.y = height - paddle_height
        self.width = paddle_width
        self.height = paddle_height
        self.y_speed = 0
        
        if y is not None:
            self.y = y
        
    def update(self):
        if (self.y + self.y_speed >= 0) and (self.y + self.y_speed <= height - self.height):
            self.y += self.y_speed
        
    def draw(self):
        push()
        fill(255)
        rect(self.x, self.y, self.width, self.height)
        pop()
