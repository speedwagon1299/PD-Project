import tf2onnx
import tensorflow as tf

# Load the trained model
# model = tf.keras.models.load_model(r'SSL_Graphs_50_New\disc_sup_0180.h5')
model = tf.keras.models.load_model(r'SSL_Graphs_50_New\gen_model_0180.h5')

# Convert the model to ONNX
onnx_model, _ = tf2onnx.convert.from_keras(model, opset=13)

# Save the ONNX model to file
# with open("disc_sup_trained_model.onnx", "wb") as f:
with open("gen_trained_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
