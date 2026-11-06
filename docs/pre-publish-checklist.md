# Pre-publish checklist
- [ ] `gitleaks detect` on full history
- [ ] Search history for `C:\Users` and large files
- [ ] Commit email is the one you want public (noreply?)
- [ ] README: demo, run command, comparison, limitations
- [ ] LICENSE name filled in; CI green; description and topics set
- [ ] Fresh clone: `uv sync && uv run pytest` works
- [ ] `gh repo edit --visibility public --accept-visibility-change-consequences`
