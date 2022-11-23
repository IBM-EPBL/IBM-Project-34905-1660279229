# IBM-Project-34905-1660279229
# AI-based localization and classification of skin disease with erythema


<p align="center">
<a href="https://www.ibm.com/in-en">
<img src="https://img.shields.io/badge/IBM-052FAD.svg?style=for-the-badge&logo=IBM&logoColor=white"> 
</a>
  <a href="https://www.python.org/">
   <img src="https://forthebadge.com/images/badges/made-with-python.svg" width =190>
  </a>
  <a href="https://www.ibm.com/cloud">
      <img src="https://img.shields.io/badge/IBM%20Cloudant-BE95FF.svg?style=for-the-badge&logo=IBM-Cloudant&logoColor=white" width=130>
  </a>
   <a href="https://www.kaggle.com/code/ankitp013/step-by-step-yolov3-object-detection">
    <img src="https://img.shields.io/badge/YOLOV3-5C3EE8.svg?style=for-the-badge&logo=YOLOV3&logoColor=white">
   </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
    </a>
  <a href="https://keras.io/">
    <img src="https://img.shields.io/badge/Keras-D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
    </a>
   <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/Numpy-D00000.svg?style=for-the-badge&logo=Numpy&logoColor=white">
    </a>
  </p>
  <img src="https://media.giphy.com/media/UX5ovY9QQ1FOpaKtc8/giphy.gif" width="30px"><a href="https://youtu.be/5z5av9i6gZ4">Demo Video Project</a>
  
  ## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Team:
    1. Bhavitha R [TL] - 312819104016
    
    2. Dhanalakshmi G [TM1] -312819104021
    
    3. Bhuvaneshwaran A [TM2] - 312819104017
    
    4. Aswin P [TM3] - 312819104014
 ## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Introduction :
 Now a day’s people are suffering from skin diseases, More than 125 million people suffering from Psoriasis also skin cancer rate is rapidly increasing over the last few decades especially Melanoma is most diversifying skin cancer. If skin diseases are not treated at an earlier stage, then it may lead to complications in the body including spreading of the infection from one individual to the other. The skin diseases can be prevented by investigating the infected region at an early stage. The characteristic of the skin images is diversified so that it is a challenging job to devise an efficient and robust algorithm for automatic detection of skin disease and its severity. Skin tone and skin colour play an important role in skin disease detection. Colour and coarseness of skin are visually different. Automatic processing of such images for skin analysis requires quantitative discriminator to differentiate the diseases.

 To overcome the above problem we are building a model which is used for the prevention and early detection of skin cancer, psoriasis. Basically, skin disease diagnosis depends on the different characteristics like colour, shape, texture etc. Here the person can capture the images of skin and then the image will be sent the trained model. The model analyses the image and detect whether the person is having skin disease or not.
 
 ![image](https://i.ibb.co/2gsT69v/Screenshot-20221118-205150.png)
 
      
## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Built with tools
![image](https://d1vwxdpzbgdqj.cloudfront.net/assets/aiml-pp-new/language-logos-mob-86e412da059ad22dc2176eb7b853c4555aaf85b0c495ce2a7bd11baa582f6f90.jpg)

## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Project Objectives: 
        1. Creating the data set from scratch by downloading ERYTHEMA skin disease images

        2. To make our detector learn, we first need to feed it some good training examples.
           We use Microsoft's Visual Object Tagging Tool (VoTT) to manually label images

        3. we will train our model using YOLO weights.

        4. Create HTML page and pretrained data, algorithm are connected to IBM cloudant Database.

        5. You will be able to build web applications using the Flask framework and predict output.  
 ## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Prerequisites :
## Anaconda Navigator :
- Anaconda Navigator is a free and open-source distribution of the Python and R programming languages for data science and machine learning-related applications. It can be installed on Windows, Linux, and macOS. Conda is an open-source, cross-platform,  package management system. Anaconda comes with so very nice tools like JupyterLab, Jupyter Notebook,QtConsole, Spyder, Glueviz, Orange, Rstudio, Visual Studio Code. For this project, we will be using Jupiter notebook and spyder.

 ### To build Deep learning models you must require the following packages :
 - Tensor flow: TensorFlow is an end-to-end open-source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers can easily build and deploy ML powered applications.
 - Keras : Keras leverages various optimization techniques to make high level neural network API easier and more performant. It supports the following features.
 
       1. Consistent, simple and extensible API.
       
       2. Minimal structure - easy to achieve the result without any frills.
       
       3. It supports multiple platforms and backends.
       
       4. It is user-friendly framework that runs on both CPU and GPU.
       
       5. Highly scalability of computation.
 - Flask: Web framework used for building  Web applications

## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Technical Architecture : 
 ![image](https://i.ibb.co/pzKcwYv/image2.png)
 ## <img src="https://media.giphy.com/media/nDmTGama5e9ZH6mlT3/giphy.gif" width="30px"> Project Structure :
 ![image](https://i.ibb.co/6sszcZG/download.png)
 - The dataset folder contains two folders contains a test and train folder, each of them have images of different fruits.
- The Flask folder has all the files necessary to build the flask application. 

     -  Templates folder has the HTML pages.
  
     -  Uploads folder has the uploads made by the user.
  
     -  app.py is the python script for server-side computing.
  
     - .h5 files are the model files that are to be saved after model building.
  
 

  
 IBM Nalaiya Thiran | Agni College Of Technology
  

