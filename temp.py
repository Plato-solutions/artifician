import os
import subprocess

def convert_md_to_rst(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".rst"):
            md_file = os.path.join(directory, filename)
            rst_file = os.path.join(directory, filename.replace(".rst", ".rst"))

            # Command to convert Markdown to reStructuredText
            command = ["pandoc", "--from=markdown", "--to=rst", md_file, "-o", rst_file]

            # Execute the command
            subprocess.run(command)
            print(f"Converted: {md_file} to {rst_file}")

# Replace 'your_directory_path' with the path to your Markdown files
convert_md_to_rst("/Users/abhijeet/Desktop/abhijeet/plato/github/artifician/docs")
