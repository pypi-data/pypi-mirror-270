import subprocess
import pkg_resources

def main():
    executable_path = pkg_resources.resource_filename('CliDApp4Rhino', 'CliDApp4Rhino')
    subprocess.run([executable_path])
