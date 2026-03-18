# Shiny Clippy

Shiny Clippy started out as a simple HTML-based, but hacky, solution designed to allow copying text from an Arch Linux virtual machine running KDE Plasma 6 on VMware to a Windows 11 host. Unfortunately, this doesn't work anymore...

It can now mostly be used to redact words from text or logs before pasting them into an LLM, for example.

## Features

- Simple and lightweight HTML page.
- Preserves text formatting when copying from VM to host.
- **Redact Text**: enter one‑per‑line patterns to remove from the main clipboard text and click _Redact Text_ to strip all occurrences (visual `sed 's/pattern/█████/g'`).

## How to Use

- **Copy and Paste Text**
  - Copy the desired text from any application within your VM.
  - Paste the text into the main text box on the Shiny Clippy page.

- **Redact Sensitive Text (optional)**
  - Enter patterns to remove, one per line, in the **Redaction Patterns** box.
  - Click **Redact Text**; all occurrences of those patterns are removed from the main text.

- **Copy the Result**
  - Copy the text from the Shiny Clippy text box.
  - Paste the text into any application on your Windows host.
