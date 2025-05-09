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




