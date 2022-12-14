import re
import numpy as np
import os
from flask import Flask,app,request,render_template
import sys
from flask import Flask,request,render_template,redirect,url_for
import argparse
from tensorflow import keras
from PIL import Image
from timeit import default_timer as timer
import test
import pandas as pd
import numpy as np
import random
def get_parent_dir(n=1):
  current_path = os.path.dirname(os.path.abspath(__file__))
  for k in range(n):
    current_path = os.path.dirname(current_path)
  return current_path
  src_path=r'c:\yolo_structure\2_Training\src'
print(src_path)
utils_path=r'c:\yolo_structure\Utils'
print(utils_path)
sys.path.append(src_path)
sys.path.append(utils_path)
import argparse
from keras_yolo3.yolo import YOLO,detect_video
import sys
from PIL import Image
from timeit import default_timer as timer
from utils import load_extractor_model, load_features, parse_input, detect_object
import test
import utils
import pandas as pd
import numpy as np
from Get_File_Paths import GetFileLists
import random
os.environ["TF_CPP_MIN_LOG_LEVEL"] ="3"
data_folder = os.path.join(get_parent_dir(n=1), "yolo_structure","Data")
image_folder =os.path.join(data_folder, "Source_Images")
image_test_folder = os.path.join(image_folder, "Test_Images")
detection_results_folder =os.path.join(image_folder, "Test_Images_Detection_results")
detection_results_file =os.path.join(detection_results_folder, "Detection_results.csv")
model_folder = os.path.join(data_folder,"Model weights")
model_weights = os.path.join(model_folder "trained_weights_final.h5")
model_classes = os.path.join(model_folder "data_classes.text")
anchors_paths  = os.path.join(src_path, "keras_yolo3","model_data",yolo_anchors.text)
FLAGS = None
app=Flask(__name__)
