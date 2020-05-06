import asyncio


async def run_command(*args, **kwargs):
    kwargs.setdefault("stdout", asyncio.subprocess.PIPE)
    kwargs.setdefault("stderr", asyncio.subprocess.PIPE)
    print(f"[{' '.join(args)!r} started]")
    proc = await asyncio.create_subprocess_exec(*args, **kwargs)

    stdout, stderr = await proc.communicate()

    print(f"[{' '.join(args)!r} exited with {proc.returncode}]")
    if proc.returncode:
        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")
    return proc.returncode
