# This code was run locally to inspect the dataset and find the outliers
import numpy as np
import matplotlib.pyplot as plt

# loading the images
images = np.load('public_data.npz', allow_pickle=True) ['data']

#Number of images to display at a time
num_images = 50

# Dimensions for subplot layout
rows = 5
cols = 10

# Iterate over images
for i in range(0, len(images), num_images):
    # Create a new figure for every `num_images` images
    fig = plt.figure(figsize=(20, 10))

    # Get the subset of images to display
    subset_images = images[i:i+num_images]

    # Iterate over the subset of images
    for j in range(len(subset_images)):
        # Add a subplot for each image
        ax = fig.add_subplot(rows, cols, j+1)

        # Display the image
        ax.imshow(subset_images[j] / 255.0)  # Normalize color scale

        # Add the image index as the title
        ax.set_title(str(i + j))

        # Remove the axis
        ax.axis('off')

    # Display the figure with `num_images` images
    plt.show()

# artifat images indexes (taken by hand upon visual inspection):
artifact_indexes = np.array([
    58, 95, 137, 138, 171, 207, 338, 412, 434, 486, 506, 529, 571, 599, 622, 658, 692, 701, 723, 725,
    753, 779, 783, 827, 840, 880, 898, 901, 961, 971, 974, 989, 1028, 1044, 1064, 1065, 1101, 1149, 1172,
    1190, 1191, 1265, 1268, 1280, 1333, 1384, 1443, 1466, 1483, 1528, 1541, 1554, 1594, 1609, 1630, 1651,
    1690, 1697, 1752, 1757, 1759, 1806, 1828, 1866, 1903, 1938, 1939, 1977, 1981, 1988, 2022, 2081, 2090,
    2150, 2191, 2192, 2198, 2261, 2311, 2328, 2348, 2380, 2426, 2435, 2451, 2453, 2487, 2496, 2515, 2564,
    2581, 2593, 2596, 2663, 2665, 2675, 2676, 2727, 2734, 2736, 2755, 2779, 2796, 2800, 2830, 2831, 2839,
    2864, 2866, 2889, 2913, 2929, 2937, 3033, 3049, 3055, 3086, 3105, 3108, 3144, 3155, 3286, 3376, 3410,
    3436, 3451, 3488, 3490, 3572, 3583, 3666, 3688, 3700, 3740, 3770, 3800, 3801, 3802, 3806, 3811, 3821,
    3835, 3862, 3885, 3896, 3899, 3904, 3927, 3931, 3946, 3950, 3964, 3988, 3989, 4049, 4055, 4097, 4100,
    4118, 4144, 4150, 4282, 4310, 4314, 4316, 4368, 4411, 4475, 4476, 4503, 4507, 4557, 4605, 4618, 4694,
    4719, 4735, 4740, 4766, 4779, 4837, 4848, 4857, 4860, 4883, 4897, 4903, 4907, 4927, 5048, 5080, 5082,
    5121, 5143, 5165, 5171
])

# second check to make sure all artifacts were detected, hihgligting them with red text and a red cross

# Iterate over images
for i in range(0, len(images), num_images):
    # Create a new figure for every `num_images` images
    fig = plt.figure(figsize=(20, 10))

    # Get the subset of images to display
    subset_images = images[i:i+num_images]

    # Iterate over the subset of images
    for j in range(len(subset_images)):
        # Add a subplot for each image
        ax = fig.add_subplot(rows, cols, j+1)

        # Display the image
        ax.imshow(subset_images[j] / 255.0)  # Normalize color scale

        # Check if the image index is in `artifact_indexes`
        if i + j in artifact_indexes:
            # Color the index red and add an 'X' on top of the image
            ax.set_title(str(i + j), color='red')
            ax.text(0.5, 0.5, 'X', color='red', fontsize=30, ha='center', va='center', transform=ax.transAxes)
        else:
            ax.set_title(str(i + j))

        # Remove the axis
        ax.axis('off')

    # Display the figure with `num_images` images
    plt.show()

"""
Now outliers are easily removable this way:

artifact_indexes = np.sort(artifact_indexes)[::-1] # Sort the artifact indexes in descending order
for index in artifact_indexes:
    X = np.delete(X, index, axis=0)
    y = np.delete(y, index, axis=0)

Upon visual inspection it seemed that some images had duplicates among the dataset.
Excess duplicates were deleted using Anti-Twin software . The new dataset was then saved (dataset_wo_duplicates.npz)
and subsequently used for all experiments.

"""