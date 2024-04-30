import os
import orjson
import re

from pydantic import BaseModel, ValidationError
from pydantic.fields import FieldInfo
from typing import Optional, Any, Type, Iterator, Union, Literal

from hectiq_config.utils import template_to_model

class Config:
    """
    A Config object is an abstract object designed to store
    your configurations with a simple API.

    The Config object is a dictionary-like object that supports
    nested configurations and aliasing.

    Example:

    ```python
    config = Config(a=4, b=Config(c=5))
    assert config.a == 4
    assert config.b.c == 5
    ```

    """

    __static_attr__ = ["_state"]
    __static_methods__ = [
        "keys",
        "values",
        "items",
        "get",
        "save",
        "load",
        "pop",
        "copy",
        "validate",
        "cast",
        "to_dict",
        "to_model",
        "from_dict",
        "from_model",
        "template",
        "retrieve",
    ]
    alias_pattern = re.compile(r"\$\{?([a-zA-Z_][a-zA-Z0-9_.]*)\}?")
    seperator = "."

    def __init__(self, **kwargs):
        self._state: dict[str, Any] = {}
        for key in kwargs:
            if key in self.__static_attr__ + self.__static_methods__:
                raise KeyError(f"Key {key} is a reserved attribute.")
            setattr(self, key, kwargs[key])

    def validate(
        self,
        template: Union[dict[str, tuple[type, Any]], type[BaseModel], type[None]] = None,
        raise_exception: bool = False,
        extra: Optional[Literal["allow", "ignore", "forbid"]] = "forbid",
    ) -> bool:
        """Validate the configuration using the template provided in the constructor.

        Args:
            template (dict or pydantic.BaseModel, optional): A template to validate the configuration
                against. Default: None.
            raise_exception (bool, optional): If True, raise an exception if the configuration does
                not match the template. Default: False.
            extra (str, optional): How to handle extra fields that are not specified in the template.
                Default: "forbid". Can be "ignore" or "allow".

        Raises:
            ValidationError: If the configuration does not match the template and `raise_exception` is True.
        """
        if template is None:
            return True
        try:
            self.to_model(template=template, extra=extra)
        except ValidationError as e:
            if raise_exception:
                raise e
            return False
        return True

    def cast(self, template: Union[dict[str, tuple[type, Any]], type[BaseModel], type[None]] = None, 
             extra: Optional[Literal["allow", "ignore", "forbid"]] = "allow") -> "Config":
        """Cast the values of a configuration to a new Config object using a template.
        Args:
            template (dict or pydantic.BaseModel, optional): A template to cast the configuration
                against. Default: None.
            extra (str, optional): How to handle extra fields that are not specified in the template.
                Default: "allow". Can be "ignore" or "forbid".
        Returns:
            Config: A new Config object with the same values as the current one
                casted according to the template.
        """
        model = self.to_model(template=template, extra=extra)
        if model is None:
            return self
        return Config.from_model(model)

    def save(self, path: str) -> None:
        """Dump the configuration to a file in a JSON format.
        If the directory does not exist, it will be created.
        The config must be serializable to JSON using orjson.

        Args:
            path (str): Path to the file.
        """
        if os.path.dirname(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
        bytes_content = orjson.dumps(self.to_dict(), default=str, option=orjson.OPT_INDENT_2)
        with open(path, "wb") as f:
            f.write(bytes_content)

    @classmethod
    def load(cls, path: str) -> "Config":
        """Load a configuration from a file.
        The file must be in a JSON format and deserializable using orjson.

        Args:
            path (str): Path to the file.
        """
        with open(path, "rb") as f:
            content = f.read()
        content = orjson.loads(content)
        return cls.from_dict(content)

    @classmethod
    def from_dict(cls, data: dict) -> "Config":
        """Convert a dict to a Config object.
        `data` can be nested (dict within dict), which will generate sub configs.
        If `data` is not a dict, then the method returns `data`.

        Example:
        -------------
        d = {"a": {"b": 4}}
        config = Config.from_dict(d)
        assert config.a.b == 4
        """
        if not isinstance(data, dict):
            return data

        config = cls(**data)
        return config

    @classmethod
    def from_model(cls, model: BaseModel) -> "Config":
        """Convert a pydantic model to a Config object.
        `model` can be nested (model within model), which will generate sub configs.
        If `model` is not a model, then the method returns `model`.

        Example:
        -------------
        m = MyPydanticModel(a=4)
        config = Config.from_model(m)
        assert config.a == 4
        """
        config = cls(**model.model_dump())
        return config

    def to_dict(self) -> dict[str, Any]:
        """A property that converts a config to a dict. Supports nested Config."""
        d = {}
        for key, item in self.items():
            if isinstance(item, Config):
                d[key] = item.to_dict()
            else:
                d[key] = item
        return d

    def to_model(
        self,
        template: Union[dict[str, tuple[type, Any]], type[BaseModel], type[None]] = None,
        extra: Literal["allow", "ignore", "forbid"] = "ignore",
    ) -> Optional[BaseModel]:
        """Convert a config to a pydantic model.

        Args:
            template (dict or pydantic.BaseModel, optional): A template to convert the configuration
                against. Default: None.
            extra (str, optional): How to handle extra fields that are not specified in the template.
                Default: "ignore".

        Returns:
            pydantic.BaseModel: A pydantic model with the same values as the current config.
        """
        template = template or self.template()
        if isinstance(template, type) and issubclass(template, BaseModel):
            template = {k: (v.annotation, v) for k, v in template.model_fields.items()}
        if not isinstance(template, dict):
            raise TypeError("Template must be a dict or a pydantic model.")
        model = template_to_model("ConfigModel", template, extra=extra)
        return model(**self.to_dict())

    def template(self) -> dict[str, tuple[Type, FieldInfo]]:
        """
        Return a template associated to the configuration.
        """
        template = {}
        for k, v in self.items():
            if isinstance(v, Config):
                template[k] = v.template()
            else:
                template[k] = (type(v), FieldInfo(examples=[v], annotation=type(v)))
        return template

    def pop(self, key, default=None) -> Any:
        return self._state.pop(key, default)

    def keys(self) -> list[str]:
        return self._state.keys()

    def values(self) -> list[Any]:
        return dict(**{k: self.get(k) for k in self.keys()}).values()

    def items(self) -> list[tuple[str, Any]]:
        return dict(zip(self.keys(), self.values())).items()

    def copy(self) -> "Config":
        return Config.from_dict(self.to_dict())

    def get(self, name: str, default: Optional[Any] = None) -> Any:
        # Nested keys
        if self.seperator in name:
            root_key, *keys = name.split(self.seperator)
            return self._state.get(root_key, Config()).get(self.seperator.join(keys), default)

        # Extract value
        value = self._state.get(name, default)

        # Alias value
        if isinstance(value, str) and (match := self.alias_pattern.match(value)):
            return self.get(match.group(1), default)
        return value

    def __contains__(self, key: str) -> bool:
        return key in self._state

    def __getattr__(self, name: str) -> Any:
        return self.get(name, None)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__static_attr__:
            object.__setattr__(self, name, value)
            return
        if isinstance(value, dict):
            self._state[name] = Config.from_dict(value)
            return
        self._state[name] = value

    def __getstate__(self) -> dict[str, Any]:
        return self._state

    def __setstate__(self, d) -> None:
        self._state.update(d)

    def __getitem__(self, key) -> Optional[Any]:
        return self.get(key)

    def __dir__(self) -> list[str]:
        return self._state.keys()

    def __setitem__(self, key, value) -> None:
        self._state[key] = value

    def __iter__(self) -> Iterator[str]:
        return self._state.__iter__()

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        bytes_content = orjson.dumps(self.to_dict(), option=orjson.OPT_INDENT_2)
        return bytes_content.decode("utf-8")
