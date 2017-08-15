#taken from https://alala666888.wordpress.com/2010/06/06/opengl2d-draw-points-and-lines/

import OpenGL
import math
OpenGL.ERROR_ON_COPY = True

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, 500.0, 0.0, 500.0)

def rotatePoint(x,y, centerOfMass, f):
    x = centerOfMass[0] + ((x-centerOfMass[0])*math.cos(f)-(y-centerOfMass[1])*math.sin(f))
    y = centerOfMass[1] + ((x-centerOfMass[0])*math.sin(f)+(y-centerOfMass[1])*math.cos(f))
    return x,y

f=0
degreesOfRotation=0
new_degrees=0

import time


meanshapeVec =[
(230.9375 ,161.3125) ,
(230.9375 ,166.) ,
(231.0625 ,170.625) ,
(231.625 ,175.1875),
(232.1875 ,179.9375),
(233.1875 ,184.375 ),
 (235. ,188.1875) ,
 (237.75  ,187.9375) ,
 (240.  ,184.4375) ,
 (242.75  ,181.1875) ,
 (245.6875,178.5)  ,
 (249.3125,175.875),
 (253.3125,173.75 ),
 (256.9375, 171.8125),
 (261.  ,170.9375 ),
 (265.125 , 170.6875) ,
 (269.75  ,171.5  ),
 (274.125 ,173.375 ),
 (278.25   ,174.9375),
 (281.8125  ,175.375),
 (283.5625 , 174.  ),
 (284.0625 ,170.8125) ,
 (283.1875 ,166.5625) ,
 (281.375 , 162.5 ) ,
 (279.875 ,158.5 ) ,
  (278.0625 ,154.625 ) ,
  (275.4375 ,151.4375 ) ,
  (271.8125 ,149.25),
  (268.25  ,147.625 ),
 (264.1875 ,146.1875),
 (260.1875 ,145.4375) ,
 (255.875  ,145.3125) ,
 (251.9375 ,146.25 ) ,
 (248.5625  ,148.5625) ,
 (245.3125 ,151.1875) ,
 (241.8125 ,153.4375 ),
 (238.3125 ,155.6875 ),
 (235.5 , 157.5)
 ]

'''
meanshapeVec = [(50,50),(100,50),(50,100),(100,100)]
'''

#https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
def rotate(x,y, centerofmass, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = centerofmass.x, centerofmass.y


    qx = ox + math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy)
    qy = oy + math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy)
    return qx, qy

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    #glClearColor(0.0, 0.0, 0.0, 0.0);


    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)

    #draw two points
    glBegin(GL_POINTS)
    '''
    for i in range(0,1):

        global f
        f+=0.1
        time.sleep(0.05)


        leftPoint=(50,50)
        rightPoint=(100,50)
        upPoint=(75,25)
        downPoint=(75,75)
        centerOfMass=( ((leftPoint[0]+rightPoint[0]+upPoint[0]+downPoint[0])/4)  ,  ((leftPoint[1]+rightPoint[1]+upPoint[1]+downPoint[1])/4) )

        #left point
        #x,y=rotatePoint(leftPoint[0], leftPoint[1] , centerOfMass, f)
        x,y=rotate(leftPoint[0], leftPoint[1] , centerOfMass, f)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2i(int(x),int(y))

        #right point
        #x,y=rotatePoint(rightPoint[0], rightPoint[1] , centerOfMass, f)
        x,y=rotate(rightPoint[0], rightPoint[1] , centerOfMass, f)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2i(int(x),int(y))

        #up point
        #x,y=rotatePoint(upPoint[0], upPoint[1] , centerOfMass, f)
        x,y=rotate(upPoint[0], upPoint[1] , centerOfMass, f)
        glColor3f(1.0, 1.0, 0.0)
        glVertex2i(int(x),int(y))

        #down point
        #x,y=rotatePoint(downPoint[0], downPoint[1] , centerOfMass, f)
        x,y=rotate(downPoint[0], downPoint[1] , centerOfMass, f)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2i(int(x),int(y))
        '''




    #Transformation recalculation
    sumx=0
    sumy=0
    global meanshapeVec
    for pt in (meanshapeVec):
        #print pt
        sumx+=pt[0]
        sumy+=pt[1]
    sumx/=len(meanshapeVec)
    sumy/=len(meanshapeVec)

    from testInitASM import Point
    centerOfMass = Point(sumx,sumy)
    global degreesOfRotation
    new_degrees=1
    degreesOfRotation+=new_degrees#-15

    #Now rotate each point individual with respect to its centerOfMass
    counter=0
    for pt in meanshapeVec:
        counter+=1
        #print pt
        global f
        #f+=1
        time.sleep(0.0001)

        x,y=rotate(pt[0], pt[1] , centerOfMass, degreesOfRotation*(math.pi/180.0))#
        #print x,y
        if counter==1:
            print x,y
        glColor3f(1.0, 0.0, 0.0)
        glVertex2i(int(x),int(y))






    glEnd()

    #draw a line
    #glBegin(GL_LINES)
    #glVertex2i(10,10)
    #glVertex2i(100,100)
    #glEnd()

    glFlush()

    glutPostRedisplay(); #//everytime you are done                            // drawing you put it on the screen

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('points and lines')
init2D(0.0,0.0,0.0)
glutDisplayFunc(display)
glutMainLoop()

