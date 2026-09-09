"""Standalone standard-library test runner for the synthetic canary."""
import importlib.util
from pathlib import Path
import unittest

source = Path(__file__).resolve().parents[1] / "src" / "calculator.py"
spec = importlib.util.spec_from_file_location("canary_calculator", source)
calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)


class ContractTests(unittest.TestCase):
    def test_preserves_plain_label(self):
        self.assertEqual(calculator.display_label("Example"), "Example")

    def test_sums_integer_cents(self):
        self.assertEqual(calculator.total_cents([100, 250]), 350)
        self.assertEqual(calculator.total_cents([]), 0)

    def test_trims_label(self):
        self.assertEqual(calculator.display_label("  Example  "), "Example")


if __name__ == "__main__":
    unittest.main()
