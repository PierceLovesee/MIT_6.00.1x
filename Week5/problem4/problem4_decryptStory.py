def decrypt_story():
    s = get_story_string()
    story = CiphertextMessage(s)
    return story.decrypt_message()
