# Figma agent and your design system: checklist (facts checked 2026-11-19, from Figma's own help pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What you need
- [ ] Figma Design in the desktop app or a web browser. The agent isn't on mobile.
- [ ] To have the agent edit a shared file: a Full seat with edit access. View, Dev and Collab seats (or view-only access) can chat but not edit. Anyone can have it edit their own drafts.
- [ ] A published library for the agent to use. Publishing a library needs a Professional, Education, Organization, Government or Enterprise plan.
- [ ] AI credits. Agent examples: change fonts about 30+, summarize the canvas about 100+, a five-screen checkout flow about 300+ (rates as of 19 November 2026): https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work
- [ ] Your team's rules: ask your admin how the Content training setting is set before you use work files.

## Get your library ready (Figma's tips)
- [ ] Give layers and components real names (Card/Product/Default, not Frame 42 copy). Slash names make groups.
- [ ] Use variables for colours, spacing and type, with names that say how they're used (color/surface/primary, not blue-500).
- [ ] Set component properties and variants (size, type, state).
- [ ] Use auto layout so components resize the way you expect.
- [ ] Fill in each component, style and variable description: what it's for and when to use it.
- [ ] Optional: an Examples page (or names ending in _example) and guidelines files for your conventions.
- [ ] Publish the library, and publish again after changes, so the agent works with the latest.

## Open the agent and connect the library
- [ ] Open a test copy of the design file. Select a layer, then click Agents, or press Cmd + Enter (Mac) or Ctrl + Enter (Windows).
- [ ] Or click Agents in the left navigation bar for a sidebar with all your chats. New chat starts a fresh one.
- [ ] In the prompt box, click the + button, then Libraries, and pick your library.
- [ ] Type @ to name a specific component, variable or style in your prompt.

## Run the colour swap (agent-prompts.txt, prompt 1)
- [ ] Select one frame built from your library's components.
- [ ] Paste prompt 1, swap the words in square brackets, and send it. Answer its two questions.
- [ ] To stop a running prompt: click Stop in the chat box.

## Check it worked
- [ ] Click through the frame: each swapped colour should now show a variable, and nothing else should have moved.
- [ ] Look at the list of colours it left and the layers that aren't library instances.
- [ ] Before you undo, duplicate the agent's version if you want to compare the two side by side.
- [ ] Not right? Click Undo in the chat. It reverses the most recent change.

## Design system chores to try next
- [ ] Draft descriptions (prompt 2), and check each before you OK it.
- [ ] Rename default layer names (prompt 3), and check each change.
- [ ] Ask for several directions (prompt 4): words like distinct or completely different help.
- [ ] Update main components and variants, or switch a screen to another mode, on a library you can edit.

## Figma Make: Make kits (paid plans)
- [ ] Plans: Professional, Education (not K-12), Organization, Government, Enterprise.
- [ ] Create: open a new Make file, click Settings (top-right corner), then Create a kit. Add npm packages and/or library styles, write guidelines, test it, then click Publish kit (not from your drafts).
- [ ] Use: in a Make file, click Add context in the prompt box, then Select a Make kit.
- [ ] Your variables arrive as one simplified CSS file with raw values, so write any rules about them in the kit's guidelines.

## Not there yet (Figma's coming soon list)
- [ ] Vector editing and Draw tools, creating icons, slots (open areas inside a component for your own layers), prototyping and interactions.
- [ ] Saving files out: the agent gives download links instead. Diagrams and charts: Figma points to FigJam.

## Afterwards
- [ ] Delete the test copy if you don't need it.
- [ ] Start a new chat for each new task: a long chat makes each prompt cost more.

Sources: help.figma.com/hc/en-us/articles/37998629035799 ; /38978644498199 ; /43861597594007 ; /43927294474263 ; /41159677390999 ; /41159787685143 ; /39241689698839 ; /360041051154 ; /33459875669015 ; /43707097479575 ; /17725942479127
