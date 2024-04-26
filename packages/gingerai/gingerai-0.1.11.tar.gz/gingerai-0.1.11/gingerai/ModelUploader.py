


import torchsummary
import torch
import requests
import io
import sys
import numpy as np

BASE_URL = "http://localhost"
PORT = 5000

class ModelParams:
    def __init__(self, x_train, y_train, x_test, y_test, optimizer="adam", loss="mse", x_val=None, y_val=None):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.x_val = x_val
        self.y_val = y_val
        self.optimizer = optimizer
        self.loss = loss
    
    def json(self):
        dataset_info = {
            "x_train": self.x_train,
            "y_train": self.y_train,
            "x_test": self.x_test,
            "y_test": self.y_test
        }
        
        if self.x_val is not None and self.y_val is not None:
            dataset_info["x_val"] = self.x_val
            dataset_info["y_val"] = self.y_val

        return {
            "dataset": dataset_info,
            "train": {
                "optimizer": self.optimizer,
                "loss": self.loss
            }
        }
    
class ModelUploader:
    """
    Publish does in order
    - pipeline (AI Agent to optimize model
    """
    def __init__(self, model: torch.nn.Module, params: ModelParams):
        self.model = model
        self.summary = None
        
        temp = params.json()
        self.data = temp["dataset"]
        self.optimizer = temp["train"]["optimizer"]
        self.loss = temp["train"]["loss"]
        del temp
        
        if hasattr(model, "reset_parameters"):
            model.reset_parameters()
    
    def _publish(self):
            payload = {
                "summary": str(self.summary),
                "data": str(self.data),
                "optimizer": str(self.optimizer),
                "loss": str(self.loss),
            }
            
            # Perform the POST request
            response = requests.post(f"{BASE_URL}:{PORT}/api/publish", json=payload)
            
            # Check if the request was successful
            if response.status_code == 200:
                print("Model published successfully.")
            else:
                print(f"Failed to publish model. Status code: {response.status_code}, Response: {response.text}")
        
    
    def _build_summary(self, input_size):
        summary_string_io = io.StringIO()
        
        original_stdout = sys.stdout
        sys.stdout = summary_string_io
        
        try:
            torchsummary.summary(self.model, input_size=input_size)
            self.summary = summary_string_io.getvalue()
        finally:
            sys.stdout = original_stdout
            summary_string_io.close()

    def json(self):
        return {
            "summary": self.summary,
            "data": self.data,
            "optimizer": self.optimizer,
            "loss": self.loss
        }
    
    def publish(self, infer_size):
        """
        Args:
            infer_size (np.ndarray): The input size of the model (1, 1, 28, 28) for example for MNIST
        """
        self._build_summary(infer_size)
        self._publish()




