from OpenGL.GLUT.freeglut import *   #新版本的glut
import ctypes
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import shaders
import numpy as np

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0)
    glDrawArrays(GL_POINTS, 0, 1)
    glDisableVertexAttribArray(0)
    glutSwapBuffers()

def buffer():
    global VBO
    vertices = np.array([0.0 , 0.0 , 0.0],dtype="float32")
    VBO = glGenBuffers(1)    #创建对象
    glBindBuffer(GL_ARRAY_BUFFER , VBO)  #绑定
    glBufferData(GL_ARRAY_BUFFER , vertices.nbytes , vertices , GL_STATIC_DRAW)  #输入数据

def main():
    glutInit([])
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # 显示模式 双缓存
    glutInitWindowPosition(100, 100)  # 窗口位置
    glutInitWindowSize(500, 500)  # 窗口大小
    glutCreateWindow("point")  # 创建窗口
    glutInitContextVersion(4,3)   #为了兼容
    glutInitContextProfile(GLUT_CORE_PROFILE)   #为了兼容
    glutDisplayFunc(Draw)  # 回调函数
    glClearColor(0.0, 0.0, 0.0, 0.0)
    buffer()
    glutMainLoop()


main()
