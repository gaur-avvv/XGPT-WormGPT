# Skills

Every `.txt` file in the repository can be installed anywhere:

- pasted into an agent session
- loaded by a CLI prompt loader
- dropped into any harness that accepts plain prompt text
- installed locally with the provided scripts

No harness-specific format is required.

## Install one skill

If you only want one skill file, copy it manually or use the helper for a single file:

```sh
sh scripts/install-skill.sh <any-.txt-file-in-the-repo>
```

This works for any `.txt` file in the repository.

## Install all skills

Install every `.txt` file in the repository as a skill:

```sh
sh scripts/install-all-skills.sh
```

Default target: `.skills/`

To install into a custom directory:

```sh
sh scripts/install-all-skills.sh /path/to/your/skills
```

## Local install from the skills folder

If you are already inside the skills folder you can run:

```sh
cd skills
sh install.sh
```

That installs every `.txt` file in that folder into `.skills/` by default.

To install into a custom directory:

```sh
sh install.sh /path/to/your/skills
```

## Where installed skills go

By default, skills are installed into a local directory called `.skills/`.

If your CLI or harness loads prompts from a folder, point it at that folder.

Examples:
- `./.skills/`
- `~/.mycli/skills/`
- any directory your tool already reads

## How any agent can use a skill

1. Install the skill to a directory
2. Load the `.txt` file into the agent
3. Use the skill contents as the system prompt, custom instruction, or prompt attachment

If your agent accepts a prompt path, point it at the installed file. If it only accepts pasted text, paste the file contents.

## How any CLI can use a skill

If your CLI can read a file, it can use the skill directly.

Example:

```sh
cat .skills/<skill-name>.txt
```

You can also wrap that in your own command:

```sh
sh -c 'cat .skills/<skill-name>.txt'
```

## Harness-agnostic install

Because skills are plain text files, they work with:
- chat agents
- coding agents
- CLI prompt helpers
- workflow harnesses
- custom prompt pipelines

No special plugin is needed.

## Add your own skill

1. Create a `.txt` file in `skills/`
2. Name it clearly
3. Add an `install.sh` file alongside it if you want one-click install for that skill

If you add `install.sh` in the same folder as the `.txt` file, it will copy that skill’s `.txt` file when run from inside `skills/`.

## List available skills

Show every `.txt` file in the repository as a skill:

```sh
sh scripts/list-skills.sh
```

Or list the files directly with your own tool:

```sh
find . -name '*.txt' -type f
```

## Manual install

If you do not want to use the scripts, install any `.txt` file manually:

```sh
cp <path-to-skill>.txt .skills/
```

That works in any environment.

## Customization

You can change:
- the default target directory
- the source folder
- the file extensions your tool expects
- the helper scripts to match your own CLI layout

The important part is that skills stay plain text so they can be installed anywhere.
