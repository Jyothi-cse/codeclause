import pyaudio
import wave

def record_audio(output_file, duration=5, channels=1, rate=44100, chunk=1024, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=format, channels=channels, rate=rate,
                        input=True, frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    record_audio(output_file)
