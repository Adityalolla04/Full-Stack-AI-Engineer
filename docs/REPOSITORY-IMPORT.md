# Earlier work consolidated into one repository

Imported on 2026-11-07 from sibling folders in the local GitHub directory.

**Placement update:** the table below describes the initial import layout. Existing notebooks/scripts have since moved into concept folders. The [placement report](MATERIAL-PLACEMENT.md) lists current locations. The manifest's `sha256` records current bytes; `original_sha256` preserves the original import hash. Six notebooks contain only documented data-path changes.

| Original repository | New location | Imported files | Observed evidence |
|---|---|---:|---|
| PYTHON | `Python/Previous-Practice/` | 9 | Python Practice and NumPy/Pandas notebooks; datasets |
| ML-DL-CV | `ML-DL-CV/Previous-Practice/` | 57 | ML, DL, CV notebooks, code, and documentation |
| LLM-Mastery | `LLM/Previous-Practice/` | 13 | Roadmap, NLP notes, three Python examples; eight empty module READMEs |
| System-Design-Engineering | `System-Design-Engineer/Previous-Practice/` | 1 | License and empty topic directories; no implemented lessons observed |

Source remotes read from local Git configuration:

- https://github.com/Adityalolla04/PYTHON
- https://github.com/Adityalolla04/ML-DL-CV
- https://github.com/Adityalolla04/LLM-Mastery
- https://github.com/Adityalolla04/System-Design-Engineering

These remote URLs identify provenance; remote contents were not compared with local files. Local uncommitted content, if any, is included in the snapshot.

## What moving means here

All future learning can happen in Full-Stack-AI-Engineer. The original sibling repositories were left intact as backups. Their `.git` folders were excluded, so the imported files are ordinary files managed by this repository. Commit history remains in the original repositories; it was not merged into this one. Other unrelated projects were not imported.

The import excluded `.DS_Store`, `.git`, virtual environments, dependency folders, bytecode caches, and notebook checkpoints. Every imported file was checked against its source with SHA-256. The manifest lists paths, sizes, and hashes. Original source content, including any inaccurate notes or incomplete examples, was preserved without claiming correctness.

Empty source directories were recreated locally. Git does not track empty directories, so add actual lesson files there when useful; the active learning structure is documented separately.

## How to work from here

1. Open this repository as your main workspace.
2. Use `<Subject>/<concept>/practice/existing/` for organized prior work. Shared notebooks are linked from related concepts rather than duplicated. `Previous-Practice/` now retains historical guides and placeholders.
3. Put your solutions under `<Subject>/<numbered-concept>/practice/`. Add personal notes beside that concept's README, and build the final application under `Capstone-Project/`.
4. Review imported notebooks and dataset provenance before publishing. The patient-named sample files have been preserved, but their privacy/licensing status was not assessed.
5. Review the working tree, then commit and push through your usual workflow when ready.
6. Once the consolidated copy is backed up remotely, you may archive old GitHub repositories and update their READMEs to point here. That has not been done automatically.

If retaining all old commit histories inside this repository becomes a requirement, use a separately prepared history-preserving subtree migration. Do not simply copy old `.git` directories into the new tree.

The helper `python scripts/import_prior_work.py` now verifies the organized manifest when a placement record exists. It does not recopy files or recreate the historical layout. A hash mismatch is reported for review rather than overwritten. It is not an ongoing two-way sync.

Reference: [Git's explanation of embedded repositories and submodules](https://git-scm.com/docs/gitsubmodules). Submodules were not used because the requested outcome is one repository containing the files.
