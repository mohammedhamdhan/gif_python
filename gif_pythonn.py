import imageio.v3 as iio 
filenames = ['barbie-ryan-gosling(1).jpg','barbie-ryan-gosling(2).jpg','barbie-ryan-gosling(3).jpg','barbie-ryan-gosling(4).jpg','barbie-ryan-gosling(5).jpg','barbie-ryan-gosling(6).jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('python_gif.gif', images, duration = 500, loop = 0)