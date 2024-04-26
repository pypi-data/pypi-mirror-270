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

    @staticmethod
    def from_x_y_split(x, y, test_size=0.2, val_size=0):
        indices = torch.randperm(x.size(0))
        first_split = 1 - test_size - val_size
        second_split = 1 - val_size

        train_indices = indices[: int(first_split * x.size(0))]
        test_indices = indices[
            int(first_split * x.size(0)) : int(second_split * x.size(0))
        ]
        val_indices = indices[int(second_split * x.size(0)) :]

        x_train, y_train = x[train_indices], y[train_indices]
        x_test, y_test = x[test_indices], y[test_indices]
        x_val, y_val = x[val_indices], y[val_indices]

        return ModelDataset(x_train, y_train, x_test, y_test, x_val, y_val)


class ModelUploader:
    def __init__(
        self,
        model_id: str,
        model: torch.nn.Module,
        dataset: ModelDataset,
        loss_fn="mse",
        optimizer="adam",
    ):
        self.model_id = model_id
        self.model = model
        self.summary = None
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.dataset = dataset

        if hasattr(model, "reset_parameters"):
            model.reset_parameters()

    def _publish(self):
        with TemporaryFile() as dataset_file:
            joblib.dump(self.dataset, dataset_file)
            dataset_file.seek(0)
            files = {"dataset": dataset_file}

            payload = {
                "model_id": self.model_id,
                "summary": self.summary,
                "loss_fn": self.loss_fn,
                "optimizer": self.optimizer,
            }

            response = requests.post(
                f"{BASE_URL}:{PORT}/api/publish",
                files=files,
                data=payload,
            )

        if response.status_code == 200:
            print("Model published successfully.")
        else:
            print(
                f"Failed to publish model. Status code: {response.status_code}, Response: {response.text}"
            )

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

    def publish(self):
        infer_size = (1,) + self.dataset.x_train[0].shape
        self._build_summary(infer_size)
        self._publish()
