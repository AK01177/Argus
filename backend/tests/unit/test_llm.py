from unittest.mock import patch, MagicMock
from app.providers.llm import GeminiProvider

# We patch the google genai Client so it doesn't make real network requests
@patch("app.providers.llm.genai.Client")
def test_gemini_provider_summarize(mock_client_class):
    # 1. Setup the fake Mock Client
    mock_client_instance = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "This is a mocked summary of the code."
    
    mock_client_instance.models.generate_content.return_value = mock_response
    mock_client_class.return_value = mock_client_instance

    # 2. Run our provider
    provider = GeminiProvider()
    
    # We don't need a real API key because the client is completely mocked!
    result = provider.summarize_file("main.py", "print('hello world')")

    # 3. Assert the results
    assert result == "This is a mocked summary of the code."
    
    # Verify it called the Gemini API with the correct model
    mock_client_instance.models.generate_content.assert_called_once()
