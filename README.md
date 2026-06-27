# Scenario Engine

## Overview

Scenario Engine is a terminal-based workflow application that allows users to create, save, execute, and manage custom scenarios.

Each scenario contains multiple steps that can be replayed whenever needed.

---

## Features

- Create Unlimited Scenarios
- Add Unlimited Steps
- Execute Saved Scenarios
- View Available Scenarios
- Delete Scenarios
- Automatic JSON Storage
- Simple Terminal Interface

---

## Project Structure

```
scenario-engine/

├── scenario_engine.py
├── app.py
├── README.md
└── .gitignore
```

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python app.py
```

---

## Example

### Create

```
Scenario Name

Morning Routine
```

Steps

```
Open VS Code

Open Chrome

Open Terminal

done
```

---

### Execute

```
Morning Routine
```

Output

```
Executing...

[1] Open VS Code

[2] Open Chrome

[3] Open Terminal

Scenario Completed.
```

---

## Generated File

```
scenarios.json
```

Example

```json
{
    "Morning Routine": [
        "Open VS Code",
        "Open Chrome",
        "Open Terminal"
    ]
}
```

---

## Future Improvements

- Real Command Execution
- Delay Between Steps
- Conditional Steps
- Loop Support
- Nested Scenarios
- Import / Export Scenarios
- Logging
- Undo Execution

---

## License

MIT License