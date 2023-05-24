!pip install -U segmentation-models-pytorch

from segmentation_models_pytorch import Unet

model = Unet('efficientnet-b2', encoder_weights="imagenet")