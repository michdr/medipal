# Tools

## text_to_speech (exec)

Generates MP3 audio via ElevenLabs.

### Usage

```
python3 tools/tts.py "<text>" [voice_id]
```

- `text` — the exact target-language phrase to speak. Must be single-language, no helper text.
- `voice_id` — optional ElevenLabs voice ID (default: Rachel).
- Prints the output MP3 file path to stdout.
- Requires `ELEVENLABS_API_KEY` in environment.

### Example

```
python3 tools/tts.py "Ich brauche ein Hustenmittel. Ich bin allergisch gegen Penicillin."
```

Output: `/app/workspace/alert.mp3`

### Constraints

- Never pass translations, helper prefixes, or mixed-language text.
- Never inline API keys in the command.
- Send the printed path as media via `message`.
