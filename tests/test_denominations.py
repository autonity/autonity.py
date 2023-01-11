"""
Tests for autonity.utils.denominations
"""

from autonity.utils.denominations import (
    format_quantity,
    format_auton_quantity,
    format_newton_quantity,
)

from web3.types import Wei
from unittest import TestCase


class TestDenominations(TestCase):
    """
    Tests for autonity.utils.denominations
    """

    def test_quantity_formatter(self) -> None:
        """
        Test the format_*_quantity functions
        """
        self.assertEqual("3", format_quantity(3, 0))
        self.assertEqual("0.0000003", format_quantity(3, 7))
        self.assertEqual("0.000000000000000003", format_quantity(3, 18))

        self.assertEqual("0.000000000000000012", format_auton_quantity(Wei(12)))
        self.assertEqual("12", format_newton_quantity(12))
