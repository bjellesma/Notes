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

