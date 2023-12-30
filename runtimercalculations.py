import time 

a = 0.0139285714286
b = 1.23571428571
c = - 0.249642857143

def timercalculation(level):
        time_formula = float(((a * (level**2)) + (b * level) + c))
        sleeptime = round(time_formula, 2)
        if sleeptime <60.0:
            print(f'Time to wait = {sleeptime}s')
        elif sleeptime <3600.0:
            print(f'Time to wait = {round(sleeptime/60, 0)}m {int(sleeptime % 60)}s')
        elif sleeptime < 3600.0 * 60:
            hours = round(sleeptime/60, 0)
            minutes = int(sleeptime % 60)
            print(f'Time to wait = {hours}h {minutes}m')

