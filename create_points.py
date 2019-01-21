import numpy as np
from matplotlib import pyplot as plt


def random_point(x_pos=100, y_pos=100, radius=40, inner_r=10):
    """
    Create a random point in a circle of radius 'radius' centered in (x_pos, y_pos)
    :param x_pos: position x of the center of the circle
    :param y_pos: position y of the center of the circle
    :param radius: radius of the circle
    :param inner_r: inner radius in which no points have to be made
    :return: position of a random point
    """
    # random angle
    alpha = 2 * np.pi * np.random.rand()
    # random radius
    r = radius * np.sqrt(np.abs(np.random.rand())) + inner_r
    # calculating coordinates
    x = r * np.cos(alpha) + x_pos
    y = r * np.sin(alpha) + y_pos
    return x, y
    # print("Random point", (x, y))


def create_base_image(n_points=0, x_pos=100, y_pos=100, radius=40, inner_r=10):
    """
    Create an image with a random distribution of n points
    :param n_points: number of points in image
    :param x_pos:
    :param y_pos:
    :param radius:
    :param inner_r:
    :return: dict with x and y arrays
    """
    x = np.zeros(n_points)
    y = np.zeros(n_points)
    for idx, point in enumerate(range(n_points)):
        x[idx], y[idx] = random_point(x_pos, y_pos, radius, inner_r)
    return np.concatenate((np.reshape(x, (1, n_points)), np.reshape(y, (1, n_points))))


def scatter_image_v(image_array, scatter=5):
    """
    Create a vertically 'moved' image scattering original points and merging them on the original
    :param image_array: 2-dim array with original image
    :param scatter: length of scatter
    :return: original image with scatter. The total amount of points has doubled
    """
    n_points = len(image_array[0])*2
    x = image_array[0]
    y = image_array[1]
    x = np.concatenate((x, x))
    y_moved = y + scatter
    y = np.concatenate((y, y_moved))
    return np.array((np.reshape(x, (1, n_points)), np.reshape(y, (1, n_points))))


def randomize_image(image_array):
    """
    Create a randomize version of the same image with doubled points
    :param image_array: 2-dim array
    :return: randomized version of the same image with doubled points
    """
    n_points = len(image_array[0])
    another_image = create_base_image(n_points)
    x = np.concatenate((image_array[0], another_image[0]))
    y = np.concatenate((image_array[1], another_image[1]))
    return np.concatenate((np.reshape(x, (1, n_points*2)), np.reshape(y, (1, n_points*2))))


def plot_points(image_array):
    plt.plot(image_array[0], image_array[1])


if __name__ == '__main__':
    image_array = create_base_image(1000)
    random_img = randomize_image(image_array)
    scattered_img = scatter_image_v(image_array, scatter=3)
    plt.plot(scattered_img[0], scattered_img[1], '.', c='black')
    # plt.plot(random_img[0], random_img[1], '.', c='red')
    plt.show()
