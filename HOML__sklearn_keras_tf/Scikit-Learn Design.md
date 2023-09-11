# Scikit-Learn Design

* Scikit-Learn’s API is remarkably well designed. These are the [main design principles](https://arxiv.org/abs/1309.0238):

### **Consistency**:
* All objects share a consistent and simple interface:

* *Estimators* :
    * Any object that can estimate some parameters based on a dataset is called an estimator (e.g., a `SimpleImputer` is an estimator). The estimation itself is performed by the `fit()` method, and it takes a dataset as a parameter, or two for supervised learning algorithms—the second dataset contains the labels. 
    * Any other parameter needed to guide the estimation process is considered a hyperparameter (such as a SimpleImputer’s `strategy`), and it must be set as an instance variable (generally via a constructor parameter).

* *Transformers* :
    * Some estimators (such as a `SimpleImputer`) can also transform a dataset; these are called transformers.
    * The API is simple: the transformer is performed by the `transform()` method w/ the dataset to transform as a parameter. It returns the transformed dataset. This transformation relies on the learned parameters.
    * All transformers also have a convenience method called `fit_transform()`, w/c is equivalent to `fit()` and then `transform()` (but somethimes `fit_transform()` is optimized and runs much faster).

* *Predictors* :
    * Some estimators, given a dataset, are capable of making predictions; they are called predictors.
    * A predictor has a `predict()` method that takes a dataset of new instances and returns a dataset of corresponding predictions. It also has a `score()` method that measures the quality of the predictions, given a test set (and the corresponding labels, in the case of supervised learning algorithms).

### **Inspection**:
* All the estimator’s hyperparameters are accessible directly via public instance variables , and all the estimator’s learned parameters are accessible via public instance variables with an underscore suffix.

### **Nonproliferation of classes**:
* Datasets are represented as NumPy arrays or SciPy sparse matrices, instead of homemade classes. Hyperparameters are just regular Python strings or numbers.

### **Composition**:
* Existing building blocks are reused as much as possible. For example, it is easy to create a Pipeline estimator from an arbitrary sequence of transformers followed by a final estimator.

### **Sensible Defaults**:
* Scikit-Learn provides reasonable default values for most parameters, making it 
easy to quickly create a baseline working system.
