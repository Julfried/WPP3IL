import numpy as np
import matplotlib.pyplot as plt

frame = r"C:\Users\Julian\OneDrive - FH OOe\Kurse\3. Semester\WPP3IL\images\frame_gray.png"
stinkbug = r"C:\Users\Julian\OneDrive - FH OOe\Kurse\3. Semester\WPP3IL\images\stinkbug_gray.png"


size_x, size_y = (78, 435), (80, 351)
stinkbug = plt.imread(stinkbug)
frame = plt.imread(frame)
frame_image_size = np.zeros_like(frame[size_x[0]:size_x[1], size_y[0]:size_y[1]])

subimg = stinkbug[0:frame_image_size.shape[0], 110:frame_image_size.shape[1]+110]

frame[size_x[0]:size_x[1], size_y[0]:size_y[1]] = subimg

plt.imshow(frame, cmap="gray")
plt.show()