Full copy-paste prompt for the Figma agent. Paste this into the Figma agent's prompt box, not into Figma Make, Claude or Claude Code: in a test copy of a design file, connect your library (the + button in the prompt box, then Libraries), select one frame built from your library's components, press Cmd + Enter on a Mac or Ctrl + Enter on Windows (or click Agents), paste it all, swap the words in square brackets, and send it. It works only on the frame you select and uses no other files. It asks you two questions first, then changes colours only and lists what it found. It needs a Full seat with edit access, or a file in your own drafts. It uses some of the AI credits on your plan (a font change was about 30+ credits on Figma's credits page, checked 2026-11-19). Written from Figma's help pages, checked 2026-11-19, not run. Check every change before you keep it; Undo in the chat reverses the most recent change.

Goal: on the frame I've selected, swap colours typed in by hand for the matching colour variables from my connected library, list any layer that isn't an instance of a library component, and change nothing else.
Steps, in order:
1. Before you change anything, check that a library is connected to this chat. If none is, stop and ask me to connect one.
2. Ask me two things and wait for my answers: which variable collection or group holds the colours to use (for example [color/brand]), and, if those variables have modes, which mode this frame should use (for example [Light]).
3. Find every fill and stroke on the selected frame that uses a colour typed in by hand instead of a variable or a style.
4. For each one, apply the colour variable from that group whose value matches exactly. If nothing matches exactly, leave it as it is and add it to a list with its colour value and layer name.
5. List every layer in the frame that isn't an instance of a component from the connected library, with its layer name.
6. Change nothing else: no layout, text, fonts, spacing, sizes, layer names, components or other frames.
7. When you're done, tell me how many colours you swapped, list the ones you left and the layers from step 5, and remind me to check each change and that Undo in the chat reverses the most recent change.
Rules: work only on the selected frame. Don't use other files, connectors or web search. Never ask me for a password, a payment detail or any personal data. If anything is unclear, ask me first.
Reminder for me: this uses some of the AI credits on my plan, and it's a test copy. Check every change before I keep it.
