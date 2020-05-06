#!/usr/bin/env python
import argparse
import asyncio

from .utils import run_command


async def main():
    parser = argparse.ArgumentParser("pcc", description="Python Clean Code")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        await run_command("isort", "--check-only", "--diff", "--quiet")
        await run_command("black", "--check", "--exclude", "node_modules", ".")
    else:
        await run_command("isort", "-y")
        await run_command("black", "--exclude", "node_modules", ".")


if __name__ == "__main__":
    asyncio.run(main())
