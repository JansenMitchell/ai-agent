import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_dir.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args:
            command.extend(args)
        result = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
        output = ""
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}\n'
        elif not result.stdout and not result.stderr:
            output += "No output produced\n"
        else:
            output += f"STDOUT: {result.stdout.strip()}\n"
            output += f"STDERR: {result.stderr.strip()}\n"
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'
