import tator


def test_default_streaming_ladder(host, token, video_type, video):
    """ A video type created without a streaming config follows a streaming profile, and its
    videos are transcoded to the server's Default AV1 ladder (2160/1080/720/360/144). The test
    clip is 1280x720, so it gets the 720, 360 and 144 rungs. """
    api = tator.get_api(host, token)
    media_type = api.get_media_type(video_type)
    assert media_type.streaming_profile is not None
    assert media_type.streaming_config_override is None

    streaming = api.get_media(video).media_files.streaming
    assert sorted(tuple(stream.resolution) for stream in streaming) == [
        (144, 256), (360, 640), (720, 1280)]
    assert {stream.codec for stream in streaming} == {"av1"}
