# set-key-mac.sh: keep your Claude API key on a Mac (zsh, the default shell); type the lines one at a time, don't run this file
# 1. Open the settings file Terminal loads every time it starts (this creates it if it's missing, and opens it in TextEdit):
touch ~/.zshrc && open -e ~/.zshrc
# 2. In TextEdit, add this line at the bottom, without the leading "# ", with your own key right after the = sign,
#    no spaces and no quotes (the key below is a fake), as in Anthropic's own zsh line.
#    Then press Command-S to save and quit TextEdit. Don't type this line in Terminal, so the key stays out of its history.
# export ANTHROPIC_API_KEY=sk-ant-EXAMPLE-not-a-real-key
# 3. Load the change into this window:
source ~/.zshrc
# 4. Check it: this prints the key's length, never the key (0 means it isn't set):
echo ${#ANTHROPIC_API_KEY}
# The file is hidden because its name starts with a dot. To find it in Finder: press Shift-Command-G and type ~/.zshrc
