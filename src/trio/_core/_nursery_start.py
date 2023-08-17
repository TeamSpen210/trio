# Generated file, see src/trio/_tools/gen_nursery_start_types.py
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Awaitable, Protocol, TypeVar

if TYPE_CHECKING:
    from trio._core import _run as run


StatusT_co = TypeVar("StatusT_co", covariant=True)
Arg1 = TypeVar("Arg1", contravariant=True)
Arg2 = TypeVar("Arg2", contravariant=True)
Arg3 = TypeVar("Arg3", contravariant=True)
Arg4 = TypeVar("Arg4", contravariant=True)
Arg5 = TypeVar("Arg5", contravariant=True)
Arg6 = TypeVar("Arg6", contravariant=True)
Arg7 = TypeVar("Arg7", contravariant=True)
Arg8 = TypeVar("Arg8", contravariant=True)
Arg9 = TypeVar("Arg9", contravariant=True)
Arg10 = TypeVar("Arg10", contravariant=True)
Arg11 = TypeVar("Arg11", contravariant=True)
Arg12 = TypeVar("Arg12", contravariant=True)
Arg13 = TypeVar("Arg13", contravariant=True)
Arg14 = TypeVar("Arg14", contravariant=True)
Arg15 = TypeVar("Arg15", contravariant=True)
Arg16 = TypeVar("Arg16", contravariant=True)
Arg17 = TypeVar("Arg17", contravariant=True)
Arg18 = TypeVar("Arg18", contravariant=True)
Arg19 = TypeVar("Arg19", contravariant=True)
Arg20 = TypeVar("Arg20", contravariant=True)
Arg21 = TypeVar("Arg21", contravariant=True)
Arg22 = TypeVar("Arg22", contravariant=True)
Arg23 = TypeVar("Arg23", contravariant=True)
Arg24 = TypeVar("Arg24", contravariant=True)
Arg25 = TypeVar("Arg25", contravariant=True)
Arg26 = TypeVar("Arg26", contravariant=True)
Arg27 = TypeVar("Arg27", contravariant=True)
Arg28 = TypeVar("Arg28", contravariant=True)
Arg29 = TypeVar("Arg29", contravariant=True)
Arg30 = TypeVar("Arg30", contravariant=True)
Arg31 = TypeVar("Arg31", contravariant=True)
Arg32 = TypeVar("Arg32", contravariant=True)


# fmt: off
class FuncImpl(Protocol[StatusT_co]):
    def __call__(
        self, *args: Any, task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func0(Protocol[StatusT_co]):
    def __call__(
        self, /, *, task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func1(Protocol[Arg1, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func2(Protocol[Arg1, Arg2, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func3(Protocol[Arg1, Arg2, Arg3, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func4(Protocol[Arg1, Arg2, Arg3, Arg4, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func5(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func6(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func7(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func8(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func9(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func10(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func11(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func12(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func13(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func14(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func15(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func16(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func17(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func18(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func19(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func20(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func21(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func22(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func23(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func24(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func25(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func26(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func27(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func28(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, Arg28, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27, arg28: Arg28,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func29(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, Arg28, Arg29, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27, arg28: Arg28, arg29: Arg29,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func30(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, Arg28, Arg29, Arg30, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27, arg28: Arg28, arg29: Arg29, arg30: Arg30,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func31(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, Arg28, Arg29, Arg30, Arg31, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27, arg28: Arg28, arg29: Arg29, arg30: Arg30, arg31: Arg31,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...

class Func32(Protocol[Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9, Arg10, Arg11, Arg12, Arg13, Arg14, Arg15, Arg16, Arg17, Arg18, Arg19, Arg20, Arg21, Arg22, Arg23, Arg24, Arg25, Arg26, Arg27, Arg28, Arg29, Arg30, Arg31, Arg32, StatusT_co]):
    def __call__(
        self,
        arg1: Arg1, arg2: Arg2, arg3: Arg3, arg4: Arg4, arg5: Arg5, arg6: Arg6, arg7: Arg7, arg8: Arg8, arg9: Arg9, arg10: Arg10, arg11: Arg11, arg12: Arg12, arg13: Arg13, arg14: Arg14, arg15: Arg15, arg16: Arg16, arg17: Arg17, arg18: Arg18, arg19: Arg19, arg20: Arg20, arg21: Arg21, arg22: Arg22, arg23: Arg23, arg24: Arg24, arg25: Arg25, arg26: Arg26, arg27: Arg27, arg28: Arg28, arg29: Arg29, arg30: Arg30, arg31: Arg31, arg32: Arg32,
        /, *,
        task_status: run.TaskStatus[StatusT_co],
    ) -> Awaitable[object]: ...
