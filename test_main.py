import unittest
from unittest.mock import patch
import subprocess
import tempfile
import os


class TestMain(unittest.TestCase):
    def test_extract(self):
        result = subprocess.run(
            ["python", "main.py", "extract"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Extracting data...", result.stdout)

    @patch("databricks.sql.connect")
    def test_transform_load(self, mock_connect):
        result = subprocess.run(
            ["python", "main.py", "transform_load"],
            capture_output=True,
            text=True,
        )
        print(f"Return Code: {result.returncode}")  # Add this line for debugging
        print(result.stdout)  # Print the subprocess stdout for further clues
        print(result.stderr)  # Print the subprocess stderr for further clues
        self.assertEqual(result.returncode, 0)

    def test_general_query(self):
        query = (
            "SELECT a.state, "
            "AVG(a.median_household_income) AS average_median_household_income, "
            "AVG(a.share_unemployed_seasonal) AS average_share_unemployed_seasonal, "
            "a.share_population_in_metro_areas, "
            "b.gini_index "
            "FROM default.hate_crimes1DB AS a "
            "JOIN default.hate_crimes2DB AS b ON a.state = b.state "
            "GROUP BY a.state, a.share_population_in_metro_areas, b.gini_index "
            "ORDER BY b.gini_index "
            "LIMIT 5"
        )

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as query_file:
            # Write the query to a temporary file
            query_file.write(query)
            query_file.close()

            try:
                result = subprocess.run(
                    ["python", "main.py", "general_query", query_file.name],
                    capture_output=True,
                    text=True,
                )
                # Log the query and result for debugging purposes
                with open("query_result.log", "w") as log_file:
                    log_file.write(f"Query: {query}\n")
                    log_file.write(f"Result: {result.stdout}\n")

                print(
                    f"Return Code: {result.returncode}"
                )  # Add this line for debugging
                self.assertEqual(result.returncode, 0)
            except Exception as e:
                print(f"Exception: {str(e)}")
            finally:
                # Clean up the temporary query file
                os.remove(query_file.name)


if __name__ == "__main__":
    unittest.main()
