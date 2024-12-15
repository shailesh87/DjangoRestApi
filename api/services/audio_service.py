from pydub import AudioSegment

def extract_audio_snippets(audio_file_path, timestamps):
    """
    Extract snippets from the audio file based on provided timestamps.

    :param audio_file_path: Path to the audio file
    :param timestamps: List of dictionaries with "start" and "end" keys
    :return: List of paths to the exported audio snippets
    """
    try:
        # Load audio file
        audio = AudioSegment.from_file(audio_file_path)

        # List to store paths of exported snippets
        snippet_paths = []

        # Process each timestamp
        for i, segment in enumerate(timestamps):
            start_ms = int(segment['start'] * 1000)  # Convert seconds to milliseconds
            end_ms = int(segment['end'] * 1000)
            snippet = audio[start_ms:end_ms]

            # Export snippet to file
            snippet_file = f"split_audio_{i}.mp3"
            snippet.export(snippet_file, format="mp3")
            snippet_paths.append(snippet_file)

        return snippet_paths

    except Exception as e:
        raise ValueError(f"Error processing audio: {e}")
