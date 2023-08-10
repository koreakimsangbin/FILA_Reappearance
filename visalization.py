from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from triangulation import *
from processing import *

def visalization(A, B, C):
    distance1 = processing('csi_0_01.dat')
    distance2 = processing('csi_0_02.dat')
    distance3 = processing('csi_0_03.dat')
    D = cal_coordinate(A,B,C, distance1, distance2, distance3)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 삼각뿔의 면을 정의
    vertices = [list(A), list(B), list(C), list(D)]
    faces = [[vertices[0], vertices[1], vertices[3]], [vertices[0], vertices[2], vertices[3]],
             [vertices[1], vertices[2], vertices[3]], [vertices[0], vertices[1], vertices[2]]]

    # 삼각뿔의 각 면을 그리기
    for face in faces:
        poly3d = [[vertice[i] for vertice in face] for i in range(3)]
        ax.add_collection3d(Poly3DCollection([list(zip(*poly3d))], linewidths=1, edgecolors='r', alpha=.25))

    # 좌표축 범위 설정
    ax.set_xlim([0, 5])
    ax.set_ylim([0, 5])
    ax.set_zlim([0, 5])

    plt.show()
