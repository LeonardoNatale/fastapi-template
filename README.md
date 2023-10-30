## Temporary

### Running the app

`poetry run dev`

### Pre-commit

To run pre-commit before commit and push:
`pre-commit install --hook-type pre-commit --hook-type pre-push`

or just before push:
`pre-commit install --hook-type pre-push`

otherwise:
`pre-commit run --all-files`
