## Error Analysis

Like other processes in ML, error analysis is iterative where you want to analyze where the algo made error and tab how the error occured so that you can build up metrics of what causes the most errors in your ML algo as you see in the second screenshot.

![image](https://github.com/user-attachments/assets/e477b93a-6d45-415f-a804-fca94e8ab35b)

![image](https://github.com/user-attachments/assets/6e97e78f-145c-4b74-9009-648252b79db3)

Taking things a step further, if you can accurately tag not only your misclassified data but also your correctly classified data you can use that data along with your assessment from before on the performance difference with human level performance to figure out what's best to work on. In the following screenshot, we've previously compared our learning algorithm with how it is performing compared with human level performance. The result was that the algorithm has the most difference on car noise with human level performance. We now revisit that because if we have tags to say that only 4% of data has car noise we may be able to assess that that's not as worth working on as previously thought. We also see that the accuracy of the algo compared with human level performance is only 1% on clean speech but when you consider that 60% of our data will be clean speech, this means that it will be worth working on that 1% improvement for clean speech. We can figure this mathematically by multiplying that 1% with the 60% of data to get .6% overall improvement which is larger than the .16% overall improvement we could get from working on the car noise.

![image](https://github.com/user-attachments/assets/c6082e63-7cc5-4c45-b674-16f415e35ab6)

Even though tagging will help us what work on, there are two other important considerations such as how easy it is to improve (we may have no other ideas on how to improve clean speech accuracy because we've already exhausted several techniques) and how important is it (car noise might be substantially more important to improve so that people aren't using their hands while driving).

![image](https://github.com/user-attachments/assets/0b2e60b3-ee09-499c-8ee0-9e57d0688e3d)

Once you decide the category to work on, you may want to start to collect more data if possible

![image](https://github.com/user-attachments/assets/2a2fa401-b7c0-4326-9b0d-ead362d51443)
