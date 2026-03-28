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
- Writes to a **unique file** each call: `tts_HHMMSS_XXXX.mp3` (timestamp + 4-char id). The full path is printed to stdout — **always use that printed path**.
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

Output (both cases): the script prints the full path to stdout, e.g. `/app/workspace/tts_143052_a1b2.mp3`

### Constraints

- Never pass translations, helper prefixes, or mixed-language text.
- Never inline API keys in the command.
- Always attach the **path printed by the script** as media via `message`. Do not hardcode a filename.
