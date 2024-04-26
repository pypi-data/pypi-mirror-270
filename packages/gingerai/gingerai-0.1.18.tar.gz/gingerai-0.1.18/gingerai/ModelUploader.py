

import torch
import torchsummary
import requests
import io
import sys
import joblib
from tempfile import TemporaryFile

BASE_URL = "http://127.0.0.1"
PORT = 5000

class ModelDataset:
    def __init__(self, x_train, y_train, x_test, y_test, x_val=None, y_val=None):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.x_val = x_val
        self.y_val = y_val

class ModelUploader:
    def __init__(self, model: torch.nn.Module, dataset: ModelDataset, optimizer="adam", loss="mse"):
        self.model = model
        self.dataset = dataset
        self.summary = None
        self.optimizer = optimizer
        self.loss = loss
        
        if hasattr(model, "reset_parameters"):
            model.reset_parameters()
    
    def _publish(self):
        with TemporaryFile() as dataset_file:
            joblib.dump(self.dataset, dataset_file)
            dataset_file.seek(0)
            files = {'dataset': dataset_file}
        
        payload = {
            'summary': self.summary,
            'optimizer': self.optimizer,
            'loss': self.loss
        }
        response = requests.post(f"{BASE_URL}:{PORT}/api/publish", files=files, data=payload)

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

    def publish(self, infer_size):
        self._build_summary(infer_size)
        self._publish()







