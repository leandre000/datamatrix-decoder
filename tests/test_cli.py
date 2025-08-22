from click.testing import CliRunner

def test_decode_command():
    runner = CliRunner()
    result = runner.invoke(decode, ['test.png'])
    assert result.exit_code == 0

