
from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from matplotlib import pyplot as plt

class Detector:
    def __init__(self): 
        # Loading a model with pre-trained weights
        model_path = hf_hub_download(repo_id="armvectores/yolov8n_handwritten_text_detection",
                                     filename="best.pt")
        self.model = YOLO(model_path)

    def detect(self, img_path):
        # Performing detection
        results = self.model.predict(source=img_path, project='.',name='detected', exist_ok=True, save=True, show=False, show_labels=False, show_conf=False, conf=0.5)
        return results

# Creating an instance of the detector
detector = Detector()

# Uploading a test image
test_blank_path = hf_hub_download(repo_id="armvectores/yolov8n_handwritten_text_detection",
                                  filename="test_blank.png")

# Performing detection
detector.detect(test_blank_path)

# Output of the result
plt.figure(figsize=(15,10))
detected_image_path = 'detected/test_blank.png'  # Make sure that the path corresponds to the actual location of the saved image
plt.imshow(plt.imread(detected_image_path))
plt.show()

