#! Convert .mp3 to .mp4
from pydub import AudioSegment
for issue in ["a", "b", "c", "d", "e", "f", "g"]:
    snippet = AudioSegment.from_mp3(f"outputs/issue_{issue}.mp3")
    snippet.export(f"outputs/issue_{issue}.mp4", format="mp4")