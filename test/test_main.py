from src.main import main

class TestMain:
    def test_main(self):
        assert main() == "Hello World!"