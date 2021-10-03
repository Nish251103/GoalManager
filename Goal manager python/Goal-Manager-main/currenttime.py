from datetime import datetime
import pygame

def currenttimee():
    try:

        pygame.init()

        #icon = pygame.image.load('digitalClock.png')
        #pygame.display.set_icon(icon)

        screen = pygame.display.set_mode((430,180))
        pygame.display.set_caption('Digital Clock')
        bigFont = pygame.font.SysFont('DS-Digital',130)#Comic Sans MS
        smallFont = pygame.font.SysFont('DS-Digital',30)

        white = (255,255,255)
        black = (0,0,0)
        green = (0,255,0)

        months = ['January', 'February', 'March', 'April', 'May', 
        'June', 'July', 'August', 'September', 'October', 'November', 'December']
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

        running = True
        while running:
            screen.fill(black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    
            now = datetime.now()
            today = datetime.today()

            minute = now.strftime('%M:%S')
            hour = int(now.strftime('%H'))
            month = int(now.strftime('%m'))
            year = now.strftime("%d %Y")
            day = today.weekday()
            day = days[day]
            month = months[month-1]
            
            am = 'AM'
            
            if hour > 12:
                hour = hour-12
                am = 'PM'
            
            time = f'{hour}:{minute}'
            timeText = bigFont.render(time,True,green)
            monthText = smallFont.render(month,True,green)
            yearText = smallFont.render(year,True,green)
            amText = smallFont.render(am,True,green)
            dayText = smallFont.render(day,True,green)

            screen.blit(timeText, (15,20))
            screen.blit(monthText, (15,150))
            screen.blit(yearText, (145,150))
            screen.blit(amText,(380,0))
            screen.blit(dayText,(280,150))

            pygame.display.update()
    except:
        return None

