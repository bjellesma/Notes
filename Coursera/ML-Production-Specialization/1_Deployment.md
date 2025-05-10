* data drift is when the data changes after a model is deployed, this can be gradual like new words being added to the dictionary or sudden like covid-19 causing many people to start shopping online throwing off fraud detection systems. In data drift, x is changing
* concept drift is where both x and y change like if a bigger house no longer correlates to a more expensive house

<img width="970" alt="image" src="https://github.com/user-attachments/assets/4e539207-d9a4-4c85-9df2-8229c0aa837d" />

During deployment, there are also software engineering issues to consider

### Realtime or Batch
- **Realtime example:** A fraud detection system that analyzes credit card transactions as they occur, immediately flagging suspicious activity
- **Batch example:** A recommendation system that updates user preferences and suggestions overnight by processing the day's collected data

### Cloud vs. Edge/Browser
- **Cloud example:** Running complex machine learning models on AWS servers where massive computation power is available
- **Edge/Browser example:** Using TensorFlow.js to run a lightweight object detection model directly in a user's mobile phone camera app. This may be useful in circumstances where you don't always have internet

### Compute resources (CPU/GPU/memory)
- **CPU example:** Running a natural language processing service that handles text parsing and sentiment analysis
- **GPU example:** Training a deep learning model for image recognition requiring parallel processing
- **Memory example:** A database service that keeps frequently accessed customer data in RAM for faster retrieval

### Latency, throughput (QPS - Queries Per Second)
- **Latency example:** A stock trading platform that needs to execute trades in under 100ms
- **Throughput example:** A social media API that must handle 1000 QPS during peak usage times

### Logging
- **Example:** An e-commerce platform that logs all purchase attempts, both successful and failed, with timestamps and user IDs for troubleshooting and analysis

### Security and privacy
- **Example:** A healthcare application that encrypts patient data both in transit and at rest, with role-based access controls and comprehensive audit trails

<img width="984" alt="image" src="https://github.com/user-attachments/assets/67e0c823-a751-456c-a307-20df5cb89541" />


## Common deployment cases

* The most obvious is if we want to implement the product or a capability.
* automation - if we want to create something to assist with a manual task in the factory. an example would be to use anomaly detection for visual inspection
* if we want to replace a previous system

When deploying, one common technique is to use a **shadow mode** deployment when the ML system works alongside the human. During this stage, we'll still go with human judgement 

The next stage of deployment might be **canary deployment** where we only deployment to a small fraction of the traffic. This is helpful because if the ML algorithm makes a mistake, it only makes a mistake to a handful of the user base. Often we have the users opt into trying this

![image](https://github.com/user-attachments/assets/7cf9e081-1267-488e-afcc-2df9cd0db5bb)

Another common deployment pattern is a **blue green deployment** where we can switch over traffic when we're ready, either all at once or gradually, which makes it a lot easier to rollback

![image](https://github.com/user-attachments/assets/5e81b836-9e1e-41a9-b189-3c0a6151159b)

As you'd imagine with ML, there are different degrees of automation that you may want. A lot of factory work falls into **human in the loop** where the ML algo may be assisting the human but we still want the final decision to come from a human.

![image](https://github.com/user-attachments/assets/83e02bcf-d484-4a7b-b7d3-b4376c446e22)

## Monitoring

Commonly, we should think of things that can go wrong and then build a dashboard to track that 

![image](https://github.com/user-attachments/assets/3c3794f2-2656-4815-8fc4-5bb373f3d22d)

When consider metrics to track in a brainstorm, we might divide them into three catagories: software (server load, latency, etc), input metrics (how much data comes through as missing or in the case of speech recognition the average volume), and output (the times that a user has to redo a search may indicate frustration). In these three categories, software metrics are usually general and apply to a broad range of algorithms where input and output can be very specific.

![image](https://github.com/user-attachments/assets/610ca1a4-1ae0-4fc8-a899-43849c0026a3)

## Pipeline Monitoring

In Addition to monitoring metrics, it's also good to monitor the entire pipeline where you can. For example, speech recognition data will come from a cell phone's VAD (voice activity detection) so if a company decides to change how their VAD functions which may  mean that the audio is clipped differently, this may lead to data drift and degradation in performance for the speech recognition software.

![image](https://github.com/user-attachments/assets/58b443dc-a5b1-4629-b53c-19378deb7fee)

## Lab: deploying image detection

In the following lab, we deploy image detection software using [cvlib](https://github.com/arunponnusamy/cvlib) which uses [YOLOv3](https://en.wikipedia.org/wiki/You_Only_Look_Once) as the model and fastapi.

Let's first create a function that will tak

```py
import cv2

# suppress Tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cvlib as cv
from cvlib.object_detection import draw_bbox


def detect_and_draw_box(filename, model="yolov3-tiny", confidence=0.5):
    """Detects common objects on an image and creates a new image with bounding boxes.

    Args:
        filename (str): Filename of the image.
        model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
        confidence (float, optional): Desired confidence level. Defaults to 0.5.
    """
    
    # Images are stored under the images/ directory
    img_filepath = f'images/{filename}'
    
    # Read the image into a numpy array
    img = cv2.imread(img_filepath)
    
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
    
    # Print current image's filename
    print(f"========================\nImage processed: {filename}\n")
    
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}\n")
    
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)
    
    # Save the image in the directory images_with_boxes
    cv2.imwrite(f'images_with_boxes/{filename}', output_image)
    
    # Display the image with bounding boxes
    display(Image(f'images_with_boxes/{filename}'))
```

Try out feeding an image into it

```py
detect_and_draw_box("fruits.jpg")
```

Now let's setup a webserver using fastapi and uvicorn to serve the content

```py
import io
import uvicorn
import numpy as np
import nest_asyncio
from enum import Enum
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

# Assign an instance of the FastAPI class to the variable "app".
# You will interact with your api using this instance.
app = FastAPI(title='Deploying an ML Model with FastAPI')

# List available models using Enum for convenience. This is useful when the options are pre-defined.
class Model(str, Enum):
    yolov3tiny = "yolov3-tiny"
    yolov3 = "yolov3"


# By using @app.get("/") you are allowing the GET method to work for the / endpoint.
@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://serve/docs"


# This endpoint handles all the logic necessary for the object detection to work.
# It requires the desired model and the image in which to perform object detection.
@app.post("/predict") 
def prediction(model: Model, file: UploadFile = File(...)):

    # 1. VALIDATE INPUT FILE
    filename = file.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")
    
    # 2. TRANSFORM RAW IMAGE INTO CV2 image
    
    # Read image as a stream of bytes
    image_stream = io.BytesIO(file.file.read())
    
    # Start the stream from the beginning (position zero)
    image_stream.seek(0)
    
    # Write the stream of bytes into a numpy array
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    
    # Decode the numpy array as an image
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    
    # 3. RUN OBJECT DETECTION MODEL
    
    # Run object detection
    bbox, label, conf = cv.detect_common_objects(image, model=model)
    
    # Create image that includes bounding boxes and labels
    output_image = draw_bbox(image, bbox, label, conf)
    
    # Save it in a folder within the server
    cv2.imwrite(f'images_uploaded/{filename}', output_image)
    
    
    # 4. STREAM THE RESPONSE BACK TO THE CLIENT
    
    # Open the saved image for reading in binary mode
    file_image = open(f'images_uploaded/{filename}', mode="rb")
    
    # Return the image as a stream specifying media type
    return StreamingResponse(file_image, media_type="image/jpeg")
```

Now run the server

```py
# Allows the server to be run in this interactive environment
nest_asyncio.apply()

# This is an alias for localhost which means this particular machine
host = "127.0.0.1"

# Spin up the server!    
uvicorn.run(app, host=host, port=8000, root_path="/serve")
```

Running the server will bring up swagger docs with a predict endpoint that you can play with

![image](https://github.com/user-attachments/assets/bb90d603-225e-4d19-b4de-8dfd0cdc571b)

## Running with docker

Optionally, you can package this fastapi in a docker container.

Here is the dockerfile that you'll use

```docker
# base image
FROM python:3.11

# specify working directory
WORKDIR /code

# copy package list
COPY ./requirements.txt /code/requirements.txt

# install packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy application code
COPY ./app /code/app

# copy pretrained models
COPY .cvlib /root/.cvlib

# expose port
EXPOSE 80

# run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

You can download all of the necessary file from [here](https://storage.googleapis.com/mlep-public/course_1/week1/mlepc1w1_cloud.zip)

## Running in AWS

Once you have a docker container setup, you can choose to deploy the container using AWS. You'll use elastic beanstalk to run the container and then a t3 large instance on ec2 to give yourself compute
