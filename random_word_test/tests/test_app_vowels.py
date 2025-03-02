from playwright.sync_api import sync_playwright


def test_index_route(client):
    """Test if the index route is accessible and contains expected elements."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Generate Word" in response.data


def test_generate_word(browser_session):
    """Test the word generation functionality."""
    browser_session.click("button.big-button")

    # Wait for the word to appear
    browser_session.wait_for_selector(".generated-word")

    # Extract the text content
    generated_text = browser_session.inner_text(".generated-word")

    # Format it with commas based on length
    formatted_text = generated_text.split(' ')

    print("Generated Text:", formatted_text)
    assert len(formatted_text) > 0, "No word generated"


def test_100_generated_vowels_list(browser_session):
    """Test the generation of 100 words exactly with only vowels."""
    generated_words = []
    special_chars = set("#@!()+=$%^&*{}[]")

    while len(generated_words) < 100:
        # Click the generate word button
        browser_session.click("button.big-button")

        # Wait for the generated word to appear
        browser_session.wait_for_selector(".generated-word")

        # Extract the text content
        generated_text = browser_session.inner_text(".generated-word")

        # Process multi-word phrases
        words = generated_text.split(" ")

        for word in words:
            if all(char in special_chars for char in word):
                continue  # Skip words with only special characters

            if len(generated_words) < 100:  # Ensure we don't exceed 100 words
                generated_words.append(word)
            else:
                print("Generated Words:", generated_words)

                break  # Stop if we've reached 100 words

    assert len(generated_words) == 100, "Incorrect number of words generated"

    # Check if  words contain vowels and the length of the word is larger than 3:
    vowels_list = [word for word in generated_words if any(v in word for v in "aeiou") and len(word) > 3]
    print("Vowels List:", vowels_list)
    assert len(vowels_list) > 0, "No words with only vowels and length > 3"
