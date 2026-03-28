# Tools

## text_to_speech (exec)

Generates MP3 audio via ElevenLabs.

### Usage

```
python3 tools/tts.py "<text>" [voice_id]
```

- `text` — the exact phrase to speak. The language depends on relay direction:
  - **User → Provider**: text is in the **target/foreign language**.
  - **Provider → User**: text is in the **user's own language** (e.g. English).
  - Must be single-language, no helper text.
- `voice_id` — optional ElevenLabs voice ID (default: Rachel).
- Always writes to `/app/workspace/tts_output.mp3` (fixed path, overwritten each call).
- Requires `ELEVENLABS_API_KEY` in environment.

### Examples

**User → Provider (German):**
```
python3 tools/tts.py "Ich brauche ein Hustenmittel. Ich bin allergisch gegen Penicillin."
```

**Provider → User (English):**
```
python3 tools/tts.py "The pharmacist says they only have 50 mg tablets. They're asking if two would work."
```

Output (both cases): `/app/workspace/tts_output.mp3`

### Constraints

- Never pass translations, helper prefixes, or mixed-language text.
- Never inline API keys in the command.
- Always attach `/app/workspace/tts_output.mp3` as media via `message`.
