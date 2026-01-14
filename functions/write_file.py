import os

from google import genai
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_target_dir = (
            os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        )

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside of the permitted working directory'

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        dir_path = os.path.dirname(target_dir)
        os.makedirs(dir_path, exist_ok=True)

        with open(target_dir, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the permitted working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file whose contents should be read",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
