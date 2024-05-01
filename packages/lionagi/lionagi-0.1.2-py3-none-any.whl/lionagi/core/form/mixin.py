from abc import ABC
from typing import Any
from lionagi.core.form.field_validator import validation_funcs


from lionagi.libs import convert, func_call

non_prompt_words = [
    "id_",
    "node_id",
    "meta",
    "metadata",
    "timestamp",
    "content",
    "signature",
    "task",
    "template_name",
    "version",
    "description",
    "in_validation_kwargs",
    "out_validation_kwargs",
    "fix_input",
    "fix_output",
    "input_fields",
    "output_fields",
    "choices",
    "prompt_fields",
    "prompt_fields_annotation",
    "instruction_context",
    "instruction",
    "instruction_output_fields",
    "in_",
    "out",
    "process",
    "_validate_field",
    "_process_input",
    "_process_response",
    "_validate_field_choices",
    "_validate_input_choices",
    "_validate_output_choices",
]


class PromptTemplateMixin(ABC):
    def _validate_field_choices(self, fields, fix_: bool = False):
        if len(self.choices) >= 1:
            for k, choices in self.choices.items():
                if k in fields and not self._validate_field(
                    k, getattr(self, k), choices, fix_
                ):
                    raise ValueError(
                        f"Invalid choice for field {k}: {getattr(self, k)} is not in {choices}"
                    )

    def _validate_input_choices(self):
        return self._validate_field_choices(self.input_fields, self.fix_input)

    def _validate_output_choices(self):
        return self._validate_field_choices(self.output_fields, self.fix_output)

    def _validate_field(self, k, v, choices=None, keys=None, fix_=False, **kwargs):

        str_ = self._prompt_fields_annotation[k]

        if keys:
            v_ = validation_funcs["dict"](v, keys=keys, fix_=fix_, **kwargs)
            setattr(self, k, v_)
            return True

        if choices:
            v_ = validation_funcs["enum"](v, choices=choices, fix_=fix_, **kwargs)
            if v_ not in choices:
                raise ValueError(f"{v} is not in chocies {choices}")
            setattr(self, k, v_)
            return True

        if "lionagi.core.prompt.action_template.actionrequest" in str_:
            self.__setattr__(k, validation_funcs["action"](v))
            return True

        if "bool" in str_ and "str" not in str_:
            self.__setattr__(k, validation_funcs["bool"](v, fix_=fix_, **kwargs))
            return True

        if any(i in str_ for i in ["int", "float", "number"]) and "str" not in str_:
            self.__setattr__(k, validation_funcs["number"](v, fix_=fix_, **kwargs))
            return True

        elif "str" in str_:
            self.__setattr__(k, validation_funcs["str"](v, fix_=fix_, **kwargs))
            return True

        return False

    def _process_input(self, fix_=False):
        kwargs = self.in_validation_kwargs.copy()
        for k, v in self.in_.items():
            if k not in kwargs:
                kwargs = {k: {}}

            if self._field_has_choices(k):
                self.choices[k] = self.model_fields[k].json_schema_extra["choices"]
                if self._validate_field(
                    k, v, choices=self.choices[k], fix_=fix_, **kwargs[k]
                ):
                    continue
                else:
                    raise ValueError(f"{k} has no choices")

            elif self._validate_field(k, v, fix_=fix_, **kwargs[k]):
                continue
            else:
                raise ValueError(f"failed to validate field {k}")

    def _get_field_attr(self, k, attr) -> Any:
        if not self._field_has_attr(k, attr):
            raise ValueError(f"field {k} has no attribute {attr}")
        field = self.model_fields[k]
        a = getattr(field, attr)
        if not a:
            try:
                a = field.json_schema_extra[attr]
                return a
            except Exception:
                return None
        return a

    def _field_has_attr(self, k, attr):
        a = False

        field = self.model_fields[k]
        a = hasattr(field, attr)

        if not a:
            try:
                a = (
                    self.model_fields[k].json_schema_extra[attr] is not None
                    and attr in self.model_fields[k].json_schema_extra
                )
                return a if isinstance(a, bool) else False
            except Exception:
                return False

    def _field_has_keys(self, k):
        return self._field_has_attr(k, "keys")

    def _field_has_choices(self, k):
        return self._field_has_attr(k, "choices")

    def _process_choices(self, k, v, fix_=False, kwargs=None):
        choices = self._get_field_attr(k, "choices")

        if self._validate_field(k, v, choices=choices, fix_=fix_, **kwargs):
            self.choices[k] = choices
            return True
        else:
            raise ValueError(f"{k} has no choices")

    def _process_keys(self, k, v, fix_=False, kwargs=None):
        keys = self._get_field_attr(k, "keys")
        if self._validate_field(k, v, keys=keys, fix_=fix_, **kwargs):
            return True
        else:
            raise ValueError(f"{k} has no keys")

    def _process_response(self, out_, fix_=True):
        kwargs = self.out_validation_kwargs.copy()
        for k, v in out_.items():
            if k not in kwargs:
                kwargs = {k: {}}

            if self._field_has_choices(k):
                try:
                    return self._process_choices(k, v, fix_=fix_, kwargs=kwargs[k])
                except Exception as e:
                    raise ValueError(
                        f"failed to process field {k} with value {v}"
                    ) from e

            elif self._field_has_keys(k):
                try:
                    return self._process_keys(k, v, fix_=fix_, kwargs=kwargs[k])
                except Exception as e:
                    raise ValueError(
                        f"failed to process field {k} with value {v}"
                    ) from e

            elif self._validate_field(k, v, fix_=fix_, **kwargs[k]):
                continue

            else:
                raise ValueError(f"failed to validate field {k} with value {v}")

    @staticmethod
    def _get_input_output_fields(str_: str) -> Any:
        inputs, outputs = str_.split("->")

        input_fields = [convert.strip_lower(i) for i in inputs.split(",")]
        output_fields = [convert.strip_lower(o) for o in outputs.split(",")]

        return input_fields, output_fields

    @property
    def _prompt_fields_annotation(self):
        dict_ = {i: self.model_fields[i].annotation for i in self.prompt_fields}
        for k, v in dict_.items():
            if "|" in str(v):
                v = str(v)
                v = v.split("|")
                dict_[k] = func_call.lcall(v, convert.strip_lower)
            else:
                dict_[k] = [v.__name__]

        return dict_
