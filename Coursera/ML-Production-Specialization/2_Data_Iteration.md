## Data Centric Approach

**Data Augmentation** is about trying to improve the data quality for specific area that are more lacking behind on performance with the model. We still hold the model mixed and focus on improving the data through cleaning.

![image](https://github.com/user-attachments/assets/72194925-275a-468a-9a93-f621aa318180)

An example in data augmentation for speech recognition might be that you add two audio clips together and literally synthasize new data by adding their waveforms.

![image](https://github.com/user-attachments/assets/4ad5a317-579e-4212-a189-eb15879591fe)

When augmenting data, you want to keep a few things in mind.

* focus on data where the algorithm is performing poorly on.
* If a human were given the same data, would they be able to classify it correctly? The goal of many algorithms is just to meet human level performance so if the data can't even be recognized by a human, it's not really worth putting time into.
* if the data is not something that would come up in a real world scenario, then it's not worth putting time into

![image](https://github.com/user-attachments/assets/820bdadb-cc94-4864-bd92-760df8816ad5)

As an example of data that humans can't even perform well on, look at the following screenshot. When the image with the scratch is darkened a human wouldn't even be able to recognize a scrath. Therefor, it's not worth have the algorithm focus on that either. Andrew also mentions that he can use a tool as simple as photoshop to augment the data and generate these images. 

![image](https://github.com/user-attachments/assets/a4d406d3-17d1-4d4f-b8de-478a19816d4b)

With data augmentation, you also want to be careful about skewing the dataset in one direction. This may hurt performance of the model. Generally, you will rarely hurt performance given two criteria for unstructured data.

* The model is large. If you're using a very large neural network with a low bias, you are unlikely to hurt performance due to the size.
* The mapping from the input to the output isn't very complex and a human can make the predictions.

![image](https://github.com/user-attachments/assets/2cf25116-5faf-43fa-a2c2-c58a4ad0f619)

