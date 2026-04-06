import json
import unittest
from pathlib import Path

from src.infer import predict
from src.optimize import optimize
from src.train import train_centroid_model


class PipelineTest(unittest.TestCase):
    def test_train_builds_centroids(self):
        rows = [
            ("1.0", "1.0", "A"),
            ("1.2", "0.8", "A"),
            ("4.0", "4.0", "B"),
            ("3.8", "4.2", "B"),
        ]
        model = train_centroid_model(rows)
        self.assertEqual(model["model_type"], "centroid_classifier")
        self.assertIn("A", model["centroids"])
        self.assertIn("B", model["centroids"])

    def test_optimize_marks_model_for_edge(self):
        model = {
            "centroids": {"A": {"x": 1.0, "y": 1.0}, "B": {"x": 4.0, "y": 4.0}}
        }
        optimized = optimize(model)
        self.assertTrue(optimized["optimized"])
        self.assertEqual(optimized["deployment_target"], "edge-device")

    def test_infer_predicts_nearest_centroid(self):
        model = {
            "centroids": {"A": {"x": 1.0, "y": 1.0}, "B": {"x": 4.0, "y": 4.0}}
        }
        label, distance = predict(model, 1.1, 1.0)
        self.assertEqual(label, "A")
        self.assertLess(distance, 0.2)


if __name__ == "__main__":
    unittest.main()
