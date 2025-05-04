An example of a deployment could be that a piece of inspection software takes a picture of a phone, sends the photo data to a prediction server via an api call, and finally have the prediction server return a prediction

![image](https://github.com/user-attachments/assets/30824337-2a31-429e-a2fa-d9368f666730)

The **POC to production gap** is when there is trouble going from the model working in a notebook to having it work in a production environment.

As we'll learn, ML code is typically a very small percentage of the actual code needed for the system.

![image](https://github.com/user-attachments/assets/24af1b98-d65a-4e1e-babe-a64b91a2831d)

The entire lifecycle of ML is usually defined by the following steps. This is not a set in stone framework but a framework tha andrew ng follows.

1. Scoping
  * This will include define the project and problem statement, as well as what you think that the x and y would be in this instance
2 Data
  * define the dataset needed
  * Label and organize the data that you can to get it ready for modeling
3. Modeling
  * Select the appropriate learning style and model to use
  * train the model
  * perform error analysis to evaluate the performance
4. Deployment
  * Deploy the model to production. Despite what you may think, deploying the model is only half of the deployment as the other half will be when you actually start accepting live traffic.
  * Monitor and maintain the system.

![image](https://github.com/user-attachments/assets/25f1d174-8a1f-4a48-8e31-7edf3ad2587f)

Let's take an example of speech recognition software.

Using the framework defined above, our first step is in the scoping step to define the project. Within defining the project and problem statement, we want to identify key metrics such as accuracy, latency and throughput. You'll also want to estimate the resources that you'll need and the timeline that you hope to have the project complete in.

![image](https://github.com/user-attachments/assets/84b88d6b-b7ca-4a32-aa7d-4cbf2bdaeda3)

The next step in the framework is Data. In this step, we want to ensure that our labels are consistent. As you'll see in the screenshot below, there are multiple ways to transcribe one audio clip. We want to make sure that we're consistent in our patterns so that if we label the data using one pattern one time, we're not using another pattern another time. Like in the example below, we don't want some labels to include the filler word um whereas some labels are removing the filler word. Either way to label the data is fine but we want to make sure that we're consistent. Other questions might be if you want a buffer in between each clip with silence to let the algorithm know that someone has stopped speaking. Still another question might be how to handle the case where some clips have very loud volume and some have very soft volume.

![image](https://github.com/user-attachments/assets/63e120c8-576e-4c52-942a-5a107f5e7bce)

The third step in the framework would be modeling. Here, we'll select the model that we want to use and train it on the dataset. In practical product teams, it's common to download and use an open source model from scikit-learn or tensorflow and they just to change the data and hyperparams to meet your needs. Error analysis will be used as an indicator for how things are performing.

![image](https://github.com/user-attachments/assets/d7e9961e-6faa-4f1b-a444-8ae9741c31a9)

In the deployment step, an implementation for a mobile phone might be that a microphone runs your voice through a VAD (Voice Activity Detection) module so that it can distill out the noise and then send thaat data to a prediction server running in the cloud. That server would then you send you back a transcript of what the algorithm thinks that you said as well as results you are looking for back to the phone where it can be display through frontend code.

Once deployed, the system may run into issues down the road where you begin receiving unexpected data. Andrew tells us a story where he has a speech recognition system that is trained largely on adult voices deployed. Because of this, when the system receives the voice of a younger user, the system starts to perform worse because it was not trained to handle this. This phenomenon is known as **Data Drift**.

![image](https://github.com/user-attachments/assets/9fe548a7-53d2-4c72-a7b5-a007e0f12f12)

## Deployment

