import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from deepface import DeepFace
import pickle
from tqdm import tqdm
import imageio

img1 = "ReconhecimentoFacial\Past_Leon\img1.jpg"
img2 = "ReconhecimentoFacial\Past_Leon\img2.jpg"
folder_path = "ReconhecimentoFacial\Past_Leon"
result = DeepFace.verify(img1,img2, enforce_detection=False)

print(result)