import unittest
from click.testing import CliRunner

from sanda.cli.entry import cli


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_status_command(self):
        """Test the `status` command outputs the correct status messages."""
        result = self.runner.invoke(cli, ["status"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Sanda is running.", result.output)
        self.assertIn("The server is healthy.", result.output)


if __name__ == "__main__":
    unittest.main()
