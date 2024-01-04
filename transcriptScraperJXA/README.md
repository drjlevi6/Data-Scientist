# transcriptScraper.jxa.scpt

JavaScript for Automation ("JXA") script to scrape transcripts from LinkedIn Learning course lectures

## Requirements

* A computer with macOS, capable of running JavaScript for Automation AppleScripts
* The bash shell (must be user's default `$SHELL`)
* Carsten Blüm's `cliclick` Unix executable (`https://github.com/BlueM/cliclick`)
* Apple's `Terminal.app` (must have permission to control your computer: System Preferences ➔ Privacy & Security ➔ Accessibility, as of MacOS Sonoma 14.0)
* My shell script `formatTranscript.bash`(included in this directory)

## Usage

* Download `cliclick` and move it to `/usr/local/bin` (if you put it elsewhere you'll have to create a link to `/usr/local/bin/cliclick`).
* Download `transcriptScraper.jxa.scpt` from this directory; move it to a location in your Scripts directory where you can access it.
* Download `formatTranscript.bash` and move it to `$HOME/bin` (create this directory if necessary).
* Using the Firefox web browser, load a lecture from a LinkedIn Learning course. Click the "Transcript" link below and at the right of the lecture panel, then run transcriptScraper.jxa.scpt with the Script Editor or a third-party application such as Red Sweater Software's FastScripts.

## Maintainer

Jonathan Levi, MD: `https://www.linkedin.com/in/jonathan-levi-md-48253526/`

