from transformers import pipeline
from recycle_ai.base.model import Model


class GarbageClassification(Model):
    def __init__(self):
        print("[INFO] get garbage classification model")
        self.garbage_classification = pipeline(
            "image-classification", model="yangy50/garbage-classification"
        )

    def expect(self, data):
        print("[INFO] garbage classification expecting")
        result = self.garbage_classification(data)

        best = {"label": "", "score": 0}

        for buf in result:
            if buf["score"] > best["score"]:
                best = buf

        return best
