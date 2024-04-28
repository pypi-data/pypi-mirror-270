import os
import json
import pandas as pd
import ipdb
import yaml
from typing import Any
from beartype import beartype
from beartype.typing import Callable, Any
from rich import print
import re
from .bunch import Bunch


def resolve_path(base_path: str, relative_path: str) -> str:
    return (
        os.path.join(base_path, relative_path)
        if not os.path.isabs(relative_path)
        else relative_path
    )


def load_yaml_file(file_path: str) -> Any:
    with open(file_path, "r", encoding="utf8") as file:
        return yaml.safe_load(file)


def transform_object(obj: dict[str, Any]) -> dict[str, Any]:
    new_obj = {}
    for key, value in obj.items():
        clean_key = key.replace("\r", "")
        if value == "null":
            new_obj[clean_key] = None
        elif isinstance(value, str) and value.isdigit():
            new_obj[clean_key] = int(value)
        else:
            new_obj[clean_key] = value
    return new_obj


def load_specific_text_file(relative_file_path: str, base_path: str) -> Any:
    file_path = resolve_path(base_path, relative_file_path)
    assert os.path.exists(file_path), f"File {file_path} does not exist."
    if os.path.isdir(file_path):
        return load_yaml_package(file_path)
    elif os.path.splitext(file_path)[1] in [".yaml", ".yml"]:
        return load_yaml_file(file_path)
    elif os.path.splitext(file_path)[1] == ".json":
        with open(file_path, "r", encoding="utf8") as file:
            return json.load(file)
    elif os.path.splitext(file_path)[1] == ".csv":
        assert os.path.getsize(file_path) > 0, f"File {file_path} is empty."
        return (
            pd.read_csv(file_path)
            .applymap(lambda x: transform_object(x) if isinstance(x, dict) else x)
            .to_dict(orient="records")
        )
    else:
        with open(file_path, "r", encoding="utf8") as file:
            result_string_unparsed = file.read().strip()
        return parse_string(result_string_unparsed, base_path)


def load_files_within_string(current_value: str, base_path: str):
    """now finds all the ${load:...} patterns in the string"""
    pattern = r"\$\{load:([^}]+)\}"
    matches = re.findall(pattern, current_value)
    target_value = current_value
    for match in matches:
        file_path = resolve_path(base_path, match)
        with open(file_path, "r", encoding="utf8") as file:
            target_value = current_value.replace(f"${{load:{match}}}", file.read())
    return target_value


def parse_string(current_value: str, base_path: str):
    if current_value.startswith("load:"):
        desired_file_path = current_value.split(":")[1].strip()
        return load_specific_text_file(desired_file_path, base_path)
    else:
        # Handle string properties that are not files
        # Placeholder replacements can be implemented here if needed
        return load_files_within_string(current_value, base_path)


def load_yaml(base_path: str, obj: Any) -> dict[str, Any]:
    target_obj = json.loads(json.dumps(obj))
    keys = list(obj) if isinstance(obj, dict) else range(len(obj))
    for key in keys:
        current_value = obj[key]
        if isinstance(current_value, str):
            target_obj[key] = parse_string(current_value, base_path)

        elif isinstance(current_value, dict):
            target_obj[key] = load_yaml(base_path, current_value)
    return target_obj


def return_existent(paths: list[str]) -> str:
    existent = [os.path.exists(path) for path in paths]
    assert any(existent), f"None of the paths exist: {paths}"
    assert existent.count(True) == 1, f"Multiple paths exist: {paths}"
    return paths[existent.index(True)]


def get_main(folder_or_file_path: str) -> str:
    assert os.path.exists(
        folder_or_file_path
    ), f"Folder or file {folder_or_file_path} does not exist"
    if os.path.isdir(folder_or_file_path):
        return return_existent(
            [
                os.path.join(folder_or_file_path, "main.yaml"),
                os.path.join(folder_or_file_path, "main.yml"),
            ]
        )
    elif os.path.splitext(folder_or_file_path)[1] in [".yaml", ".yml"]:
        return folder_or_file_path
    raise ValueError(f"No main file found: {folder_or_file_path}")


def wrap_strings(data, string_wrapper: type = str):
    if isinstance(data, dict):
        return {
            k: string_wrapper(v) if isinstance(v, str) else wrap_strings(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [wrap_strings(item) for item in data]
    else:
        return data


def load_yaml_package_as_bunch(
    folder_or_file_path: str, string_wrapper: type = str
) -> Bunch:
    package = load_yaml_package(folder_or_file_path, string_wrapper)
    return Bunch(package)


def load_yaml_package(
    folder_or_file_path: str, string_wrapper: type = str
) -> dict[str, Any]:
    main_yaml_path = get_main(folder_or_file_path)
    obj = load_yaml_file(main_yaml_path)
    result_unwrapped = load_yaml(os.path.dirname(main_yaml_path), obj)
    result = wrap_strings(result_unwrapped, string_wrapper)
    assert isinstance(result, dict), f"Result is not a dict: {result}"
    mapped_package = apply_to_leaves_wrapper(result, replace_self_references)
    return mapped_package


def print_object_with_newlines(obj: Any, indent: str = "") -> None:
    for key, value in obj.items():
        if isinstance(value, dict):
            print(f"{indent}{key}: {{")
            print_object_with_newlines(value, indent + "  ")
            print(f"{indent}}}")
        elif isinstance(value, list):
            print(f"{indent}{key}: [")
            for item in value:
                if isinstance(item, dict):
                    print_object_with_newlines(item, indent + "  ")
                else:
                    print(f"{indent}  {item}")
            print(f"{indent}]")
        else:
            print(f"{indent}{key}: {value}")


@beartype
def apply_to_leaves(
    obj: Any,
    func: Callable,
    orig_obj: Any = None,
    modified: dict | None = None,
    depth: int = 0,
):
    if orig_obj is None:
        orig_obj = obj
    if modified is None:
        modified = {"flag": False}
    if isinstance(obj, dict):
        return {
            k: apply_to_leaves(v, func, orig_obj, modified, depth + 1)
            for k, v in obj.items()
        }
    elif isinstance(obj, list):
        return [
            apply_to_leaves(item, func, orig_obj, modified, depth + 1) for item in obj
        ]
    else:  # Leaf node
        if not modified["flag"]:
            new_obj = func(obj, orig_obj)
            if new_obj != obj:
                modified["flag"] = True
                return new_obj
        return obj


def apply_to_leaves_wrapper(obj: Any, func: Callable):
    modified = True
    while modified:
        modified_flag = {"flag": False}
        obj = apply_to_leaves(obj, func, modified=modified_flag)
        modified = modified_flag["flag"]
    return obj


def access_by_path(data, path):
    elements = path.strip(".").split(".")
    for el in elements:
        if "[" in el and "]" in el:
            key, index = el.split("[")
            index = int(index[:-1])  # Removing the ']' and converting to int
            data = data[key][index]
        else:
            assert el in data, f"Key {el} not found in object {json.dumps(data)}"
            data = data[el]
            # except:
            #     import ipdb
            #
            #     ipdb.set_trace()
    return data


@beartype
def replace_self_references(maybe_text, root_obj):
    if isinstance(maybe_text, str):
        pattern = r"\${this\.([a-zA-Z_0-9\[\]\.]+)}"
        matches = re.findall(pattern, maybe_text)
        if matches:
            for match in matches:
                result = access_by_path(root_obj, match)
                full_match = (
                    f"${{this.{match}}}"  # Construct the full pattern to replace
                )
                result = access_by_path(root_obj, match)
                maybe_text = re.sub(
                    re.escape(full_match), str(result), maybe_text, count=1
                )
    return maybe_text


# Exported functions
__all__ = ["load_yaml_file", "load_yaml_package", "load_yaml_package_as_bunch", "Bunch"]


if __name__ == "__main__":
    package = load_yaml_package("./prompts")
    mapped_package = apply_to_leaves_wrapper(package, replace_self_references)
    print(mapped_package)
