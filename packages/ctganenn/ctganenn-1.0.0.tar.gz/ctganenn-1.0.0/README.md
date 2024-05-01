# CTGAN-ENN

Welcome to CTGAN-ENN : Tabular GAN-based Hybrid sampling method.

## Installation

Install using pip:

```bash
pip install ctganenn==1.0
```

## Usage

### Variables

- minClass: the minority class in the dataset (dataframe).
- majClass: the majority class in the dataset (dataframe).
- genData: how much data that you want generate from minorty class.
- targetLabel: what is your target label name in dataset.

### Example Usage
```bash
from ctganenn import CTGANENN
```

# use the CTGANENN function with 4 variables
```bash
CTGANENN(minClass,majClass,genData,targetLabel)
```
### Output
the output of method are X and y :
- X : all features of your dataset
- y : target label of your dataset

For example using Decision Tree Classifier

```bash
model = tree.DecisionTreeClassifier()
classification = model.fit(X, y)
```

you can process the X and y variable to the next step for classification stage

