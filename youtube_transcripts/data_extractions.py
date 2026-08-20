import json
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


# ============================================================
# Configuration
# ============================================================

VIDEO_ID = "Y7m9eNoB3NU"
LANGUAGES = ["en"]

OUTPUT_DIR = Path("data/transcripts")


# ============================================================
# Functions
# ============================================================

def fetch_transcript(video_id: str, languages: list[str]):
    """
    Fetch the YouTube transcript while preserving timestamps.
    """
    api = YouTubeTranscriptApi()

    return api.fetch(
        video_id,
        languages=languages
    )


def save_raw_json(video_id: str, transcript, output_dir: Path):
    """
    Save the original transcript including timestamps.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "video_id": video_id,
        "language": "pt",
        "transcript": [
            {
                "start": snippet.start,
                "duration": snippet.duration,
                "text": snippet.text
            }
            for snippet in transcript
        ]
    }

    output_file = output_dir / f"{video_id}_raw.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    return output_file


def save_raw_txt(video_id: str, transcript, output_dir: Path):
    """
    Save the raw transcript as plain text.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{video_id}_raw.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for snippet in transcript:
            f.write(snippet.text.strip())
            f.write("\n")

    return output_file


def save_continuous_txt(video_id: str, transcript, output_dir: Path):
    """
    Join all transcript snippets into a continuous text.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{video_id}_continuous.txt"

    text = " ".join(
        snippet.text.strip()
        for snippet in transcript
        if snippet.text.strip()
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    return output_file


# ============================================================
# Main
# ============================================================

def main():

    print(f"Downloading transcript for: {VIDEO_ID}")

    try:
        transcript = fetch_transcript(
            VIDEO_ID,
            LANGUAGES
        )

        print(f"Transcript retrieved: {len(transcript)} snippets")

        json_file = save_raw_json(
            VIDEO_ID,
            transcript,
            OUTPUT_DIR
        )

        txt_file = save_raw_txt(
            VIDEO_ID,
            transcript,
            OUTPUT_DIR
        )

        continuous_file = save_continuous_txt(
            VIDEO_ID,
            transcript,
            OUTPUT_DIR
        )

        print("\nFiles created:")
        print(f"  JSON:       {json_file}")
        print(f"  TXT:        {txt_file}")
        print(f"  Continuous: {continuous_file}")

    except Exception as e:
        print("\nERROR:")
        print(e)


if __name__ == "__main__":
    main()