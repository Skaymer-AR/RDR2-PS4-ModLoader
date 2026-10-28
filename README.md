# RDR2-PS4-ModLoader

Open-source experimental modding framework for **Red Dead Redemption 2 on PlayStation 4**, targeting **CUSA08519 / update 1.29** with GoldHEN.

> Research-stage project. No working PS4 loader or PC-mod compatibility is claimed yet.

## Goals
- Explore reversible file replacement through GoldHEN AFR, where compatible.
- Research a native PRX extension for runtime hooks and diagnostics.
- Build a version-aware manifest validator and mod catalog.
- Keep original game assets, executables, keys, and copyrighted resources out of this repository.

## First milestone
1. Confirm game title ID and update on console.
2. Inspect permitted file-access logs and document target resource formats.
3. Test a harmless, reversible file redirect; record pass/fail and restore procedure.
4. Only then begin PRX proof-of-concept work.

## Status
**v0.1.0-alpha — research scaffold only.** No executable PS4 payload is included.

## Layout
- `profiles/`: title and version metadata.
- `docs/`: architecture, test plan, research log.
- `tools/`: local validation utilities.
- `mods/`: examples without game assets.

Contributions via issues and pull requests are welcome. Do not upload Rockstar game files or third-party mods without redistribution permission.
