import moviepy.editor

video = moviepy.editor.VideoFileClip("Pham.mp4")

audio=video.audio
audio.write_audiofile("extract.mp3")