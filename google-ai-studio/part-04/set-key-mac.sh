# set-key-mac.sh: set your Gemini API key on a Mac (zsh, the default since macOS 10.15); type the lines one at a time, don't run this file
# Put your own key between the quotes. EXAMPLE-NOT-A-REAL-KEY is a fake, so this line alone won't work.
# This window only:
export GEMINI_API_KEY="EXAMPLE-NOT-A-REAL-KEY"
# Check it: this prints the key's length, never the key (0 means it isn't set in this window)
echo ${#GEMINI_API_KEY}
# Keep it for every new window: this creates ~/.zshrc if it's missing and opens it in TextEdit (-e means TextEdit).
# Keep it plain text: if TextEdit shows a formatting bar, choose Format, then Make Plain Text.
# Paste the export line at the bottom, with your key, press Command-S to save, then quit TextEdit.
touch ~/.zshrc && open -e ~/.zshrc
# Or skip TextEdit and add the line from Terminal: type the line below without the leading "# ".
# Use two > signs, because one > would wipe the file.
# echo 'export GEMINI_API_KEY="EXAMPLE-NOT-A-REAL-KEY"' >> ~/.zshrc
# The file is hidden because its name starts with a dot. To find it in Finder: press Shift-Command-G and type ~/.zshrc
# On an older Mac that uses bash, use ~/.bash_profile instead of ~/.zshrc in these lines (Terminal opens bash as a login shell).
# Load it into this window
source ~/.zshrc
