import shlex
from subprocess import Popen, PIPE

def get_exitcode_stdout_stderr(cmd):
	args = shlex.split(cmd)
	proc = Popen(args, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	exitcode = proc.returncode
	return exitcode, out, err

cmd = "julia -e 'Base.banner()'"
exitcode, out, err = get_exitcode_stdout_stderr(cmd)