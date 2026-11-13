# OpenCode 2 in a do-it-yourself Docker sandbox (The AI Toolbox, AI Coding Agents Part 6, checked 2026-11-12).
# OpenCode's own official image at one exact version, plus git and a normal user. Test folders only.
FROM ghcr.io/anomalyco/opencode:2.2.7

# git, so OpenCode can see the folder's history. Your undo button is git on your own computer.
RUN apk add --no-cache git

# A normal user, with no sudo and no root password.
RUN addgroup -g 1000 agent && adduser -D -u 1000 -G agent agent

USER agent
WORKDIR /workspace
# The image's own ENTRYPOINT ["opencode"] stays as it is.
