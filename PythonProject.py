import turtle
import os
import time
import random

#SetUpWindow
wn=turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("black")
wn.title("Space Invaders")

#Setting up Menu
menu_pen=turtle.Turtle()
menu_pen.speed(0)
menu_pen.setposition(0,200)
menu_pen.hideturtle()
menu_pen.color("purple")
menu_pen.write("Space Invaders",False,align="center",font=("System",60,"bold"))
menu_pen.up()

#Instructions
menu_pen.color("white")
menu_pen.setposition(0,50)
menu_pen.write("Shoot the aliens coming down before they hit your ship!\nYou only have three lives!", False, align="center",font=("System",18,"bold"))
menu_pen.setposition(0,-25)
menu_pen.write("Use the left and right arrow keys to move side to side\nand the space bar to shoot.", False, align="center",font=("System",18,"bold"))
menu_pen.setposition(0,-275)
menu_pen.color("purple")
menu_pen.write("Press ENTER to start",False,align="center",font=("System",35,"bold"))

def main_game():
    turtle.clearscreen()
    wn.bgcolor("black")
    wn.addshape("Space.gif")
    wn.addshape("Ship2.gif")
    wn.addshape("Alien1.gif")
    wn.bgpic("Space.gif")
    score_file = open("score_track.txt","w+")
    

    #DrawBorder
    border_pen = turtle.Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)

    #Score
    score = 0
    high_score= 0
    score_pen = turtle.Turtle()
    score_pen.color("white")
    score_pen.speed(0)
    score_pen.hideturtle()
    score_pen.penup()
    score_pen.setposition(160,310)

    #Lives
    lives = 3
    life_pen = turtle.Turtle()
    life_pen.color("white")
    life_pen.penup()
    life_pen.hideturtle()
    life_pen.speed(0)
    life_pen.setposition(370,250)   

    #Player
    player = turtle.Turtle()
    player.shape("Ship2.gif")
    player.penup()
    player.speed(0)
    player.setposition(0,-270)
    player.setheading(90)
    playerspeed = 8

    #MultipleEnemies
    num_of_enemies = 5
    enemies = []
    for i in range(num_of_enemies):
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.shape("Alien1.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)
    enemyspeed = 8  

    #Bullet
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5,0.5)
    bullet.hideturtle()
    bulletspeed = 50

    #MovingLeftAndRightAndBullet
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280    
        player.setx(x)
    
    def move_right():
        x = player.xcor()
        x +=playerspeed
        if x > 280:
            x = 280
        player.setx(x)   
        

    def fire_bullet():
    #Declare state as global if it needs changed
        global bulletstate
        bulletstate = "ready"
        if bulletstate == "ready":
            bulletstate = "fire"
            #MoveBulletAbovePlayer
            x = player.xcor()
            y = player.ycor() +10
            bullet.setposition(x,y)
            bullet.showturtle()

    def is_collided_with(a, b):
        return abs(a.xcor() - b.xcor()) < 20 and abs(a.ycor() - b.ycor()) < 20
            
    def quit_game():
        wn.bye()

    def game_over():
        
        wn.bgcolor("black")
        turtle.onkey(quit_game,"q")
        life_pen.setposition(600,600)
        menu_pen.setposition(0,200)
        menu_pen.write("Game Over",False,align="center",font=("System",60,"bold"))
        score_pen.setposition(0,0)
        score_pen.write("Score: {} High Score: {}".format(score,high_score),False,align="center", font=("System",18,"bold"))
        menu_pen.setposition(0,-100)
        menu_pen.write("Press Q to exit the game.",False,align="center", font=("System",18,"bold"))
    
    #KeyBoardBindings    
    turtle.onkeypress(move_left,"Left")
    turtle.onkeypress(move_right,"Right")    
    turtle.onkey(fire_bullet,"space")
    

    #MainGameLoop
    while True:
        for enemy in enemies:
            
        #MoveTheEnemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

        #MoveEnemyBackAcross
            if enemy.xcor() > 280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40                    
                    e.sety(y)
                enemyspeed *= -1
            
            if enemy.xcor() < -280:
                for e in enemies:                
                    y = e.ycor()
                    y -= 40                    
                    e.sety(y)
                enemyspeed *= -1
            if enemy.ycor() < -280:
                for e in enemies:
                    x = random.randint(-200,200)
                    y = random.randint(100,250)
                    enemy.setposition(x,y)
                    

            #Collision  
            if is_collided_with(bullet,enemy):
                #resetbullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                #resetenemy
                x = random.randint(-200,200)
                y = random.randint(100,250)
                enemy.setposition(x,y)
                
                score+=10                
                if score > high_score:
                    high_score = score            
                    
                score_pen.clear()           
                
            if is_collided_with(player,enemy):
                lives = lives - 1
                life_pen.clear()
                x = random.randint(-200,200)
                y = random.randint(100,250)
                enemy.setposition(x,y)
                if lives == 0:
                    turtle.clearscreen()
                    game_over()
                    

    #MoveBullet
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #BulletReachesTop
        if bullet.ycor() > 295:
            bullet.hideturtle()
            bulletstate = "ready"
            
    #WritingScore        
        score_pen.write("Score: {} High Score: {}".format(score,high_score),False,align="center", font=("System",18,"bold"))
        life_pen.write("Lives: {}".format(lives),False, align="center",font=("System",18,"bold"))        
                   

turtle.listen()
turtle.onkey(main_game,"Return")
wn.mainloop()
