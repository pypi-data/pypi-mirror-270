import sys
import os
import speech_recognition as sr
import wave


def transcribe_audio(audio_file, language="en-US"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Language code provided by the user
        transcript = recognizer.recognize_google(audio_data, language=language)
        return transcript.split()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def get_audio_duration(audio_file):
    with wave.open(audio_file, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration


def get_equal_duration(timestamps, total_duration):
    num_words = len(timestamps)
    return total_duration / num_words


def get_timestamps_with_equal_duration(words, total_duration):
    duration_per_word = get_equal_duration(words, total_duration)
    timestamps = []
    start_time = 0
    for word in words:
        end_time = start_time + duration_per_word
        timestamps.append((word, start_time, end_time))
        start_time = end_time
    return timestamps


def write_to_textgrid(output_file, timestamps):
    with open(output_file, "w") as file:
        file.write("File type = \"ooTextFile\"\n")
        file.write("Object class = \"TextGrid\"\n\n")
        file.write("xmin = 0\n")
        file.write(f"xmax = {timestamps[-1][2]}\n")
        file.write("tiers? <exists>\n")
        file.write("size = 1\n")
        file.write("item []:\n")
        file.write("    item [1]:\n")
        file.write("        class = \"IntervalTier\"\n")
        file.write("        name = \"words\"\n")
        file.write("        xmin = 0\n")
        file.write(f"        xmax = {timestamps[-1][2]}\n")
        file.write("        intervals: size = {}\n".format(len(timestamps)))
        for i, (word, start_time, end_time) in enumerate(timestamps, start=1):
            file.write(f"        intervals [{i}]:\n")
            file.write(f"            xmin = {start_time}\n")
            file.write(f"            xmax = {end_time}\n")
            file.write(f"            text = \"{word}\"\n")


def print_help():
    print("praanscribe is small application for automatically transcribing audio and creating TextGrid files to be used in Praat.")
    print("\nUsage:")
    print("python praanscribe.py <language_code> <audio_file>")
    print("\nArguments:")
    print(
        "<language_code>: Language code indicating the language of the audio such as 'en', 'tr', 'fr', or more specific dialects like 'en-US', 'tr-TR', etc.")
    print("<audio_file>: Path to the audio file (.wav) you want to transcribe.")
    print("\nOutput:")
    print(
        "The output is a simple TextGrid file where each word has the same length, stretching through the duration of the audio. This file, along with the audio can be further edited and analyzed using Praat.")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print_help()
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Invalid arguments. Use --help for usage instructions.")
        sys.exit(1)

    language_code = sys.argv[1]
    audio_file = sys.argv[2]
    output_file = os.path.splitext(audio_file)[0] + ".TextGrid"
    words = transcribe_audio(audio_file, language=language_code)
    if words:
        total_duration = get_audio_duration(audio_file)
        timestamps = get_timestamps_with_equal_duration(words, total_duration)
        write_to_textgrid(output_file, timestamps)


if __name__ == "__main__":
    main()