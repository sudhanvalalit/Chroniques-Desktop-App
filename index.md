---
title: Chroniques Desktop App
theme: jekyll-theme-architect
---

# Chroniques Desktop App

_This page is automatically generated from the latest GitHub release and README on main._

## Latest Release
- Version: [Chroniques v2.0.0-1](https://github.com/sudhanvalalit/Chroniques-Desktop-App/releases/tag/v2.0.0-1) (`v2.0.0-1`)
- Published: 2026-05-19
- Downloads:
  - [ChroniquesSetup.exe](https://github.com/sudhanvalalit/Chroniques-Desktop-App/releases/download/v2.0.0-1/ChroniquesSetup.exe)

### Release Notes

## What's Changed
* Fix broken GitHub Pages rendering on gh-pages fallback deploy by @Copilot in https://github.com/sudhanvalalit/Chroniques-Desktop-App/pull/1

## New Contributors
* @Copilot made their first contribution in https://github.com/sudhanvalalit/Chroniques-Desktop-App/pull/1

**Full Changelog**: https://github.com/sudhanvalalit/Chroniques-Desktop-App/commits/v2.0.0-1

Features added:
- login
- keybindings
- borders in journal as well as pdf

Included source commit: [44b6466](https://github.com/sudhanvalalit/Chroniques-Desktop-App/commit/44b64665e27e092fae15c6051f3c6b3cdcc8ed53).

## Features And Documentation

#### Version 2.0 - AI-Powered Journaling

Chroniques is a cross-platform desktop app for journaling with AI-powered features. It includes a rich text editor with formatting, image insertion, spell checking, inline and advanced word cloud visualization, and an AI assistant with multiple provider options.

## ✨ Features

### Core Journaling
- **Rich Text Editor** - Format text with bold, italic, underline, colors, and more
- **Image & Link Insertion** - Embed pictures and hyperlinks directly in entries
    - **Image Resizing** - Hold Ctrl and drag images to resize (maintains aspect ratio)
    - **Move Content** - Use Ctrl+Shift+X to move selected content, Ctrl+Shift+V to paste at new location
- **Text File Attachment** - Add supporting documents to entries
- **PDF Export** - Export journal entries to PDF format
- **Spell Checking** - Built-in spell checker with suggestions
- **Calendar Navigation** - Browse through all your entries by date
- **Full-Text Search** - Find and replace within entries (Search menu with dedicated Find/Replace actions)
- **Auto-Save** - Automatic saving every 30 seconds
- **Statistics Dashboard** - Word counts, editing frequency, and more

### New in v2.0: AI and Platform Features
- **Reorganized Menu Structure** - Improved menu order: Journal → Edit → View → Insert → Format → Search → Tools → Help
- **Word Cloud Generator** - Visualize word frequency from your entries with customizable sizing and export (Tools menu)
- **AI Journal Assistant** - Choose your provider (Tools menu):
    - Anthropic (Claude)
    - OpenAI-compatible APIs (ChatGPT-style endpoints)
    - Local Ollama models (Llama/Mistral)
    - 📊 **Sentiment Analysis** - Understand emotional patterns and mood trends
    - 🏷️ **Auto-Tag** - Generate relevant tags for your entries automatically
    - 📝 **Summarize** - Create condensed summaries of your journal
    - 💡 **Suggestions** - Get personalized writing and wellness recommendations
- **Enhanced Search Menu** - Dedicated Search menu with Find and Replace actions
- **Improved Help Menu Workflow**
    - Contents opens complete in-app documentation
    - Get Help Online opens GitHub Q&A discussions
    - Give Feedback opens an email compose flow
    - About dialog includes app icon and release metadata

## System Requirements
- **Python** 3.8 or higher
- **OS Support**:
    - Windows 8 and above
    - Linux (Ubuntu, Debian, Fedora, Arch, etc.)
    - macOS 10.13 and above

## Installation

### From Pre-Built Binary
1. Download the latest release for your platform from [Releases](https://github.com/sudhanvalalit/Chroniques-Desktop-App/releases)
2. Windows: Run the `.exe` installer
3. Linux/macOS: Extract and run the executable

### From Source

#### Prerequisites
```bash
pip install -r requirements.txt
```

#### Setup API Key (for cloud AI providers)
Set API key as an environment variable if you use Anthropic/OpenAI-compatible endpoints.
For local Ollama usage, API key is not required.

**Linux/macOS:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

Or use System Properties > Environment Variables (Windows) for persistent setup.

#### Run the App
```bash
python src/chronicles.py
```

## Building

### Windows
```bash
.\build_windows.sh
```

### Linux
```bash
bash build_linux.sh
```

### Arch Linux Package (.pkg.tar.zst)
```bash
chmod +x build_arch.sh
./build_arch.sh
```

This routine uses `packaging/arch/PKGBUILD` and produces an Arch package via `makepkg`.

### Debian/Ubuntu Package (.deb)
```bash
chmod +x build_deb.sh
./build_deb.sh
```

This routine builds an installable `.deb` package in `dist/`.

## Documentation

- In-app: Help > Contents
- Local file: `documentation.html`

## AI Provider Setup

You can use one of the following in the AI Assistant dialog:
1. **Anthropic (Claude)**
2. **OpenAI-compatible endpoint**
3. **Ollama (Local Llama/Mistral)**

For local Ollama:
1. Install Ollama
2. Run `ollama serve`
3. Select provider `Ollama (Local Llama/Mistral)` in app
4. Use endpoint `http://localhost:11434/api/chat`

## Support & Feedback

- 🐛 [Report a Bug](https://github.com/sudhanvalalit/Chroniques-Desktop-App/issues)
- 💬 [Q&A / Help](https://github.com/sudhanvalalit/Chroniques-Desktop-App/discussions/categories/q-a)
- 📫 [Feedback Email](mailto:chroniquesdesktop@gmail.com)
- 📧 Email: chroniquesdesktop@gmail.com
- 🌐 Website: https://chroniquesdesktop.github.io

## License

GNU General Public License - See LICENSE file for details

## Changelog

### v2.0 (Current)
- ✨ Multi-provider AI Assistant (Anthropic/OpenAI-compatible/Ollama)
- ✨ Inline + advanced word cloud workflow
- ✨ Enhanced Help menu (Contents/Q&A/Feedback/About)
- ✨ Arch Linux packaging routine with PKGBUILD
- 📈 Cross-platform support (Windows, Linux, macOS)
- 📚 Expanded in-app documentation

### v1.0 (Initial Release)
- Rich text journal editor
- Image and link support
- PDF export
- Spell checking
- Statistics dashboard
- Windows support

_Last updated: 2026-05-19 02:01 UTC_
