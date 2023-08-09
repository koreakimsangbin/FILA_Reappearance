from processing import *

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
    processing('csi_0_01.dat')
    processing('csi_0_02.dat')
    processing('csi_0_03.dat')
    processing('csi_0_10.dat')
    processing('csi_0_100.dat')


