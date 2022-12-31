import moviepy.editor
from pathlib import Path

s = input('Name of file: ')
video_file = Path(f'{s}.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')