# MediPal

AI-powered medical communication relay that converts urgent health needs into speakable audio for non-native speakers abroad.

Built on [nanobot](https://github.com/HKUDS/nanobot) with OpenRouter for LLM and ElevenLabs for TTS.

## How it works

You message MediPal (via Telegram) with a medical need — pharmacy visit, ER situation, allergy warning, dietary restriction. MediPal produces a short, clear phrase in the local language and generates audio you can play directly to staff.

## Setup

1. Install [uv](https://docs.astral.sh/uv/):

```bash
brew install uv
```

2. Configure environment:

```bash
cp .env.example .env
# Fill in OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN, ELEVENLABS_API_KEY
```

3. Install dependencies:

```bash
uv sync
```

4. Run:

```bash
uv run --env-file .env nanobot gateway
```

## Deploy on Railway

1. Connect this repo to a Railway project.
2. Set the three environment variables from `.env.example` in the Railway dashboard.
3. Deploy — Railway auto-detects the Dockerfile.

## Project layout

```
├── config.json              # Nanobot runtime config
├── pyproject.toml           # Python dependencies (uv)
├── Dockerfile               # Railway-compatible container
├── .env.example             # Required environment variables
└── workspace/
    ├── AGENTS.md            # Behavior rules and output format
    ├── IDENTITY.md          # Who MediPal is
    ├── TOOLS.md             # TTS tool documentation
    ├── USER.md              # User profile template
    └── tools/
        └── tts.py           # ElevenLabs text-to-speech tool
```

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `OPENROUTER_API_KEY` | Yes | OpenRouter API key for LLM |
| `OPENROUTER_BASE_URL` | No | Defaults to `https://openrouter.ai/api/v1` |
| `TELEGRAM_BOT_TOKEN` | Yes | Telegram bot token from @BotFather |
| `ELEVENLABS_API_KEY` | Yes | ElevenLabs API key for TTS |
