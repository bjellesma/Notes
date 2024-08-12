**Univariate Linear Regression** - $\hat{y}^{(i)} = wx^{(i)} + b$

**Squared Error Cost Function** -  $J(w,b) = \frac{\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^{2}}{2m}$ where m is the number of training examples, $\hat{y}^(i)$ or $f_{w,b}(x^{(i)}$ is the value of the line that we're proposing, and $y^{(i)}$ is the actual value. Remember that $f_{w,b}(x^{(i)} = wx^{(i)} + b$ from univariate linear regression above.

**Gradient Descent** - $w = w - \alpha (\frac{\partial}{\partial w}J(w,b))$ and $b = b - \alpha (\frac{\partial}{\partial b}J(w,b))$

**Gradient Descent (without derivatives)**

$w = w - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})(x^{(i)})$

$b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})$
