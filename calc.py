import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

type = 'host'
walls = {}
drainage_riser = {}
plums_coordinates = {}

def guestType():
    wallsNum = 5
    plumbing = ['раковина', 'унитаз']

def hostType():
    wallsNum = 3
    plumbing = ['раковина', 'душевая кабина или ванная', 'унитаз']
    height = int(input(f'Введите высоту стен  '))
    for i in range(wallsNum):
        width = int(input(f'Введите длину {i+1}-й  стены  '))
        depth = int(input(f'Введите глубину {i+1}-й  стены  '))
        walls[f'wall{i+1}'] = {'width':width, 'depth':depth, }
    # в четных стенах меняется z в нечетных х
    walls1_coordinate = [[0, 0, 0], [0, height, 0],   #левые точки
                    [walls.get('wall1').get('width'), 0, 0], [walls.get('wall1').get('width'), height, 0],    # правые точки

                     [0, 0, 0-walls.get('wall1').get('depth')], [0, height, 0-walls.get('wall1').get('depth')],
                     [walls.get('wall1').get('width'), height, 0-walls.get('wall1').get('depth')],[walls.get('wall1').get('width'), 0, 0-walls.get('wall1').get('depth')]]
    
    x0 = walls1_coordinate[3][0]
    walls2_coordinate =[[x0, 0, 0], [x0, height, 0],
                     [x0, 0, walls.get('wall2').get('width')], [x0, height, walls.get('wall2').get('width')],
                     
                     [x0+walls.get('wall2').get('depth'), 0, 0], [x0+walls.get('wall2').get('depth'), height, 0],
                     [x0+walls.get('wall2').get('depth'), 0, walls.get('wall2').get('width')], [x0+walls.get('wall2').get('depth'), height, walls.get('wall2').get('width')]]

    z0 = walls2_coordinate[3][2]
    walls3_coordinate = [[x0, 0, z0], [x0, height, z0], 
                     [x0-walls.get('wall3').get('width'), 0, z0+walls.get('wall2').get('depth')], [x0-walls.get('wall3').get('width'), height, z0+walls.get('wall2').get('depth')],

                     [x0, 0, z0], [x0, height, z0],
                     [x0-walls.get('wall3').get('width'), 0, z0+walls.get('wall2').get('depth')], [x0-walls.get('wall3').get('width'), height, z0+walls.get('wall2').get('depth')]]
    
    for i in wallsNum:
        plt.figure(i) # добавить прямоугольники отображающие стены !!!
      
    plt.show()
    for plum in plumbing:
        check = input(f"В вашем проекте будет {plum}? Введите + если да, - если нет     ")
        if check == '+':
            x,y,z = input(f'Введите координаты точек подключения {plum} x, y, z через запятую     ').split(',')
            int(x)
            int(y)
            int(z)
            plums_coordinates[f'{plum}'] = {'x':x, 'y':y, 'z':z}
            fromPlumToTarget(plum, drainage_riser)




    return {'wall1': walls1_coordinate, 'wall2':walls2_coordinate, 'wall3': walls3_coordinate}

def dualType():
    plumbing = ['раковина хоз', 'душевая кабина', 'унитаз хоз', 'раковина гост', 'унитаз гост']
    wallsNum = 5

def whichWall(target):
    for wall in walls:
        if target.get('x') == wall.get('x') and target.get('z') == wall.get('z'):
            return wall

def fromPlumToTarget(plum, target):
    #сравниваем высоту сантех прибора и стояка
    plumHeight = plum.get('y')
    targetheight = target.get('y')
    # d - разница
    if plumHeight > targetheight:
        d = plumHeight - targetheight
    elif plumHeight < targetheight:
        d = targetheight - plumHeight
    x = plum.get('x') #plot!!!!
    y = target.get('y')
    z = plum.get('z')
    #сравниваем стены прибора и стояка
    plumWall = whichWall(plum)
    goal = False
    while goal == False:
        if plumWall == drainageWall:
            #если они на одной и той же стене пишем координаты
            d += abs(x-target.get('x'))
            d += abs(z-target.get('z')) #сохраняем разницу длины
            x = target.get('x')#plot!!!!
            z = target.get('z')
            goal = True
            return {'Длина трубы':'d'}
        elif list(plumWall.keys()) < list(drainageWall.keys()): #если plumWall лежит влево от drainageWall
            coord = walls_coordinate.get(plumWall.keys()) # вершины стены
            str = list(plumWall.keys())[0]
            num = str[len(str)-1]
            if num % 2 == 0:
                z = coord[0][2] #plot!!!!
            else:
                x = coord[0][1]
        elif list(plumWall.keys()) > list(drainageWall.keys()): #если plumWall лежит влево от drainageWall
            coord = walls_coordinate.get(plumWall.keys())
            str = list(plumWall.keys())[0]
            num = str[len(str)-1]
            if num % 2 == 0:
                z = coord[3][2] #plot!!!!
            else:
                x = coord[3][1]
                




if type == 'host':
    walls_coordinate = hostType()
elif type == 'guest':
    walls_coordinate = guestType()
elif type =='dual':
    walls_coordinate = dualType()


target_x,target_y,target_z = input('Введите координаты стояка x, y, z через запятую      ').split(',')
int(target_x)
int(target_y)
int(target_z)
drainage_riser = {'x':target_x, 'y':target_y, 'z':target_z}

drainageWall = whichWall(drainage_riser)





#print(walls)

#height = 200
#walls={'wall1': {'width': 400, 'depth': 50}, 'wall2': {'width': 200, 'depth': 50}, 
#       'wall3': {'width': 400, 'depth': 50}, 'wall4': {'width': 200, 'depth': 50}}