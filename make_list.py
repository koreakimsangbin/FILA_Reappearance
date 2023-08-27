import os


def make_list():

    file_list = []
    for z in range(1, 4):
        for t in range(1, 6):
            for j in range(1, 6):
                for i in range(1,7):
                    if not os.path.exists('user4-1-' + str(z) + '-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat'):
                        #print(f"Warning: {'user4-1-1-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat'} does not exist. Skipping...")
                        continue
                    file_list.append('user4-1-' + str(z) + '-' + str(t) + '-' + str(j) + '-r' + str(i) + '.dat')

    return file_list