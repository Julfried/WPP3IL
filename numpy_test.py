import math
import numpy as np
import matplotlib.pyplot as plt

frame = r"C:\Users\Julian\OneDrive - FH OOe\Kurse\3. Semester\WPP3IL\images\frame_color.png"
stinkbug = r"C:\Users\Julian\OneDrive - FH OOe\Kurse\3. Semester\WPP3IL\images\stinkbug_color.png"


size_x, size_y = (78, 435), (80, 351)
stinkbug = plt.imread(stinkbug)
frame = plt.imread(frame)
frame_image_size = np.zeros_like(frame[size_x[0]:size_x[1], size_y[0]:size_y[1]])

subimg = stinkbug[0:frame_image_size.shape[0], 110:frame_image_size.shape[1]+110]

frame[size_x[0]:size_x[1], size_y[0]:size_y[1]] = subimg

plt.imshow(frame, cmap="gray")
plt.show()

def transform(img_src, T):
    img_dst = np.zeros_like(img_src)
    for y in range(img_dst.shape[0]):
        for x in range(img_dst.shape[1]):
            new_coord = T @ np.array([y, x])
            new_y = int(new_coord[0])
            new_x = int(new_coord[1])
            if 0 < new_y < img_dst.shape[0] and 0 < new_x < img_dst.shape[1]:
                img_dst[y, x] = img_src[new_y, new_x]
    return img_dst
alpha = 30 # degrees
T = np.array([[np.cos(math.radians(alpha)), -np.sin(math.radians(alpha))],
              [np.sin(math.radians(alpha)), np.cos(math.radians(alpha))]])

frame_rotated = transform(frame, T)
plt.imshow(frame_rotated, cmap="gray")
plt.show()