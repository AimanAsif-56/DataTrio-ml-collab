# Contributing Guide

## Branches

- `main` - production-ready code
- `staging` - release testing
- `dev` - development integration
- `feat/<name>` - feature work
- `data/<name>` - data-related work
- `exp/<member>-<idea>` - experiments
- `fix/<name>` - bug fixes

## Workflow

1. Create a short-lived branch from `dev`.
2. Make changes on your branch.
3. Commit your changes.
4. Push your branch to GitHub.
5. Open a Pull Request into `dev`.
6. Get a teammate review.
7. Merge only after required checks pass.

## Pull Request Rules

- Do not directly push to `dev`, `staging`, or `main`.
- Every PR should have a clear description.
- At least one teammate should review the PR.
- CI checks must pass before merging.

## Commit Messages

Use clear commit messages, for example:

- `feat: add data preprocessing`
- `fix: correct training pipeline`
- `data: add dataset configuration`
- `test: add preprocessing tests`
- `docs: update contributing guide`

## Merge Strategy

The team will use **squash merging** for Pull Requests into `dev`.

## Code Quality

Before pushing changes, run the project's formatting, linting, and tests where applicable.