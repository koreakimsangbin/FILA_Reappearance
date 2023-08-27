import os

from processing import *
from triangulation import *
from visalization import *
from train import *

"""
TODO

1. TIME DOMAIN MULTIPATH MITIGATION
    a. Perform IFFT: Convert the CSI information from the frequency domain to the time domain using Inverse Fast Fourier Transform (IFFT).

    b. Identify LOS and nearest NLOS: Analyze the time-domain CSI data to identify Line-of-Sight (LOS) and the nearest Non-Line-of-Sight (NLOS) components based on certain criteria or algorithms.

    c. Remove other components: Remove all CSI values except for the identified LOS and nearest NLOS components from the time-domain data.

    d. Perform FFT: Transform the remaining time-domain CSI data back to the frequency domain using Fast Fourier Transform (FFT).

2. FREQUENCY DOMAIN FADING COMPENSATION
    a. Use Time domain multipath mitigation to rewarded the fading
    
    
1번까지는 클리어
"""

"""
TODOLIST

1. h(t) 함수 구현
2. 구현해서 필터링한 값과 기존값 비교
3. 보상까지 구현

해결
"""

if __name__ == "__main__":

    delta, n, model = main_training(make_list())
    distance_list = []
    csieff_list = []


    for z in range(1, 4):
        for t in range(1, 6):
            for j in range(1, 6):
                for i in range(1,7):
                    if not os.path.exists('user4-1-' + str(z) + '-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat'):
                        #print(f"Warning: {'user4-1-1-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat'} does not exist. Skipping...")
                        continue
                    distance, csieff = processing('user4-1-' + str(z) + '-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat', delta, n)
                    distance_list.append(distance)
                    csieff_list.append(csieff)
    print("distance :", distance_list)
    print("CSIEFF :", csieff_list)
    plt.plot(distance_list, csieff_list, label='CSIEFF VS DISTANCE', color='red', linestyle='--')
    plt.xlabel('Distance')
    plt.ylabel('CSIeff Amplitude')
    plt.title('CSIEFF VS DISTANCE')
    plt.grid(True)
    plt.show()
    #고정 좌표 A, B, C
    A = (0, 0, 0)
    B = (4, 0, 0)
    C = (2,math.sqrt(12), 0)

    #visalization(A,B,C)
