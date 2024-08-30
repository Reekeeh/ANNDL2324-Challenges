# ANNDL2324-Challenges
Repository for the challenges of the "*Artificial Neural Network and Deep Learning*" course competition, during A.Y. 2023/2024 at Politecnico di Milano.

The competition consisted in 2 separate challenges, hosted in two weeks periods each during the lessons:
* Homework 1: **Image Classification**
* Homework 2: **Time Series Forecasting**

Competition was hosted on CodaLab platform and the evaluations using hidden test sets were also divided in 2 phases: Development and Final.

Please refer to the Report in each section to read further information. Dataset for training is **not** publicly available 

# H1: ***Image Classification***
The goal of the first homework was correctly classify images (5200x96x96x3) of plants as *healthy* or *unhealthy*. Several CNN architectures have been explored in our efforts, leading finally to a 90% accuracy in Development Phase, 87.2% accuracy in Final Phase (28th place out of 211)

# H2: ***Time Series Forecasting***
In the second homework the task was predicting future samples from univariate (48000x2776) time series divided in categories based on the source the series was collected from. The model evaluation consisted in the prediction of 60 hidden time series for the next 9/18 future samples (Development/Final Phase). 

Obtained score results, with MSE and MAE as evaluation metrics:
* Development Phase: (0.0053; 0.051)
* Final Phase: (0.0093; 0.0699), 60th place out of 518

# Contributors
* **Riccardo Villa**
* **Mattia Pezzano** - pezzano.mattia@gmail.com
* **Luca Di Stefano** - lucads0298@gmail.com
* **Gabriele Romano** - romanogabriele48huawei@gmail.com


# Acknowledgments
* Professors and Teaching Assistants of the course
* Tensorflow and Keras documentation
* Google Colab platform

