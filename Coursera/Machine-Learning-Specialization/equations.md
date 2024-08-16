**Univariate Linear Regression** - $\hat{y}^{(i)} = wx^{(i)} + b$

**Squared Error Cost Function** -  $J(w,b) = \frac{\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^{2}}{2m}$ where m is the number of training examples, $\hat{y}^(i)$ or $f_{w,b}(x^{(i)}$ is the value of the line that we're proposing, and $y^{(i)}$ is the actual value. Remember that $f_{w,b}(x^{(i)} = wx^{(i)} + b$ from univariate linear regression above.

**Gradient Descent** - $w = w - \alpha (\frac{\partial}{\partial w}J(w,b))$ and $b = b - \alpha (\frac{\partial}{\partial b}J(w,b))$

**Gradient Descent (without derivatives)**

$w = w - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})(x^{(i)})$

$b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})$

**Multiple Linear Regression** - $f_{w,b}(x) = w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{3}+...+w_{n}x_{n}+b$ where n is the number of features

**Multiple Linear Regression** (vector notation) - $f_{\vec{w},x}(\vec{x})=\vec{w} \cdot \vec{x} + b$

**Gradient Descent for Multiple Linear Regression**

## $w_n = w_n - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})(x_n^{(i)})$ for all features n

## $b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})$ 

An important note is that b doesn't utilize the term n

**Cost Function for Multiple Features**

## $J(\vec{w},b) = \frac{1}{2m} \sum_{i=1}^{m} (f_{w,b}(\vec{x}^{(i)}) - y^{(i)})^{2}$

where

## $f_{w,b}(\vec{x}^{(i)}) = \vec{w} \cdot \vec{x}^{(i)} + b$