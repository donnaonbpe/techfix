# TechFix

TechFix is a Python program designed to customize and schedule alerts for reminders, appointments, or system events on Windows. It provides a simple interface to create, manage, and trigger alerts based on the scheduled time.

## Features

- Schedule alerts with a specific name, time, and message.
- Alerts trigger a sound and display a message at the scheduled time.
- Manage alerts by adding or removing them from the schedule.
- Runs continuously in the background to check for upcoming alerts.

## Requirements

- Python 3.x
- Windows operating system
- `winsound` module (included in the Python standard library for Windows)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/techfix.git
    ```

2. Navigate to the project directory:
    ```bash
    cd techfix
    ```

3. Make sure you have Python installed on your system. You can verify this by running:
    ```bash
    python --version
    ```

## Usage

1. Open the `techfix.py` file and add your alerts in the `if __name__ == "__main__":` block, specifying the `name`, `alert_time`, and `message`.

2. Run the program:
    ```bash
    python techfix.py
    ```

3. The program will run in the background and trigger alerts based on the schedule.

4. To stop the program, use `Ctrl+C` in the terminal.

## Example

```python
# Example: Adding an alert for 2 minutes from now
techfix.add_alert(
    name="Test Alert",
    alert_time=datetime.datetime.now() + datetime.timedelta(minutes=2),
    message="This is a test alert"
)
```

This example schedules an alert to trigger two minutes from the current time.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.