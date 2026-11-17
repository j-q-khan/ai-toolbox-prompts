# Claude build prompt: Power Automate Desktop Tutorial: Automate Clicks and Typing on Windows

Paste this into Microsoft Copilot (Copilot Chat) or into Claude, with made-up examples only. Follow your employer's rules on what you may install, automate and paste, and never describe real customers, staff or real company files: use a made-up test file in a test folder. It turns your own idea for a desktop flow into a list of Power Automate for desktop actions and settings to build one by one, written from Microsoft Learn's desktop flow pages, checked 2026-11-17.

Goal: plan one attended desktop flow in Power Automate for desktop that works only on test files in a test folder, so I can build it action by action and run it while I watch.
Steps, in order:
1. Restate my task in one sentence: which test file goes in, what happens to it, and which new file comes out.
2. List the ready-made actions in order, each with its group in the Actions pane (for example File, Folders or Excel) and every setting I need to change, using Microsoft's names for the boxes.
3. Prefer ready-made actions over the recorder. Use the recorder only for an app with no ready-made action, say which steps would need it, and remind me that loops can't be recorded.
4. Never write over the original file: save every result under a new name in the test folder.
5. If a step takes in a comma-separated file, set its columns separator to a comma rather than System default.
6. Say which variable each action produces and where a later action uses it.
7. Before the first run, remind me where to stop the flow (Stop beside Run in the designer's toolbar, Stop on the flow's line in the main window, and, for flows started from the main window, Stop on the notification or monitoring window that Settings, Flow run control, is set to show) and to set my own stop shortcut in Settings, under Flow run control.
8. End with one check I can do by hand to confirm the result.
If you're not sure of an action's or a setting's exact name, write [CHECK: name in Power Automate for desktop].
My task: (for example: copy a made-up price list from a test file into a new Excel workbook and save it under a new name)
