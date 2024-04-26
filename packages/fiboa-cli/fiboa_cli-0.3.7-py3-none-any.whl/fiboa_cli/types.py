import pyarrow as pa
import pyarrow.types as pat
import pandas as pd
import numpy as np

def is_enum(schema):
    return isinstance(schema.get("enum"), list)


def get_geopandas_dtype(type, required = False, schema = {}):
    """
    fiboa datatypes to geopandas datatypes
    """
    if is_enum(schema) and (type == "string" or type.startswith("int") or type.startswith("uint")):
        return "category"
    elif type == "boolean":
        if required:
            return "bool"
        else:
            return "boolean"
    elif type == "int8":
        if required:
            return "int8"
        else:
            return "Int8"
    elif type == "uint8":
        if required:
            return "uint8"
        else:
            return "UInt8"
    elif type == "int16":
        if required:
            return "int16"
        else:
            return "Int16"
    elif type == "uint16":
        if required:
            return "uint16"
        else:
            return "UInt16"
    elif type == "int32":
        if required:
            return "int32"
        else:
            return "Int32"
    elif type == "uint32":
        if required:
            return "uint32"
        else:
            return "UInt32"
    elif type == "int64":
        if required:
            return "int64"
        else:
            return "Int64"
    elif type == "uint64":
        if required:
            return "uint64"
        else:
            return "UInt64"
    elif type == "float":
        if required:
            return "float32"
        else:
            return "Float32"
    elif type == "double":
        if required:
            return "float64"
        else:
            return "Float64"
    elif type == "binary":
        return "bytearray" # todo: check
    elif type == "string":
        if required:
            return "str"
        else:
            return "string"
    elif type == "array":
        return lambda series: series.apply(lambda x: np.array(x))
    elif type == "object":
        return "object"
    elif type == "date":
        return "datetime64[D]"
    elif type == "date-time":
        return lambda series: pd.to_datetime(series)
    elif type == "geometry":
        return None, # not a column, don't convert geometry
    elif type == "bounding-box":
        raise Exception("Bounding boxes are not supported yet") # todo
    else:
        return None


def get_pyarrow_field(name, pa_type = None, schema = None, required = False):
    if pa_type is None:
        pa_type = get_pyarrow_type(schema)
    if pa_type is None:
        return None
    else:
        return pa.field(name, pa_type, nullable = not required)


def get_pyarrow_type(schema):
    """
    fiboa datatypes to pyarrow datatypes
    """
    dtype = schema.get("type")
    if dtype == "boolean":
        return pa.bool_()
    elif dtype.startswith("int") or dtype.startswith("uint") or dtype == "string" or dtype == "binary":
        return getattr(pa, dtype)()
    elif dtype == "float":
        return pa.float32()
    elif dtype == "double":
        return pa.float64()
    elif dtype == "array":
        pa_subtype = get_pyarrow_type(schema.get("items", {}))
        return pa.list_(pa_subtype)
    elif dtype == "object":
        additonal_properties = schema.get("additionalProperties", False)
        if additonal_properties is True:
            raise Exception("Additional properties for objects are not supported")
        else:
            properties = schema.get("properties", {})
            required_props = schema.get("required", [])
            fields = []
            for name, schema in properties.items():
               field = get_pyarrow_field(name, schema = schema, required = name in required_props)
               fields.append(field)
            return pa.struct(fields)
    elif dtype == "date":
        return pa.date32()
    elif dtype == "date-time":
        return pa.timestamp("ms", tz="UTC")
    elif dtype == "geometry":
        return pa.binary()
    elif dtype == "bounding-box":
        raise Exception("Bounding boxes are not supported yet") # todo
    else:
        return None

def get_pyarrow_type_for_geopandas(dtype):
    """
    geopandas datatypes to pyarrow datatypes
    """
    if dtype == "bool":
        return pa.bool_()
    elif dtype == "string" or dtype == "|S0" or dtype == "<U0":
        return pa.string()
    elif dtype == "float128" or dtype == "record" or dtype == "timedelta64" or dtype.startswith("complex"): # complex128/256/512
        raise Exception(f"Unsupported data type: {dtype}")
    elif dtype.startswith("int") or dtype.startswith("uint") or dtype.startswith("float"): # float16/32/64
        return getattr(pa, dtype)()
    elif dtype == "object":
        return pa.string() # todo
    elif dtype == "datetime64":
        return pa.timestamp("ms", tz="UTC")
    else:
        return None


# checks pyarrow datatypes
PA_TYPE_CHECK = {
    "boolean": pat.is_boolean,
    "int8": pat.is_int8,
    "uint8": pat.is_uint8,
    "int16": pat.is_int16,
    "uint16": pat.is_uint16,
    "int32": pat.is_int32,
    "uint32": pat.is_uint32,
    "int64": pat.is_int64,
    "uint64": pat.is_uint64,
    "float": pat.is_float32,
    "double": pat.is_float64,
    "binary": pat.is_binary,
    "string": pat.is_string,
    "array": pat.is_list,
    "object": pat.is_map,
    "date": pat.is_date32,
    "date-time": pat.is_timestamp,
    "geometry": pat.is_binary, # todo: check more?
    "bounding-box": None # todo
}

LOG_STATUS_COLOR = {
    "info": "white",
    "warning": "yellow",
    "error": "red",
    "success": "green"
}

SUPPORTED_PROTOCOLS = ["http", "https", "s3", "gs"]
