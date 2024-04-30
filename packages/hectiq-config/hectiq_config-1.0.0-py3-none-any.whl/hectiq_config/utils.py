from pydantic import create_model, BaseModel, ConfigDict
from pydantic.fields import FieldInfo
from typing import  Any, Type

def template_to_model(
    name: str, template_dict: dict[str, tuple[type, Any]], *, extra: str = "ignore"
) -> Type[BaseModel]:
    """Create a pydantic model from a template dict.

    Args:
        name (str): The name of the model.
        template_dict (dict): A dictionary with the template.
        extra (str, optional): How to handle extra fields that are not specified in the template.
            Default: "ignore".
    
    Returns:
        pydantic.BaseModel: A pydantic model with the specified fields.
    """
    fields = {}
    for key, value in template_dict.items():
        if isinstance(value, dict):
            fields[key] = (template_to_model(key, value, extra=extra), ...)
        else:
            fields[key] = value
    return create_model(name, **fields, __config__=ConfigDict(extra=extra))

def model_to_template(model: BaseModel) -> dict[str, tuple[type, FieldInfo]]:
    """
    Return a template associated to the configuration.

    Args:
        model (pydantic.BaseModel): A pydantic model.

    Returns:
        dict[str, tuple[Type, FieldInfo]]: A template with the same fields as the model.
    """
    template = {}
    for prop, info in model.model_fields.items():
        type = info.annotation
        if issubclass(type, BaseModel):
            template[prop] = model_to_template(type)
        else:
            template[prop] = (type, info)
    return template
