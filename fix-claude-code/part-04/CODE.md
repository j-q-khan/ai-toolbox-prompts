# Full code: Claude Code Command Not Found After Install: Fix It on Mac and Windows

A command not found checklist written for this video from Anthropic's Claude Code docs (checked 2026-11-15, Claude Code 2.1.325). Messages and commands are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-command-not-found-checklist.md
```
# Claude Code "command not found" checklist: Mac and Windows (from Anthropic's docs, checked 2026-11-15)

## Which message?
- macOS:          zsh: command not found: claude
- Linux:          bash: claude: command not found
- Windows CMD:    'claude' is not recognized as an internal or external command
- PowerShell:     claude : The term 'claude' is not recognized as the name of a cmdlet
All four usually mean the install folder isn't in your PATH (the list of folders your terminal searches).
The installer puts claude in ~/.local/bin (Mac, Linux) or C:\Users\you\.local\bin (Windows).
Its output may say under "Setup notes:": Native installation exists but ~/.local/bin is not in your PATH.

## 1. Is Claude Code there?
- [ ] Mac or Linux, in the Terminal:      ls -la ~/.local/bin/claude
      A listing for the file: it's there. "No such file or directory": no native install.
- [ ] Windows, in PowerShell:             Test-Path "$env:USERPROFILE\.local\bin\claude.exe"
      True: it's there. False: no native install.
- [ ] Installed another way (npm, Homebrew, WinGet)? List every claude your terminal finds:
      Mac or Linux:  which -a claude
      Windows:       where.exe claude
- [ ] Not installed at all: follow Anthropic's install page, code.claude.com/docs/en/setup
- [ ] Windows, 'claude' is not recognized right after an update: look for a backup whose name starts claude.exe.old. followed by numbers, in C:\Users\you\.local\bin.
      This renames the newest backup back to claude.exe (it changes nothing else):
      Get-ChildItem "$env:USERPROFILE\.local\bin\claude.exe.old.*" | Sort-Object Name | Select-Object -Last 1 | Rename-Item -NewName claude.exe

## 2. Is the folder already in your PATH?
- [ ] Mac or Linux:  echo $PATH | tr ':' '\n' | grep -Fx "$HOME/.local/bin"
      Prints /Users/you/.local/bin (or /home/you/.local/bin): it's there, skip to step 5.
- [ ] Windows PowerShell:  $env:PATH -split ';' | Select-String '\.local\\bin'
      Prints C:\Users\you\.local\bin: it's there, skip to step 5.

## 3. Add the folder (once; it's permanent)
Not sure which shell your Mac uses? Type:  echo $0
- [ ] Zsh (the Mac default), in the Terminal. Line 1 adds one line to the end of ~/.zshrc and prints nothing when it works; line 2 applies it to this window:
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
      source ~/.zshrc
- [ ] Bash on Linux:
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc
- [ ] Bash on a Mac (Terminal starts Bash as a login shell, which ignores ~/.bashrc). If you already have ~/.bash_login or ~/.profile and no ~/.bash_profile, use that file instead:
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
      source ~/.bash_profile
- [ ] Windows PowerShell. Line 1 copies your User PATH; line 2 saves it with the folder added to the end (your account only). Then restart your terminal:
      $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
      [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
- [ ] Windows Command Prompt: open System Settings, go to Environment Variables, and add %USERPROFILE%\.local\bin to your User PATH variable. Restart your terminal.

## 4. If something blocks it
- [ ] "zsh: permission denied: /Users/you/.zshrc" (or "bash: /home/you/.bashrc: Permission denied"): nothing was saved. See who owns the file (the third field is the owner):
      ls -l ~/.zshrc
      Owner is another user, such as root. This makes you the owner of that one file and asks for your password (administrator rights):
      sudo chown $(whoami) ~/.zshrc
      Owner is you, but the file is read-only. This lets you change that one file:
      chmod u+w ~/.zshrc
      Then run the two lines from step 3 again.
- [ ] Windows, npm install, "running scripts is disabled on this system" (it names npm.ps1 or claude.ps1):
      Type claude.cmd instead (npm.cmd for npm); the policy doesn't cover them.
      Or allow locally created scripts for your user. This changes PowerShell's execution policy for your account only:
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
      Or use the PowerShell installer instead of npm (below).
- [ ] The install command itself failed: you used the command for a different window.
      'irm' is not recognized                              you're in CMD: open PowerShell and run the PowerShell installer, or use the CMD installer
      The token '&&' is not a valid statement separator    you're in PowerShell: use the PowerShell installer
      A parameter cannot be found that matches parameter name 'fsSL'   you ran the Mac/Linux installer in PowerShell: use the PowerShell installer
      'bash' is not recognized as the name of a cmdlet     you ran the Mac/Linux installer on Windows: use the PowerShell installer
      PowerShell installer:  irm https://claude.ai/install.ps1 | iex
      CMD installer:         curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
- [ ] Windows: typing claude opens the Claude desktop app. An older Claude Desktop registers a Claude.exe in WindowsApps that comes first. Update Claude Desktop.
- [ ] "Claude Code on Windows requires either Git for Windows (for bash) or PowerShell": that's a different problem (the next video in this series).

## 5. Check it worked
- [ ] Shut every Terminal or PowerShell window and open a new one. A window that was already open keeps its old PATH.
- [ ] Typing commands inside an editor (Visual Studio Code, for example)? Quit the whole editor and open it again: its terminal takes its PATH from the editor.
- [ ] Type:  claude --version
      Example output:  2.1.325 (Claude Code)
- [ ] Still not found? Mac or Linux: grep -n '.local/bin' ~/.zshrc (use your shell's file) shows whether the line was saved; echo $0 shows which shell you're in.
      Windows: [Environment]::GetEnvironmentVariable('PATH', 'User') and look for .local\bin in what it prints.

## Still stuck?
- [ ] Search or open an issue with your operating system, the install command you ran and the full error: github.com/anthropics/claude-code/issues
- [ ] Once claude --version works but something else is wrong: claude doctor. Once a session starts: /feedback.

Docs: code.claude.com/docs/en/troubleshoot-install (Verify your PATH; command not found; permission denied; Wrong install command on Windows; running scripts is disabled; Claude Desktop overrides the claude command)
```
