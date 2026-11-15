# Full code: Claude Code on Windows Requires Git Bash? The Error, Fixed (PowerShell Works Too)

A Windows shell error checklist written for this video from Anthropic's Claude Code docs (checked 2026-11-15, Claude Code 2.1.325). Messages, folders and settings lines are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-windows-git-bash-checklist.md
```
# Claude Code "requires Git Bash" on Windows: checklist (from Anthropic's docs, checked 2026-11-15)

## Which message?
- Today:  Claude Code on Windows requires either Git for Windows (for bash) or PowerShell
  Git for Windows is optional. Claude Code uses PowerShell when Git Bash is absent,
  so this message means it found NEITHER shell.
- Older:  Error: Claude Code on Windows requires git-bash (https://git-scm.com/downloads/win)
  This wording comes from an older version of Claude Code.
  Install Git for Windows (fix 2) or use fix 3.
- Older, with the setting pointing at a file that isn't there:
  Claude Code was unable to find CLAUDE_CODE_GIT_BASH_PATH path
  Versions before 2.1.219 stopped at startup with this. Check the path letter for letter (fix 3).
- "claude : The term 'claude' is not recognized as the name of a cmdlet": a different problem
  (command not found, the previous video in this series).
- "Claude Code does not support 32-bit Windows": open "Windows PowerShell" from the Start menu,
  not "Windows PowerShell (x86)". Check with:  [Environment]::Is64BitOperatingSystem
  True: your Windows is 64-bit, so use the other entry. False: 32-bit Windows isn't supported.
- The Claude desktop app asks for Git: versions before 1.49585.0 asked for Git before starting any
  local session. If you aren't using worktrees, update the app.

## Fix 1: PowerShell on your path (nothing to download)
- [ ] PowerShell's default folder:  C:\Windows\System32\WindowsPowerShell\v1.0\
- [ ] Add it to your path: open System Settings, go to Environment Variables, select Path under
      your account's (User) variables, choose Edit, then New, paste the folder above, then OK
      in each window.
      Then open a new terminal.
- [ ] Or install PowerShell 7 (which provides pwsh) from Microsoft: https://aka.ms/powershell

## Fix 2: install Git for Windows (adds Git Bash and Claude Code's Bash tool)
- [ ] Download: https://git-scm.com/downloads/win
- [ ] During setup, select "Add to PATH" (Anthropic's wording). Keeping the suggested install
      folder puts Git in C:\Program Files\Git, the first place Claude Code looks.
- [ ] Shut the terminal and open a new one. A window that was already open keeps its old path.
- Without the setting below, Claude Code looks for bash.exe in this order:
  1. C:\Program Files\Git  and  C:\Program Files (x86)\Git
  2. The git on your path, using bin\bash.exe from that Git.
  It skips a git inside the folder you started Claude Code from, or under node_modules or a
  virtual-environment folder such as .venv or env. If your Git is there, use fix 3.

## Fix 3: point Claude Code at your Git's bash.exe
- [ ] In PowerShell:  where.exe git
      Example output:  D:\Tools\Git\cmd\git.exe
- [ ] Keep the Git folder, swap the end:  D:\Tools\Git\bin\bash.exe   (bin\bash.exe, not cmd\git.exe)
- [ ] The settings file:  C:\Users\you\.claude\settings.json
      (In Anthropic's docs: ~/.claude/settings.json; on Windows, ~/.claude means %USERPROFILE%\.claude.)
- [ ] No .claude folder yet? In PowerShell, this makes the empty folder and changes nothing else:
      mkdir "$env:USERPROFILE\.claude"
- [ ] No settings.json yet: copy these lines into Notepad, put YOUR bash.exe path in the quotes,
      keep every backslash doubled:
      {
        "env": {
          "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
        }
      }
      File, then Save As. Go to your .claude folder. Save as type: All files (otherwise Notepad adds .txt).
      File name: settings.json. Save.
- [ ] Already have a settings.json? Don't replace it. Open it in Notepad.
      It already has an "env" block? Add this line as the first line inside it, comma included (no comma if the block is empty):
          "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe",
      No "env" block? Paste these lines right after the file's first { line, comma included:
        "env": {
          "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
        },
      The file is only {} with nothing inside? Replace it with the full lines above instead.
      Settings files are strict JSON: no // comments, no trailing comma after the last entry.
      A broken file shows a Settings Error the next time Claude Code starts.

## The common mistake
- [ ] The file name must be bash.exe, sh.exe, bash or sh.
      git-bash.exe (the launcher that opens the Git Bash window) is IGNORED: Claude Code searches
      as if the setting weren't there. A path with no file there is ignored the same way.
- [ ] Check every folder name in the path against File Explorer, letter for letter.
- [ ] Set CLAUDE_CODE_GIT_BASH_PATH as a Windows environment variable before (some videos teach that)?
      Check that one for git-bash.exe too: System Settings, Environment Variables.

## Check it worked
- [ ] Shut every PowerShell window, open a new one, type:  claude
      Claude Code should start without the shell error.
- [ ] Set the path and nothing changed? Start it with:  claude --debug
      Claude Code logs a warning when the file name is wrong or the file doesn't exist.

## Still stuck?
- [ ] Work computer: AppLocker, Group Policy software restriction policies or EDR software may block
      claude.exe and the programs it starts (cmd.exe, bash.exe). Ask your IT team to allowlist them.
- [ ] Search or open an issue with your Windows version, the install command you ran and the full error:
      github.com/anthropics/claude-code/issues

Docs: code.claude.com/docs/en/troubleshoot-install (Claude Code on Windows requires either Git for Windows (for bash) or PowerShell; Claude Code does not support 32-bit Windows), code.claude.com/docs/en/settings, code.claude.com/docs/en/desktop (Git and Git LFS errors), Claude Code changelog 2.1.120 and 2.1.219.
```
