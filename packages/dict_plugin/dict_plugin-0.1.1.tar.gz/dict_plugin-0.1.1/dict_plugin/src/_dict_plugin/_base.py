from typing import Any, Dict, List

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ImportString,
    RootModel,
    constr,
    field_validator,
)

NonEmptyStr = constr(strip_whitespace=True, min_length=1)


class _PluginArgs(RootModel):
    root: List[Any] = Field(default_factory=list)

    @field_validator("root")
    @classmethod
    def _resolve_plugins(cls, args: List[Any]) -> List[Any]:
        for idx, val in enumerate(args):
            try:
                args[idx] = Plugin(**val).generate()
            except Exception:
                continue
        return args


class _PluginKwargs(RootModel):
    root: Dict[NonEmptyStr, Any] = Field(default_factory=dict)

    @field_validator("root")
    @classmethod
    def _resolve_plugins(cls, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        for key, val in kwargs.items():
            try:
                kwargs[key] = Plugin(**val).generate()
            except Exception:
                continue
        return kwargs


class Plugin(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True, extra="forbid", frozen=True
    )

    obj: ImportString | Any = Field(
        description="Plugin's object.", examples=["len", "StandardScaler"]
    )
    init: bool = Field(
        description="Whether to call the obj with args and kwargs.",
        default=True,
    )
    args: _PluginArgs = Field(
        default_factory=_PluginArgs,
        validate_default=True,
        description="Arguments passed to the object along with kwargs if"
        " init=True. Arguments representing a Plugin are resolved to the"
        " plugin's self.",
        examples=[[5], [1, 2, 3], {"obj": "builtins.len", "args": [1, 2, 3]}],
    )
    kwargs: _PluginKwargs = Field(
        default_factory=_PluginKwargs,
        validate_default=True,
        description="keyword arguments passed to the object along with args if"
        " init=True. keyword arguments representing a Plugin are resolved to"
        " the plugin's self.",
        examples=[
            {"param1": "val1", "param2": {"obj": "len", "args": [1, 2, 3]}}
        ],
    )

    @field_validator("args")
    @classmethod
    def _get_parsed_args(cls, args: _PluginArgs) -> List[Any]:
        return args.root

    @field_validator("kwargs")
    @classmethod
    def _get_parsed_kwargs(cls, kwargs: _PluginKwargs) -> Dict[str, Any]:
        return kwargs.root

    def generate(self):
        """
        Generate the desired plugin.

        Returns:
            If `init` is set to False, `obj` is returned. Otherwise, the result of 
            `obj(*args, **kwargs)` is returned.
        """
        if self.init:
            return self.obj(*self.args, **self.kwargs)
        return self.obj


if __name__ == "__main__":

    p = Plugin(**{"obj": "builtins.len", "args": [[1, 2, 3]]})
    print(p.generate())

    p = Plugin(
        obj="sklearn.preprocessing.StandardScaler",
        init=True,
        kwargs={"blocker": {"obj": "builtins.len", "args": [[1, 2, 3]]}},
    )
    print(p)

    p = Plugin(obj="math.pi", init=False)
    print(p.generate())
