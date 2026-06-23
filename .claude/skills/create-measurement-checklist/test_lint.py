from __future__ import annotations

import unittest

from _build_checklist import BuildError, Column, Table, parse_column, validate_table


class DerivedInputLintTest(unittest.TestCase):
    def test_derived_without_raw_input_fails(self):
        table = Table(ac="AC X", part="Part X", code="Table X", model="mock")
        table.indep_values = ["row1"]
        table.columns = [
            Column(name="항목", unit="", kind="independent"),
            Column(name="Measured", unit="", kind="derived", formula="A/B", expected=["1"]),
        ]

        with self.assertRaisesRegex(BuildError, "no raw input source"):
            validate_table(table)

    def test_pipe_in_symbol_does_not_split_field(self):
        col = parse_column(
            "Thevenin Equivalent | kind: derived | formula: |Z_Th|=sqrt(R^2+X_L^2) | expected: 1"
        )

        self.assertEqual(col.formula, "|Z_Th|=sqrt(R^2+X_L^2)")
        self.assertEqual(col.expected, ["1"])


if __name__ == "__main__":
    unittest.main()
