# airflow-csharp-python-dag

# Airflow C# Python Integration

This repository demonstrates how to integrate Airflow with Python and C# tasks, running on a Windows system with WSL (Windows Subsystem for Linux). The setup includes executing a C# program using .NET and a Python script, orchestrated via Airflow.

## Repository Structure

```plaintext
├── dags
│   └── run_csharp_python.py       # Airflow DAG defining the task workflow
├── scripts
│   ├── csharp
│   │   ├── csharp.csproj          # C# project file
│   │   ├── hello.cs               # Main C# script
│   │   ├── hello.exe              # Compiled C# executable
│   │   └── Program.cs             # C# program entry point
│   └── python
│       └── hello.py               # Python script to be executed
├── .gitignore                     # Git ignore file
├── README.md                      # Project documentation
```

## Prerequisites

### Windows Setup with WSL

1. **Install WSL**:
   - Open PowerShell as Administrator and run:
     ```powershell
     wsl --install
     ```
   - Restart your computer if prompted.

2. **Install Ubuntu (or other Linux distribution)**:
   - Follow the WSL setup prompts to install a Linux distribution.

3. **Install .NET SDK**:
   - Inside your WSL environment, run:
     ```bash
     wget https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh -O dotnet-install.sh
     chmod +x dotnet-install.sh
     ./dotnet-install.sh --channel 7.0
     ```
   - Add .NET to your PATH in `~/.bashrc` or `~/.zshrc`:
     ```bash
     export PATH=$PATH:$HOME/.dotnet
     export DOTNET_ROOT=$HOME/.dotnet
     ```
   - Reload your shell:
     ```bash
     source ~/.bashrc
     ```

4. **Install Python and Virtual Environment**:
   - Ensure Python 3 is installed. Install `venv`:
     ```bash
     sudo apt update
     sudo apt install python3-venv
     ```
   - Create a virtual environment for your project:
     ```bash
     python3 -m venv ~/airflow_project/venv
     source ~/airflow_project/venv/bin/activate
     ```

5. **Install Apache Airflow**:
   - Install Airflow dependencies in the virtual environment:
     ```bash
     pip install apache-airflow
     ```

### C# Setup

- Ensure your `hello.cs` and `Program.cs` scripts are correctly configured.
- Use the following `csharp.csproj` to define the C# project:
  ```xml
  <Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
      <OutputType>Exe</OutputType>
      <TargetFramework>net7.0</TargetFramework>
    </PropertyGroup>
  </Project>
  ```
- Build the project:
  ```bash
  dotnet build
  ```
- Test the project:
  ```bash
  dotnet run --project /path/to/your/csharp/project
  ```

## Airflow DAG Workflow

### `run_csharp_python.py`

This DAG contains two tasks:

1. **C# Task** (`run_csharp`):
   - Executes the `hello.cs` script using .NET.

2. **Python Task** (`run_python`):
   - Executes the `hello.py` Python script.

### Task Dependencies

- `run_csharp` must succeed before `run_python` is executed.

### DAG Schedule

- Runs every 10 seconds (for demonstration purposes).

## Usage

1. **Start the Airflow Scheduler and Webserver**:
   ```bash
   airflow db init
   airflow scheduler &
   airflow webserver -p 8080 &
   ```

2. **Deploy the DAG**:
   - Place `run_csharp_python.py` into the Airflow `dags` directory.

3. **Access the Airflow UI**:
   - Open your browser and go to `http://localhost:8080`.

4. **Trigger the DAG**:
   - Locate the DAG `run_csharp_python` in the Airflow UI.
   - Click the "Trigger DAG" button.

## Example Output

### C# Task Output
```plaintext
Hello from C#!
C# script executed successfully
```

### Python Task Output
```plaintext
Hello from Python!
Python Version: 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0]
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

