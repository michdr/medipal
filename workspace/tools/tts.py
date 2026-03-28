"""ElevenLabs text-to-speech tool for MediPal."""

import argparse
import json
import os
import sys
from pathlib import Path
from urllib import error, request

VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = Path(__file__).resolve().parents[1]


def text_to_speech(text: str, voice_id: str = VOICE_ID) -> str:
    """Convert text to speech and return the output file path."""
    api_key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("ELEVENLABS_API_KEY is not set")

    req = request.Request(
        url=f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=json.dumps({
            "text": text,
            "model_id": MODEL_ID,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }).encode(),
        method="POST",
        headers={
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        },
    )

    try:
        with request.urlopen(req, timeout=60) as resp:
            audio = resp.read()
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"ElevenLabs API error ({exc.code}): {body}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"ElevenLabs request failed: {exc.reason}") from exc

    filename = "tts_output.mp3"
    output_path = OUTPUT_DIR / filename
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_bytes(audio)
    return str(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MediPal TTS")
    parser.add_argument("text", help="Text to speak")
    parser.add_argument("voice_id", nargs="?", default=VOICE_ID)
    args = parser.parse_args()

    try:
        path = text_to_speech(args.text, args.voice_id)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

    print(path)
