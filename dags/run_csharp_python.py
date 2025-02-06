from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Python 任務函數
def run_python_script():
    result = subprocess.run(
        ["/home/kaiicheng/airflow_project/venv/bin/python3",
         "/home/kaiicheng/airflow_csharp_python/csharp_python_scripts/python/hello.py"],
        text=True,
        capture_output=True,
    )
    # print("Standard Output:", result.stdout.strip())  # 打印標準輸出
    # print("Error Output:", result.stderr.strip())  # 打印錯誤輸出
    return f"Standard Output: {result.stdout.strip()} | Error Output: {result.stderr.strip()}"

default_args = {
    "owner": "kai",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

# 定義 DAG，每 10 秒執行一次
dag = DAG(
    "run_csharp_python",
    default_args=default_args,
    schedule_interval=timedelta(seconds=10),  # 設置調度間隔
    catchup=False,  # 禁止補跑（避免積壓任務）
)

# 執行 C# 程式
run_csharp = BashOperator(
    task_id="run_csharp",
    # bash_command="export PATH=$PATH:/user/bin/dotnet && dotnet run --project /home/kaiicheng/airflow_csharp_python/csharp_python_scripts/csharp/ && echo 'C# script executed successfully && /home/kaiicheng/.dotnet/dotnet run --project /home/kaiicheng/airflow_csharp_python/csharp_python_scripts/csharp/csharp.csproj'",
    bash_command="export PATH=$PATH:/home/kaiicheng/.dotnet && export DOTNET_ROOT=/home/kaiicheng/.dotnet && /home/kaiicheng/.dotnet/dotnet run --project /home/kaiicheng/airflow_csharp_python/csharp_python_scripts/csharp/csharp.csproj && echo 'C# script executed successfully'", 
    dag=dag,
)

# 執行 Python 程式
run_python = PythonOperator(
    task_id="run_python",
    python_callable=run_python_script,
    dag=dag,
)

# 設置任務依賴
run_csharp >> run_python