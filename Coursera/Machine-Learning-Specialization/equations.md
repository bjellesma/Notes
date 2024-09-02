**Univariate Linear Regression** - $\hat{y}^{(i)} = wx^{(i)} + b$

**Squared Error Cost Function** -  $J(w,b) = \frac{\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^{2}}{2m}$ where m is the number of training examples, $\hat{y}^(i)$ or $f_{w,b}(x^{(i)}$ is the value of the line that we're proposing, and $y^{(i)}$ is the actual value. Remember that $f_{w,b}(x^{(i)} = wx^{(i)} + b$ from univariate linear regression above.

**Gradient Descent** - $w = w - \alpha (\frac{\partial}{\partial w}J(w,b))$ and $b = b - \alpha (\frac{\partial}{\partial b}J(w,b))$

**Gradient Descent (without derivatives)**

## $w = w - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})(x^{(i)})$

## $b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})$

**Multiple Linear Regression** - $f_{w,b}(x) = w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{3}+...+w_{n}x_{n}+b$ where n is the number of features

**Multiple Linear Regression** (vector notation) 

## $f_{\vec{w},x}(\vec{x})=\vec{w} \cdot \vec{x} + b$

**Gradient Descent for Multiple Linear Regression**

## $w_n = w_n - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})(x_n^{(i)})$ for all features n

## $b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})$ 

An important note is that b doesn't utilize the term n

**Cost Function for Multiple Features**

## $J(\vec{w},b) = \frac{1}{2m} \sum_{i=1}^{m} (f_{w,b}(\vec{x}^{(i)}) - y^{(i)})^{2}$

where

## $f_{w,b}(\vec{x}^{(i)}) = \vec{w} \cdot \vec{x}^{(i)} + b$

**Basic Scaling**

### $x_n = \frac{x_n}{max_n}$ where max is the max value of the feature

**Mean Normalization**

### $x_n = \frac{x_n-\mu_n}{max_n-min_n}$ where the max and min are the max and min for the feature, x is the feature parameter and $\mu$ is the mean of the feature in the training set

**Z-Score Normalization**

### $x_n = \frac{x_n - \mu_n}{\sigma_n}$ where $\mu$ is the mean for that feature and $\sigma$ is the standard deviation for that figure

**logistic regression**

## $f_{\vec{w},b}(\vec{x}) = g(\vec{w} \cdot \vec{x} + b) = \frac{1}{1+e^{-(\vec{w} \cdot \vec{x} + b)}}$

**Logistic Regression Loss Functions**

## For y=1, $L(f_{\vec{w},b}(\vec{x}), y^{(i)}) = -\log{(f_{\vec{w},b}(\vec{x}))}$ 

## For y=0, $L(f_{\vec{w},b}(\vec{x}), y^{(i)}) = -\log{(1-f_{\vec{w},b}(\vec{x}))}$ 

These two cases are derived from the following

## $L(f_{\vec{w},b}(\vec{x}), y^{(i)}) = (-y^{(i)}\log{(f_{\vec{w},b}(\vec{x}))}) -(1-y^{(i)})\log{(1-f_{\vec{w},b}(\vec{x}^{(i)}))}$ 

**Logistic Regression Cost Function**

## $J(\vec{w},b) = -\frac{1}{m}\sum_{i=1}^m(y^{(i)}(\log{(f_{\vec{w},b}(\vec{x}))} +(1-y^{(i)})\log{(1-f_{\vec{w},b}(\vec{x}^{(i)}))}))$ 

**Cost function with regularized linear regression**

## $J(\vec{w},b) = \frac{1}{2m} \sum_{i=1}^{m} (f_{w,b}(\vec{x}^{(i)}) - y^{(i)})^{2}+ \frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$

**gradient descent for regularized linear regression**

## $w_j = w_j - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})(x_j^{(i)}) + \frac{\lambda}{m}w_j$ for all features j

## $b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})$ 

**Regularized Logistic Regression Cost Function**

## $J(\vec{w},b) = -\frac{1}{m}\sum_{i=1}^m(y^{(i)}(\log{(f_{\vec{w},b}(\vec{x}))} +(1-y^{(i)})\log{(1-f_{\vec{w},b}(\vec{x}^{(i)}))})) + \frac{\lambda}{2m}\sum_{j=1}^n w_j^2$ 

**Sigmoid Activation Function for a neuron**

## $a_j^{[l]} \cdot \vec{a}^{[l-1]}+b_j^{[l]}$ where l is the layer of the neural network and j is neuron within the layer and keep in mind that $\vec{a}^{[0]}=\vec{x}$
