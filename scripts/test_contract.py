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

    def test_formats_integer_cents_without_float_rounding(self):
        for amount, expected in ((350, "3.50"), (0, "0.00"), (-1, "-0.01"), (123456789012345, "1234567890123.45")):
            with self.subTest(amount=amount):
                self.assertEqual(calculator.format_cents(amount), expected)


if __name__ == "__main__":
    unittest.main()
