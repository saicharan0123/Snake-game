import sys,pygame,random
pygame.init()

size = width,height = 900,600

window = pygame.display.set_mode(size)
white = 155,200,150
red = 255,0,0
black = 0,0,0
pygame.display.update()

ball_x = 40
vel_x = 0
ball_y = 50
#leng = 10
#h_leng = 10
food_leng = 20
vel_y = 0
food_x=random.randint(0,width-10)
food_y=random.randint(0,height-10)
ball_len = 20
score = 0
fps = 30

clock=pygame.time.Clock()

bal_lis = []
bal_len =1

def plot_bal(window,color,bal_lis,ball_len):
    for x,y in bal_lis:
        pygame.draw.rect(window,color,[x,y,ball_len,ball_len])


while True:
    if ball_x >= width or ball_x < 0 or ball_y < 0 or ball_y >= height:
        print("game over")
        print("your total score : ",score)
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("your total score : ",score)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x = 5
                vel_y = 0
            if event.key == pygame.K_LEFT:
                vel_x = -5
                vel_y = 0
            if event.key == pygame.K_UP:
                vel_y = -5
                vel_x = 0
            if event.key == pygame.K_DOWN:
                vel_y = 5
                vel_x = 0
            # if event.key == pygame.K_e:
            #     score +=50
                # print(score)
    ball_x += vel_x
    ball_y += vel_y

    if abs(ball_x-food_x)<20 and abs(ball_y-food_y)<20:
        food_x=random.randint(10,width-10)
        food_y=random.randint(10,height-10)
        score += 10
        bal_len += 2
        fps+=5
        print(score)
    window.fill(white)
    #pygame.draw.rect(window,red,[ball_x,ball_y,leng,h_leng])
    pygame.draw.rect(window,red,[food_x,food_y,food_leng,food_leng])

    head = []
    head.append(ball_x)
    head.append(ball_y)
    bal_lis.append(head)

    if len(bal_lis)>bal_len:
        del bal_lis[0]
    plot_bal(window,black,bal_lis,ball_len)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()