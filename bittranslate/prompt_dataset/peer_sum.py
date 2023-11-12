from datasets import load_dataset
from .prompt_dataset import PromptDataset
import random


class PeerSum(PromptDataset):
    def __init__(self):
        super().__init__()
        self._dataset = load_dataset("oaimli/PeerSum", split="train")
        self._dataset = self._dataset.filter(
            lambda record: record["paper_abstract"] is not None
        )
        self._dataset_len = len(self._dataset)
        self._valid_ln = ["en"]

    def sample_case(self, language="en") -> str:
        if language not in self._valid_ln:
            raise ValueError(
                f"{language} is an invalid language. Valid languages include {self._valid_ln}"
            )

        random_index = random.randint(0, self._dataset_len-1)
        return self._dataset[random_index]["paper_abstract"]
