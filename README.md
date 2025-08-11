# Shiny Clippy

Shiny Clippy is a simple HTML-based solution designed to facilitate copying text from an Arch Linux virtual machine running KDE Plasma 6 on VMware to a Windows 11 host. In some setups, copying text directly from the VM to the host is not always possible. Shiny Clippy leverages the Brave browser as an intermediate clipboard to retain text formatting during the copy-paste process. It may also work with other browsers or applications that use a different clipboard manager than KDE.

## Features

- Simple and lightweight HTML page.
- Preserves text formatting when copying from VM to host.
- Easy to use with no additional software installation required.

## How to Use

1. **Open the HTML File**:
   - Launch the Brave browser within your Arch Linux VM.
   - Open the `shiny_clippy.html` file by navigating to it or using the command: `brave shiny_clippy.html`.
   - Optionally, create an alias in your shell configuration file (e.g., `.bashrc`, `.zshrc`) for quicker access.

2. **Copy and Paste Text**:
   - Copy the desired text from any application within your VM.
   - Paste the text into the text box on the Shiny Clippy page.
   - Copy the text from the Shiny Clippy text box.
   - Paste the text into any application on your Windows host.

## Requirements

As far as I know the issue seems to be restricted to Arch Linux with KDE Plasma 6 running in a VMware Workstation Pro virtual machine with a Windows 11 host system.

- Brave browser installed in the Arch Linux VM. See here: https://brave.com/linux/

## Installation

No installation is required. Simply download the `shiny_clippy.html` file and open it in the Brave browser within your VM.
