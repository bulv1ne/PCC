#!/usr/bin/env python
import argparse
import asyncio

from .utils import run_command


async def run_pcc(test=False):
    if test:
        await run_command("isort", "--check-only", "--diff", "--quiet")
        await run_command("black", "--check", "--exclude", "node_modules", ".")
    else:
        await run_command("isort", "-y")
        await run_command("black", "--exclude", "node_modules", ".")


def main():
    parser = argparse.ArgumentParser("pcc", description="Python Clean Code")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    asyncio.run(run_pcc(test=args.test))


if __name__ == "__main__":
    main()
