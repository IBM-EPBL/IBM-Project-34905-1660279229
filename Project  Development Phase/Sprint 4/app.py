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
src_path=r'C:\yolo_structure\2_Training\src'
print(src_path)
utils_path=r'C:\yolo_structure\Utils'
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

from cloudant.client import Cloudant 
client = Cloudant.iam('username', 'apikey', connect=True)
my_database=client.create_database('my_database')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/aftrreg',methods=['POST'])
def afterreg():
    X=[X for X in request.form.values()]
    print(X)
    data={
        '_id':X[1]
        'name':X[0]
        'psw':X[2]
    }
    print(data)
    query={'_id':{'$eq':data['_id']}}
    docs=my_database.get_query_result(query)
    print(docs)
    print(len(docs.all()))
    if(len(docs.all())==0):
        url=my_database.create_document(data)
        return render_template('register.html', pred="Registration Successful, please login using your details")
    else:
        return render_template('register.html', pred="You are already a member, please login using your details")
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/afterlogin',method=['POST'])
def afterlogin():
    user=request.form['_id']
    passw=request.form['psw']
    print(user,passw)

    query={'_id':{'$eq':user}}

    docs=my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if(len(docs.all())==0):
        return render_template('login.html',pred="The username is not found.")
    else:
        if((user==docs[0][0]['_id'] and passw==docs[0][0]['psw'] )):
            return redirect(url_for('prediction'))
        else:
            print('Invalid user')
@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/result',methods=["GET","POST"])
def res():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPRESS)
    parser.add_argument(
        "--input_path",
        type=str,
        default=image_test_folder,
        help="C:\yolo_structure\Data\Source_Images\Test_Images"+image_test_folder,
    )
parser.add_argument(
    "--output",type=str,
    default=detection_results_folder,help="C:\yolo_structure\Data\Source_Images\Test_Image_Detection_Results"+detection_results_folder,
)
parser.add_argument(
    "--no_save_img",
    default=False, action="store_true",
    help="only save bounding box coordinates but not save output images with annotated boxes. Default is false.",
)
parser.add_argument(
    "--file_types",
    "--names-list",
    narges="*",
    default=[],
    help="Specify list of file types to include. Default is --file_types .jpg .jpeg",
)
parser.add_argument(
    "--anchors",
    type=str,
    dest="anchors_path",
    default=anchors_path,
    help="Path to YOLO anchors. Default is "+anchors_path,
)
parser.add_argument(
    "--classes_path",
    type=str,
    dest="classes_path",
    default=model_classes,
    help="Path to YOLO class specifications. Default is "+ model_classes,
)
parser.add argument(
    "--confidence",
    type=float,
    dest-"score",
    default-0.25,
    help="Threshold for YOLO object confidence score to show predictions. Default is 0.25.",
)
parser.add argument(
    "--box file",
    type-str,
    dest="box",
    default=detection_results_file,
    help="File to save bounding box results to. Default is" + detection_results_file,
)
parser.add argument(
    "--postfix",
    type=str,
    dest="postfix",
    default="disease",
    help="Specify the postifix for images with boundings boxes.Default is "_disease"',
)
FLAGS =parser.parse_args()
save_img =not FLAGS.no_save_img
file_types= FLAGS.file_types
if file types:
    input =GetFilelist(FLAGS.input_path,endings=file_types)
    print(input_paths)
else:
    input_paths = GetFilelist(FLAGS.input_path)
    print(input_paths)
img_endings = (".jpg", ".jpeg",".png")
vid_endings = (."mp4", ".mpeg",".mpg",".avi")
input_image_paths =[]
input_video_paths =[]
for item in input_paths:
  if item.endswith(img_endings):
    input_image_paths.append(item)
  elif item.endswith(vid_endings):
    input_video_paths.append(item)
output_path = FLAGS.output
if not os.path.exists(output_path):
  os.makedirs(output_path)
yolo =YOLO(
    **{"model_path": FLAGS.model_path,
       "anchors_path":FLAGS.anchors_path,
       "classes_path": FLAGS.classes_path,
       "score": FLAGS.score,
       "gpu_num":FLAGS.gpu_num,
       "model_image_size":(416,416),
       }
)
out_df = pd.DataFrame(
    columns=[
        "image",
        "image_paths",
        "xmin",
        "xmax",
        "ymax",
        "label",
        "confidence",
        "x_size",
        "y_size",
    ]
)

class file = open (FLAGS.classes_path, "r")

input_labels = [line.rstrip("\n") for line in class_file.readlines()]
print("Found {} input labels:{}...".format(len(input_labels), input_labels))
if input_image_paths:
    print(
        "found {} input images: {} ...".format(
            len(input_image_paths),
            [os.path.basename(f) for f in input_image_paths[:5]],
        )
    )
  start = timer()
  text_out = ""
for i,img_path in enumerate(input_image_paths):
    print(img_path)
    prediction, image, lat, lon = detect_object(
        yolo,
        img_path,
        save_img=save_img,
        save_img_path=FLAGS.output,
        postfix=FLAGS.postfix,
    )
print(lat,lon)
y_size, x_size, _ = np.array(image).shape
for single_prediction in prediction:
    out_df = out_df.append(
        pd.DataFrame(
            [
                [
                    os.path.basename(img_path.rstrip("\n")),
                    img_path.rstrip("\n"),
                ]
                + single_prediction
                + [x_size, y_size]
             ],
    coloumns=[
        "image",
        "image_paths",
        "xmin",
        "xmax",
        "ymax",
        "label",
        "confidence",
        "x_size",
        "y_size",
    ],
 )
)
    end = timer()
    print("Processed {} images in {:.1f}sec-{:.1f}FPS".format(
        len(input_image_paths),
        end - start,
        len(input_image_paths) \(end - start),
    )
)
out_df.to_csv(FLAGS.box, index=False)
if input_video_paths):
    print(
    "found {} input videos: {} ...".format(
        len(input_video_paths),
            [os.path.basename(f) for f in input_video_paths[:5]],
    )
)
start = timer()
for i, vid_path in enumerate(input_video_paths):
    output_paths = os.path.join(
         FLAGS.output,
         os.path.basename(vid_path).replace(".", FLAGS.postfix + "."),
    )
    detect_video(yolo, vid_path, output_path=output_path)
end = timer()
print(
     "processed {} viideos in {:.1f}sec".format(
         len(input_video_paths), end - start
     )
)
yolo.close_session()
return render template('predictions.html')

if __name__=="__maina__":
  app.run(debug=False)



