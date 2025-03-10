**Checkpoints**

Contains weights as accessed from the codes in "OptimizerComparisons"(Predict_Nadam_CNN.ipynb) and "OtherNetworks"

**Data**

Contains Train Val Test Split from PPMI Dataset obtained through https://ida.loni.usc.edu/
SPECT DaT-SCAN Images of PD and HC used.

**Documents**

Containing the Word Documents with organized results of:

1. Network Architecture Comparisons
2. Optimizers
3. Parameter Finetuning
4. Base Theory behind SGAN
5. Results of SGAN based on sample sizes

**onnx**

Contains code to generate the architecture of the Generator and Discriminator using ONNX
Visualized using netron.app (shown in respectively named png)

**OptimizerComparisons**

Discriminator model trained and evaluated using the following Optimizers:

1. AdaDelta
2. Adam
3. Nadam
4. RMSProp
5. SGD

Results documented in Documents/Optimizer.docx

**OtherNetworks**

Results of SOTA models on dataset obtained.
Documented in Documents/"Network Architecture Comparisons".docx

**Saved Weights**

Weights obtained during OptimizerComparisons phase

**SSL_Graphs**

Generator and Discriminator Weights + Generated plots
for various sample sizes.
Results Documented in Documents/SSL_GAN_Analysis.docx
