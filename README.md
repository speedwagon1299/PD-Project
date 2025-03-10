# **PD-Project: Parkinson's Disease Classification and SGAN Analysis**

## **Project Overview**

This repository contains models, datasets, and analysis related to Parkinson's Disease (PD) classification using various neural network architectures. It also includes a comparative study of optimizers, fine-tuning parameters, and SGAN-based sample efficiency analysis.

---

## **Repository Structure**

### 📁 **Checkpoints**

Contains trained model weights accessed by scripts in:

-   `OptimizerComparisons/Predict_Nadam_CNN.ipynb`
-   `OtherNetworks/`

---

### 📁 **Data**

-   **Dataset:** Train, validation, and test split from the **PPMI Dataset** (obtained from [IDA LONI](https://ida.loni.usc.edu/)).
-   **Images Used:** SPECT DaT-SCAN images of PD and HC (Healthy Control).

---

### 📁 **Documents**

Contains organized research and results, including:

1. 📄 **Network Architecture Comparisons**
2. 📄 **Optimizer Performance Analysis**
3. 📄 **Parameter Fine-Tuning Experiments**
4. 📄 **Base Theory Behind SGAN (Semi-Supervised GANs)**
5. 📄 **SGAN Results on Different Sample Sizes**

---

### 📁 **onnx**

-   Code to generate the **Generator** and **Discriminator** architectures using **ONNX**.
-   **Visualization:** Network structures visualized via [Netron](https://netron.app/).

---

### 📁 **OptimizerComparisons**

A comparative study of discriminator training performance using different optimizers:  
✔ **AdaDelta**  
✔ **Adam**  
✔ **Nadam**  
✔ **RMSProp**  
✔ **SGD**

📄 **Results:** Documented in `Documents/Optimizer.docx`.

---

### 📁 **OtherNetworks**

-   Implementation and evaluation of **state-of-the-art (SOTA)** models on the dataset.
-   📄 **Results:** Documented in `Documents/Network Architecture Comparisons.docx`.

---

### 📁 **Saved Weights**

-   Model weights obtained during the **OptimizerComparisons** phase.

---

### 📁 **SSL_Graphs**

-   **Generator & Discriminator Weights** for different sample sizes.
-   **Generated Plots** visualizing results.
-   📄 **Results:** Documented in `Documents/SSL_GAN_Analysis.docx`.

---

## 📝 **Acknowledgment**

-   Data sourced from **[PPMI Dataset](https://ida.loni.usc.edu/)**.
-   Visualizations made with **Netron**.
-   Implementation inspired by **SOTA deep learning techniques** for PD classification.
-   Bhattiprolu, S. (2023, August 23). 259 - Semi-supervised learning with GANs - in keras [Video]. YouTube. https://youtu.be/mjftYIKSlLQ
