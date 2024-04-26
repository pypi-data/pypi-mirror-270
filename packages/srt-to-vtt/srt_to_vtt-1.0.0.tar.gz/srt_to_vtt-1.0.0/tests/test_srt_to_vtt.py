import srt_to_vtt

def test_convert():

    srt_to_vtt.srt_to_vtt('test_input.srt', 'output.vtt')

test_convert()