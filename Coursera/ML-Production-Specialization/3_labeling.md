## Obtaining Data

Because ML is an iterative process and usually takes a long time, it's best to get into that iteration cycle as quickly as possible. You can always go back after performing error analysis and get more data after that.

![image](https://github.com/user-attachments/assets/2ddd75f1-4714-4253-9877-34109e43472c)

Once you decide the time constraints that you have, it may be worth to brainstorm where to get the data from. When thinking about this, it'll be useful to think of things like how much data you can get, the monetary cost, and how long it might take to get each data source. In the example below, we have 100 hours of audio already which is great because there's no monetary or time cost. If we want to further start up a crowdsourcing team outside the org, it may take 14 days and we'll want to pay $10000 to have these people do it.

<img width="812" alt="image" src="https://github.com/user-attachments/assets/43386a8a-faad-4644-bd52-3ec7d4aaf3a1" />

When trying to get data, it's also useful to consider who is going to label the data. If you choose in house, this may not be the best use of everyone's time. The difference between outsourcing and crowdsourcing is that outsourcing may be a specific company that is specialized for the certain type of data that you're looking to label whereas crowdsourcing may be using a platform where users can opt in to help label data. Crowdsouncing may be an option more for speech recognition where all you need is someone that if fluent in the language. Outsourcing may better if the data is more specialized like factory inspection or medical imaging.

![image](https://github.com/user-attachments/assets/c916e01a-19d3-4d5f-9010-a945cd3db7fb)

## Data Pipeline

Having a data pipeline is usually a good tool to have because then we can have a cleaning scipt as a pre processor for when we generate our test and training sets. But keep in mind that this means that this pipeline must now be in our production system.

![image](https://github.com/user-attachments/assets/960adf8e-7a47-479b-b9c1-4e43695bfc45)

Some data pipelines can become very complicated and transform the data multiple times. In the below example, Andrew paints a picture of a very complicated pipeline and then mmentions that months later, a bug is detected in the early spam detection step. It'll be nice to be able to identify the data that came from that spam model source so that we can redact it when it's at a later stage in the pipeline. However, the problem is that we have so many steps in the pipeline now that we aren't able to identify which data came from where. This is where the ideas of data provenance and data lineage come into play.

**Data Provenance** will tell us where the data originated from.

**Data Lineage** will tell us the sequence in steps that the data has traversed in the pipeline.

![image](https://github.com/user-attachments/assets/13c3b70b-c325-4b4d-8876-857631aafd4e)

Often it's useful if there's a framework for the data so that we can store the data provenance and lineage in metadata.
