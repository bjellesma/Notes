This section focuses on the standardization of data to address the ambiguity present in data interpretation. Maintaining consistency in data definitions is crucial, and this can be achieved through human input to provide examples and ensure accurate labeling.

Andrew discusses the user ID merge problem, where data is sourced from both a website and a chatbot. A company may involve the product management team to manually identify whether the two data sources refer to the same person. This process aids in training the algorithm to make these determinations independently in the future.

![image](https://github.com/user-attachments/assets/76c2cfb5-79fa-4752-ac7d-16ca2baf5fc1)

The quality of input data is crucial for accurate defect detection. In the screenshot below, two photos of the same phone are shown; the second photo has significantly better lighting. This improved lighting allows the algorithm to detect defects more accurately.  Remember if a human can't even detect the defect, we can't expect an algorithm to.

![image](https://github.com/user-attachments/assets/4af772dc-3689-4616-b277-da0962679ab0)

## Data Problems

The tactic(s) that you employ may be different depending on if the data is unstructed (videos and images) or structured (database records and spreadsheets) and also if it is a small dataset vs a large dataset. When the data is structured, we can have humans go in and label the training data if it's small data or augment the data by creating new slightly different audio or images. But if the data is big, this becomes unwieldy and we'll have to rely on the data gathering process such as crowdsourcing from a voluntary group of labelers. If the data is structured, data augmentation by creating new datapoints becomes difficult. In the example below, we can't create data on a new house or user that doesn't exist.

![image](https://github.com/user-attachments/assets/de34b3d1-84dc-4ed7-8845-c34b840c6c33)

A problem arises when ask humans to label data that multiple inspectors may label something differently. For the exampple below, multiple inspectors have given different examples between whether they see a scratch depending on its length. The best tactic here is to try to get those labelers to agree on a certain length to determine a scratch. This will help with label consistency and help train the algorithm to be able to determine for itself whether a scratch is present.

![image](https://github.com/user-attachments/assets/7b8549e4-8a25-4d95-a58f-6f01651b40c9)

The final this to keep in mind that andrew goes over in the video is that big data problems will also contain these small data problems as well because a big dataset is really just a superset of a smaller dataset. So the same problems of labeling consistency comes into play. Larger datasets also have a big chance to have corner cases. For example, a self driving car company can have a lot of data of the car but there are still those corner cases like when a truck is blocking the highway.

![image](https://github.com/user-attachments/assets/62efdc1a-29af-4dea-9da0-0b05d0df8d0a)

## Improving label consistency

One example that we've seen previously for labeling data is to have labelers agree to standardize such as using 1 m when they hear um in the audio clip. Another example would be to **merge classes** whereas you can call multiple types of data the same thing. An example of merging classes might be that you can label a deep scratch and a shallow scratch both a scratch provided it's not important to distinguish between these two.

![image](https://github.com/user-attachments/assets/45fc0cf9-72a2-4eeb-98eb-0b520cf8ed32)

We've also mentioned that it's best to get labelers to agree on how long a scratch on a phone should be to be considered a defect vs not a defect. This may be difficult to get everyone to agree so one tactic could be to introduce a new classification to hold all of the borderline cases. However, this may still present the problem of having everyone agree on what to put into the borderline classification.

Introducing a new classification works well in speech recognition because multiple labelers could have different interpretations of an audio clip that's hard to understand. A cool tactic may be use to introduce the classification of "Unintelligable" for parts of the clip that are difficult to understand. Again, this presents an issue of having everyone agree on what's unintelligible but this is a lot easier to enforce on speech recognition.

![image](https://github.com/user-attachments/assets/5ef4a9e5-2b29-4fa1-ad5d-432c1cdd16a5)

Lastly, your tactic for labeling consistency may be different for small vs large datasets. With small datasets, it's easier to just ask the labelers to agree on consistency (if the dataset is small enough, we may just do this in house). With a larger dataset where you may use crowdsourcing to label the data, it's most useful to just have a set of consistent labeling instructions. You can also use **consensus voting** for large datasets where multiple voters will just vote on the correct label but this can relinquish control more to the voters.

![image](https://github.com/user-attachments/assets/5a2e3e15-4710-4097-a9c2-e79ad1774369)
