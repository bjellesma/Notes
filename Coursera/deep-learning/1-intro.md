# Intro to Deep Learning

Here is a recap of neural networks. We have a list of features x that go into a second layer that determines family size, walkability, and school quality, and finally gives an output layer y
<img width="2880" height="1564" alt="image" src="https://github.com/user-attachments/assets/37220b26-e0a3-43eb-9a2a-bff3cdf2de63" />

In this example, the layers are densely connected because each of the four input features is connected to every node in the second layer (referred to as the **hidden layer**) 
<img width="1456" height="669" alt="image" src="https://github.com/user-attachments/assets/11c9c291-6c75-479d-93e6-e0a32a827b87" />

Various applications exist for neural networks. Real estate and online ads might use a standard neuraal network. Photo Tagging might use a **convolutional neural network** where it uses filters (small matrices) to learn to detect specific features like edges and corners. Speech recognition might use a **recurrent neural network** where it processes sequential data by maintaining an internal memory that gets updated as it processes each element in a sequence.
<img width="2165" height="951" alt="image" src="https://github.com/user-attachments/assets/617e2079-b37c-4169-b9fe-ce15ef7c2bc3" />

Historically computers have been very good at dealing with **structured data** where it's in columns and rows. Deep Learning is enabling computers to be better with **unstructured data** such as audio clips and images.
<img width="3744" height="1963" alt="image" src="https://github.com/user-attachments/assets/14db08c9-9b25-4918-987f-95423b2984bb" />

The big drivers of the advances in deep learning were data, computation, and algorithms. Data was big because we spend some much of our time online these days. With algorithms specifically, a lot of performance gain game from switching from sigmoid to relu function. This is because at certain points on the sigmoid, the gradiant will be zero whereas in relu, the gradiant is guarenteed to be greater than 1 with positive values. Faster computation also means that practicioners can move a lot faster from idea to experimentation.
<img width="1385" height="1555" alt="image" src="https://github.com/user-attachments/assets/a59b9a7b-afe7-4593-884a-1c2b4785966c" />
