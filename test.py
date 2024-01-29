import subprocess 

def run():
  subprocess.run(["echo", "Hello from subprocess"], check=True, text=True)
