import requests
import numpy
import grequests
import io
from tqdm import tqdm

class ModelExecutor():
    def __init__(self, model_id: str, **kwargs):
        """ Constructor for the execute class

        Args:
            model_id (_type_): The model id to be executed
        """
        self.model_id = model_id
        self.kwargs = kwargs

    def run_FHE_model(self, X, client, URL, serialized_evaluation_keys):
        encrypted_input = None
        clear_input = None

        # Update all base64 queries encodings with UploadFile
        response = requests.post(
            f"{URL}/add_key", files={"key": io.BytesIO(initial_bytes=serialized_evaluation_keys)}
        )
        assert response.status_code == 200
        uid = response.json()["uid"]

        inferences = []
        # Launch the queries
        for i in tqdm(range(len(X))):
            clear_input = X[[i], :]

            assert isinstance(clear_input, numpy.ndarray)
            encrypted_input = client.quantize_encrypt_serialize(clear_input)
            assert isinstance(encrypted_input, bytes)

            inferences.append(
                grequests.post(
                    f"{URL}/compute",
                    files={
                        "model_input": io.BytesIO(encrypted_input),
                    },
                    data={
                        "uid": uid,
                    },
                )
            )

        # Unpack the results
        decrypted_predictions = []
        for result in grequests.map(inferences):
            if result is None:
                raise ValueError("Result is None, probably due to a crash on the server side.")
            assert result.status_code == 200

            encrypted_result = result.content
            decrypted_prediction = client.deserialize_decrypt_dequantize(encrypted_result)[0]
            decrypted_predictions.append(decrypted_prediction)
        print(decrypted_predictions)
        return decrypted_predictions