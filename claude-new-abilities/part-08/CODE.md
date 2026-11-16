# Full code: Claude Computer Use: Let Claude Control Your Computer, Safely

A checklist, a settings file and commands written for this video from Anthropic's Claude Code docs, agent-desktop's files at tag v1.3.1 (read as text), its release page and Microsoft's Windows Sandbox docs, checked 2026-11-15. Not run by us: read every line, and use it only inside Windows Sandbox or a virtual machine.

### 1. computer-use-checklist.md
```
# Claude computer use, safely: checklist (checked 2026-11-15)

## The rule for both routes
- A virtual machine or a spare computer, never your everyday desktop.
- Sign in to nothing there but Claude: no banking, email or work accounts,
  no password manager. Use an email sign-in for Claude, not Google.
- A web page or document on screen can carry instructions aimed at
  Claude (prompt injection). Watch what it does.
- Keep Claude asking before it acts: manual mode in Claude Code;
  "Needs approval" on each tool in Claude's desktop app.
- Stop: Esc. Switch it off when you're done (below).

## Route 1: built into Claude Code
- Research preview. Pro, Max or Ultra plan (not Team or Enterprise),
  signed in through claude.ai. Not with -p.
- Terminal (Mac only): inside Claude Code, /mcp > computer-use > Enable.
  It sticks per folder you start Claude in.
- Desktop app (Mac, macOS 14 or later; Windows): Settings > Capabilities
  (or This computer > System) > Computer use > Enable computer use.
- Mac: the first use asks for Accessibility and Screen Recording.
  Grant both in System Settings, then Try again. Still asking? /exit and
  start Claude Code again.
- Each app asks: Allow for this session / Deny. Terminals, Finder (File
  Explorer on Windows) and System Settings carry an extra warning: think
  before allowing them.
  Browsers are view only; terminals are click only.
- Desktop app: add sensitive apps to Denied apps in the same section.
- Stop: Esc (from any app, Mac terminal) or Ctrl+C in the terminal;
  in the desktop app, the stop button.
- "Computer use is in use by another Claude session"? /exit the other one.
- Off: /mcp > computer-use > Disable, or turn off Enable computer use.

## Route 2: agent-desktop inside Windows Sandbox (Windows terminal)
### Before you install
- Repo: github.com/vercel-labs/agent-desktop. Vercel Labs, experimental.
- Licence: Apache-2.0. Latest release: 1.3.1, 2026-11-13.
- Real use: about 24,000 stars, about 1,800 forks; issues 87 open,
  51 closed; 7 closed sampled: a core developer closed 6, 3 with a fix.
- Reaches: every app's accessibility tree, screenshots, the clipboard
  (get, set, clear), keyboard, mouse, apps and windows, notifications.
  It can launch any program, so its docs say treat it like a shell for
  the signed-in user. Keep Claude asking before every tool.
- Telemetry: none found in its code at 1.3.1. Costs: free.
- The Windows program is unsigned: Windows security may warn or block it.
### Needs
- Windows Pro, Enterprise or Education (Windows Sandbox is not on Home;
  Hyper-V is on Pro and Enterprise). Home: use a spare computer.
- Virtualization on in the BIOS.
- Turn Windows features on or off > tick Windows Sandbox > OK > restart.
  Can't tick it? Check virtualization in the BIOS.
### On your own computer (nothing runs here)
1. Make the folder C:\Users\you\claude-sandbox.
2. From github.com/vercel-labs/agent-desktop/releases/tag/v1.3.1,
   save agent-desktop-v1.3.1-x86_64-pc-windows-msvc.tar.gz into it, not
   Downloads (or move it there afterwards).
   (ARM computer: the aarch64 file and its code, section 3).
   Your browser may warn about the download (the program inside is
   unsigned). Keep the file from the browser's downloads list (Edge can
   ask you to confirm twice): it is only hashed here, never run. Never
   switch off SmartScreen or any other protection on this computer.
3. Check its fingerprint (section 3). PowerShell prints True when it
   matches. False or "cannot find path"? Stop.
4. Save the settings file (section 2) as claude-sandbox.wsb in the same
   folder: Notepad > Save as > Save as type: All files.
   Older than Windows 11 23H2? %USERPROFILE% doesn't work there: write the
   full path, C:\Users\yourname\claude-sandbox, in HostFolder. The folder
   must exist, or the sandbox won't start.
5. Double-click claude-sandbox.wsb.
### Inside the sandbox (type these: the clipboard is off)
6. Start menu > Windows PowerShell. (Windows 11 24H2's sandbox has no
   Notepad or Terminal.)
7. Install Claude Code (section 4). It shows no progress: wait.
   Then open a new Windows PowerShell window.
8. Unpack agent-desktop and add it to Claude Code (section 4): the $a line
   names the archive, then tar -xzf $a -C $HOME unpacks it.
   Windows security blocks agent-desktop.exe? It's unsigned. Smart App
   Control or antivirus inside the sandbox can stop it; /mcp then shows
   agent-desktop as failed. Stopping here is fine. Changing a setting inside the sandbox changes only the sandbox,
   which is deleted when you shut it; never change it on your own computer.
9. claude --permission-mode manual. The sandbox's browser opens to sign in:
   use an email (not Google). If the browser shows a code, copy it into
   PowerShell (copy and paste work inside the sandbox). An emailed code
   that arrives on your phone or computer has to be typed.
   Say yes to trusting the folder.
10. /mcp: check agent-desktop is connected.
11. Ask: Open File Explorer, make a folder on the desktop called
    claude-test, and tell me when it's done.
12. Approve each agent-desktop tool after checking what it does.
    The folder appears at C:\Users\WDAGUtilityAccount\Desktop\claude-test,
    inside the sandbox.
### Stop and switch off
- Stop: click the sandbox's PowerShell window (File Explorer will be in
  front), then press Esc in Claude Code.
- Off: /exit, then shut the sandbox and choose OK when it asks to delete
  everything. Nothing you installed in it survives.
- Done for good: delete C:\Users\you\claude-sandbox.

## Route 2 on a Mac (not shown in the video)
- agent-desktop's sandbox command makes a macOS virtual machine on an
  Apple Silicon Mac (not Intel), macOS 13 or later, with Xcode Command
  Line Tools. Creating the first VM from a macOS image is experimental.
- Its docs: "Use agent-desktop sandbox for a desktop you trust at the
  same level as your own account." The VM shares your network.
- Steps: agent-browser.dev/desktop/sandboxes/macos (sandbox install macos,
  sandbox create, the one-time guest setup by hand, sandbox start).
  It installs agent-desktop on your Mac to manage the VM; run the MCP
  server only inside the guest.
- From the release archive (agent-desktop-v1.3.1-aarch64-apple-darwin.tar.gz)?
  Check it first in Terminal (section 3b): it prints OK when it matches.
  It holds agent-desktop and agent-desktop-macos-helper: keep them together.
- In the guest, macOS asks for Accessibility for the app that starts
  agent-desktop, and Screen Recording only for screenshots;
  agent-desktop permissions --guide opens the right System Settings pane.

## Runner-up
- AmrDab/clawdcursor: MIT, 2.0.0 (2026-11-11). On-screen Stop button,
  one-time consent. Its README says error reports go on by default from
  2.1: opt out with CLAWD_TELEMETRY=0 or DO_NOT_TRACK=1.
```

### 2. claude-sandbox.wsb (save in C:\Users\you\claude-sandbox, Save as type: All files)
```
<Configuration>
  <ClipboardRedirection>Disable</ClipboardRedirection>
  <AudioInput>Disable</AudioInput>
  <VideoInput>Disable</VideoInput>
  <PrinterRedirection>Disable</PrinterRedirection>
  <MappedFolders>
    <MappedFolder>
      <HostFolder>%USERPROFILE%\claude-sandbox</HostFolder>
      <SandboxFolder>C:\claude-sandbox</SandboxFolder>
      <ReadOnly>true</ReadOnly>
    </MappedFolder>
  </MappedFolders>
</Configuration>
```

### 3. On your own computer: check the archive's fingerprint (Windows PowerShell; it only hashes the file)
```
# x64 (most computers). Prints True when it matches.
$want = "6ee4b1e078f4e78792e79f16e32e4a78b9919464aa3c55629b7e27ed53a08c13"
$f = "$HOME\claude-sandbox\agent-desktop-v1.3.1-x86_64-pc-windows-msvc.tar.gz"
(Get-FileHash $f).Hash -eq $want
# ARM: agent-desktop-v1.3.1-aarch64-pc-windows-msvc.tar.gz, code
# 805f1f61890f9983fceaf38cda94a37a049c379435d65607db5cedd22c8ef97b
# (use the ARM file name in the $a line in section 4 too).
# Codes from the 1.3.1 release page and its checksums.txt (2026-11-15).
```

### 3b. On a Mac: check the archive's fingerprint (Terminal; it only hashes the file)
```
# Apple Silicon. Run it inside the folder you saved the archive to. Prints OK when it matches.
echo "9b7b7cfc74892eab46c2c85d6cb7dc4863bf8dab0a222cfcfb8ae4604c69c86c  agent-desktop-v1.3.1-aarch64-apple-darwin.tar.gz" | shasum -a 256 -c
```

### 4. Inside Windows Sandbox only (Windows PowerShell; type each line)
```
irm https://claude.ai/install.ps1 | iex
# wait for it to finish, then open a new Windows PowerShell window
$a = "C:\claude-sandbox\agent-desktop-v1.3.1-x86_64-pc-windows-msvc.tar.gz"
tar -xzf $a -C $HOME
claude mcp add agent-desktop -- "$HOME\agent-desktop.exe" mcp
claude --permission-mode manual
```

### 5. Inside Claude Code, in the sandbox: check the connection, then type the task
```
/mcp
Open File Explorer, make a folder on the desktop called claude-test, and tell me when it's done.
```

### 6. Built-in computer use, inside Claude Code on a Mac (switch on, then off)
```
/mcp
# pick computer-use, choose Enable; to switch it off later, pick it again and choose Disable
/exit
```
