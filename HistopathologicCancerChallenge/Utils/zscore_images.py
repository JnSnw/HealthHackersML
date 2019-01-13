import numpy as np

def zscore_images(X):
    """Converts images to 0 mean, unit variance. Expects NHWC
    Args:
        X (np array): images
    
    Returns:
        np array: z scored images
    """
    for i,image in enumerate(X):
        for channel in range(image.shape[2]):
            image[:,:,channel] = image[:,:,channel] - np.mean(image[:,:,channel])
            image[:,:,channel] = image[:,:,channel] / np.std(image[:,:,channel])  
        X[i] = image

    return X