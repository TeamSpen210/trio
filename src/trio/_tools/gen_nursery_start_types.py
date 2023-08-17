"""Generate the protocols, typevars and overload for nursery.start()."""

from __future__ import annotations

from io import StringIO
from pathlib import Path
from typing import TextIO

COUNT = 32  # Number of positional args to support.
MODNAME = "_nstart"  # Name the module is imported under.

IMPORTS = """\
# Generated file, see src/trio/_tools/gen_nursery_start_types.py
from __future__ import annotations

from typing import Any, Awaitable, Protocol, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from trio._core import _run as run
"""


def varname(index: int) -> str:
    return f"Arg{index + 1}"


def write_vars(f: TextIO) -> None:
    f.write('StatusT_co = TypeVar("StatusT_co", covariant=True)\n')
    for name in map(varname, range(COUNT)):
        f.write(f'{name} = TypeVar("{name}", contravariant=True)\n')


def write_protocols(f: TextIO) -> None:
    """Generate all the protocols."""
    # Implementation type and unary are special cases.
    f.write(
        """\
class FuncImpl(Protocol[StatusT_co]):
    def __call__(
        self, *args: Any, task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func0(Protocol[StatusT_co]):
    def __call__(
        self, /, *, task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

"""
    )

    for count in range(1, COUNT + 1):
        f.write(f"class Func{count}(Protocol[")
        tvars = [varname(i) for i in range(count)]
        f.write(", ".join(tvars))
        f.write(
            """, StatusT_co]):
    def __call__(
        self,
        """
        )
        for name in tvars[:-1]:
            f.write(f"{name.lower()}: {name}, ")
        f.write(
            f"""{tvars[-1].lower()}: {tvars[-1]},
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

"""
        )


def build_decos() -> str:
    f = StringIO()
    f.write(
        f"""\
    # fmt: off
    @overload  # Note - unary async_fn can be passed by keyword!
    async def start(self, async_fn: {MODNAME}.Func0[StatusT], *, name: object = None) -> StatusT: ...
"""
    )
    for count in range(1, COUNT + 1):
        f.write(
            f"""\
    @overload
    async def start(
        self, async_fn: {MODNAME}.Func{count}["""
        )
        tvars = [varname(i) for i in range(count)]
        for name in tvars:
            f.write(f"{MODNAME}.{name}, ")
        f.write(
            """StatusT],
        """
        )
        for name in tvars[:-1]:
            f.write(f"{name.lower()}: {MODNAME}.{name}, ")
        f.write(
            f"""{tvars[-1].lower()}: {MODNAME}.{tvars[-1]},
        /, *,
        name: object = None,
    ) -> StatusT: ...
"""
        )
    f.write(
        """\
    # fmt: on
"""
    )
    return f.getvalue()


def patch_run(filename: Path) -> None:
    """Patch the run module."""
    new_code = build_decos()
    prefix: list[str] = []
    suffix: list[str] = []
    with open(filename) as src:
        for line in src:
            prefix.append(line)
            if "GEN NURSERY START" in line:
                break
        # Skip old code.
        for line in src:
            if "GEN NURSERY END" in line:
                suffix.append(line)
                break
        suffix.extend(src)

    with open(filename, "w") as dest:
        dest.writelines(prefix)
        dest.write(new_code)
        dest.writelines(suffix)


def main() -> None:
    """Generate the code."""
    source_root = Path.cwd()
    # Double-check we found the right directory
    assert (source_root / "LICENSE").exists()

    with open(source_root / "src/trio/_core/_nursery_start.py", "w") as f:
        f.write(IMPORTS)
        f.write("\n\n")
        write_vars(f)
        f.write("\n\n# fmt: off\n")
        write_protocols(f)
    patch_run(source_root / "src/trio/_core/_run.py")


if __name__ == "__main__":  # pragma: no cover
    main()
