import numpy as np
import matplotlib.pyplot as plt

def get_chroma_matrix(sr, win):
    """
    Compute a chroma matrix
    
    Parameters
    ----------
    sr: int
        Sample rate
    win: int
        STFT Window length
    
    Returns
    -------
    ndarray(12, floor(win/2)+1)
        A matrix, where each row has a bunch of Gaussian blobs
        around the center frequency of the corresponding note over
        all of its octaves
    """
    K = int(win/2)+1 # Number of non-redundant frequency bins
    M = np.zeros((12, K)) # Create the matrix
    freqs = sr*np.arange(K)/win # Compute the frequencies at each spectrogram bin
    ## TODO: Fill this in
    return M