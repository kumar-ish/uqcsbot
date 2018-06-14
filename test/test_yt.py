"""
Tests for yt.py
"""
from test.conftest import MockUQCSBot, TEST_CHANNEL_ID
from test.helpers import generate_message_object

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='
# TODO(mitch): work out a way to get this from yt.py without triggering
# 'on_command' to be called and add '!yt' as a handler which messes with
# testing.
NO_QUERY_MESSAGE = "You can't look for nothing. !yt <QUERY>"

def test_yt_no_query(uqcsbot: MockUQCSBot):
    message = generate_message_object(TEST_CHANNEL_ID, "!yt")
    uqcsbot.post_and_handle_message(message)
    channel = uqcsbot.test_channels.get(TEST_CHANNEL_ID)
    assert channel is not None
    messages = channel.get('messages', [])
    assert len(messages) == 2
    assert messages[-1]['text'] == NO_QUERY_MESSAGE

def test_yt_normal(uqcsbot: MockUQCSBot):
    message = generate_message_object(TEST_CHANNEL_ID, "!yt dog")
    uqcsbot.post_and_handle_message(message)
    channel = uqcsbot.test_channels.get(TEST_CHANNEL_ID)
    assert channel is not None
    messages = channel.get('messages', [])
    assert len(messages) == 2
    assert messages[-1]['text'][0:len(YOUTUBE_VIDEO_URL)] == YOUTUBE_VIDEO_URL
