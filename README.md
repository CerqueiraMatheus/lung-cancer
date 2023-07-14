# Lung cancer detection

> Final project develop for the Machine Learning course at ICMC/USP during 2023/1. It presents multiple approachs for lung cancer detection in Computerized Tomography (CT).

## Install

```bash
pip install .
```

## Notebooks

Our project is built in the ``/notebooks`` folder. Please, first read the following file:

* ``yolo_detection.ipynb``: present the project, dataset, YOLO results and examples;

There are references to other files:

* ``reader.ipynb``: read the original dataset and convert it to ``.jpg`` images and ``.csv`` files;
* ``converter.ipynb``: convert the processed dataset to YOLO format;
* ``yolo_model.ipynb``: execute the YOLO model;

Finally, we also tried a custom approach:

* ``custom_detection.ipynb``: present our custom model and its results.
