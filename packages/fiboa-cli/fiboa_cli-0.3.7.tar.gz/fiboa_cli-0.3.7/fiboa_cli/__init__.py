import click
import sys
import json
import os

from .convert import convert as convert_
from .create_geoparquet import create_geoparquet as create_geoparquet_
from .create_geojson import create_geojson as create_geojson_
from .describe import describe as describe_
from .jsonschema import jsonschema as jsonschema_
from .rename_extension import rename_extension as rename_extension_
from .validate import validate as validate_
from .validate_schema import validate_schema as validate_schema_
from .version import __version__, fiboa_version as fiboa_version_
from .util import log, check_ext_schema_for_cli, valid_file_for_cli, valid_file_for_cli_with_ext, valid_files_folders_for_cli, valid_folder_for_cli

@click.group()
@click.version_option(version=__version__)
def cli():
    """
    The fiboa CLI.
    """
    pass


## DESCRIBE
@click.command()
@click.argument('file', nargs=1, callback=lambda ctx, param, value: valid_file_for_cli_with_ext(value, ["parquet", "geoparquet"]))
@click.option(
    '--json', '-j',
    is_flag=True,
    type=click.BOOL,
    help='Print the JSON metadata.',
    default=False
)
@click.option(
    '--num', '-n',
    type=click.IntRange(min=0),
    help='Number of rows to show. Defaults to 10.',
    default=10
)
@click.option(
    '--column', '-c',
    type=click.STRING,
    multiple=True,
    help='Column names to show in the excerpt. Can be used multiple times. Shows all by default.',
    default=[]
)
def describe(file, json, num = 10, column = []):
    """
    Inspects the content of a fiboa GeoParquet file.
    """
    log(f"fiboa CLI {__version__} - Describe {file}\n", "success")
    try:
        if len(column) == 0:
            columns = None
        else:
            columns = list(column)
        describe_(file, json, num, columns)
    except Exception as e:
        log(e, "error")
        sys.exit(1)


## VALIDATE
@click.command()
@click.argument('files', nargs=-1, callback=lambda ctx, param, value: valid_files_folders_for_cli(value, ["parquet", "geoparquet", "json", "geojson"]))
@click.option(
    '--schema', '-s',
    type=click.STRING,
    callback=valid_file_for_cli,
    help='fiboa Schema to validate against. Can be a local file or a URL. If not provided, uses the fiboa version to load the schema for the released version.'
)
@click.option(
    '--ext-schema', '-e',
    multiple=True,
    callback=lambda ctx, param, value: check_ext_schema_for_cli(value, allow_none = False),
    help='Maps a remote fiboa extension schema url to a local file. First the URL, then the local file path. Separated with a comma character. Example: https://example.com/schema.yaml,/path/to/schema.yaml',
)
@click.option(
    '--fiboa-version', '-f',
    type=click.STRING,
    help='The fiboa version to validate against. Default is the version given in the collection.',
    default=None
)
@click.option(
    '--collection', '-c',
    type=click.Path(exists=True),
    help='Points to the Collection that defines the fiboa version and extensions.',
    default=None
)
@click.option(
    '--data', '-d',
    is_flag=True,
    type=click.BOOL,
    help='EXPERIMENTAL: Validate the data in the GeoParquet file. Enabling this might be slow or exceed memory. Default is False.',
    default=False
)
def validate(files, schema, ext_schema, fiboa_version, collection, data):
    """
    Validates a fiboa GeoParquet or GeoJSON file.
    """
    log(f"fiboa CLI {__version__} - Validator\n", "success")
    config = {
        "schema": schema,
        "extension_schemas": ext_schema,
        "fiboa_version": fiboa_version,
        "collection": collection,
        "data": data,
    }
    for file in files:
        log(f"Validating {file}", "info")
        try:
            result = validate_(file, config)
            if result:
                log("\n  => VALID\n", "success")
            else:
                log("\n  => INVALID\n", "error")
                sys.exit(1)
        except Exception as e:
            log(f"\n  => UNKNOWN: {e}\n", "error")
            sys.exit(2)


## VALIDATE SCHEMA
@click.command()
@click.argument('files', nargs=-1, callback=lambda ctx, param, value: valid_files_folders_for_cli(value, ["yaml", "yml"]))
@click.option(
    '--metaschema', '-m',
    callback=valid_file_for_cli,
    help=f'A fiboa schema metaschema to validate against.',
    default=None
)
def validate_schema(files, metaschema):
    """
    Validates a fiboa schema file.
    """
    log(f"fiboa CLI {__version__} - Schema Validator\n", "success")
    config = {
        "metaschema": metaschema
    }
    for file in files:
        log(f"Validating {file}", "info")
        result = validate_schema_(file, config)
        if result:
            sys.exit(0)
        else:
            sys.exit(1)


## CREATE PARQUET
@click.command()
@click.argument('files', nargs=-1, callback=lambda ctx, param, value: valid_files_folders_for_cli(value, ["json", "geojson"]))
@click.option(
    '--out', '-o',
    type=click.Path(exists=False),
    help='File to write the file to.',
    required=True
)
@click.option(
    '--collection', '-c',
    callback=valid_file_for_cli,
    help='Points to the Collection that defines the fiboa version and extensions. Only applies if not provided in the GeoJSON file (embedded or as link).',
    default=None
)
@click.option(
    '--schema', '-s',
    type=click.Path(exists=True),
    help='fiboa Schema to work against. If not provided, uses the fiboa version from the collection to load the schema for the released version.'
)
@click.option(
    '--ext-schema', '-e',
    multiple=True,
    callback=lambda ctx, param, value: check_ext_schema_for_cli(value, allow_none = True),
    help='Applicable fiboa extensions as URLs. Can map a remote fiboa extension schema url to a local file by adding a local file path, separated by a comma. Example: https://example.com/schema.json,/path/to/schema.json',
)
@click.option(
    '--fiboa-version', '-f',
    type=click.STRING,
    help=f'The applicable fiboa version if no collection is provided. Defaults to {fiboa_version_}.',
    default=fiboa_version_
)
def create_geoparquet(files, out, collection, schema, ext_schema, fiboa_version):
    """
    Create a fiboa GeoParquet file from GeoJSON file(s).

    The collection metadata has the following priority order:
    1. Read from the last GeoJSON file/feature (embedded 'fiboa' property)
    1. Read from the last GeoJSON file/feature (link with relation type 'collection')
    2. Read from the collection parameter
    3. Use fiboa_version and extension_schemas parameters
    """
    log(f"fiboa CLI {__version__} - Create GeoParquet\n", "success")
    config = {
        "files": files,
        "out": out,
        "schema": schema,
        "collection": collection,
        "extension_schemas": ext_schema,
        "fiboa_version": fiboa_version
    }
    create_geoparquet_(config)
    # try:
    #     create_geoparquet_(config)
    # except Exception as e:
    #     log(e, "error")
    #     sys.exit(1)


## CREATE GEOJSON
@click.command()
@click.argument('file', nargs=1, callback=lambda ctx, param, value: valid_file_for_cli_with_ext(value, ["parquet", "geoparquet"]))
@click.option(
    '--out', '-o',
    type=click.Path(exists=False),
    help='Folder to write the files to.',
    required=True
)
@click.option(
    '--features', '-f',
    is_flag=True,
    type=click.BOOL,
    help='Create seperate GeoJSON Feature files.',
    default=False
)
@click.option(
    '--num', '-n',
    type=click.IntRange(min=1),
    help='Number of features to export. Defaults to all.',
    default=None
)
@click.option(
    '--indent', '-i',
    type=click.IntRange(min=0, max=8),
    help='Indentation for JSON files. Defaults to no indentation.',
    default=None
)
def create_geojson(file, out, features = False, num = None, indent = None):
    """
    Create a fiboa GeoJSON file(s) from a fiboa GeoParquet file
    """
    log(f"fiboa CLI {__version__} - Create GeoJSON\n", "success")
    try:
        create_geojson_(file, out, features, num, indent)
        abs_path = os.path.abspath(out)
        log(f"Files written to {abs_path}", "success")
    except Exception as e:
        log(e, "error")
        sys.exit(1)


## JSON SCHEMA
@click.command()
@click.option(
    '--schema', '-s',
    type=click.STRING,
    callback=valid_file_for_cli,
    help='fiboa Schema to create the JSON Schema for. Can be a local file or a URL. If not provided, uses the fiboa version to load the schema for the released version.'
)
@click.option(
    '--out', '-o',
    type=click.Path(exists=False),
    help='File to write the file to. If not provided, prints the file to the STDOUT.',
    default=None
)
@click.option(
    '--fiboa-version', '-f',
    type=click.STRING,
    help=f'The fiboa version to validate against. Defaults to {fiboa_version_}.',
    default=fiboa_version_
)
@click.option(
    '--id', '-i', 'id_',
    type=click.STRING,
    help='The JSON Schema $id to use for the schema. If not provided, the $id will be omitted.',
)
def jsonschema(schema, out, fiboa_version, id_):
    """
    Create a JSON Schema for a fiboa Schema
    """
    log(f"fiboa CLI {__version__} - Create JSON Schema\n", "success")
    config = {
        "schema": schema,
        "fiboa_version": fiboa_version,
        "id": id_,
    }
    try:
        schema = jsonschema_(config)
        if out:
            with open(out, 'w', encoding='utf-8') as f:
                json.dump(schema, f, indent=2)
        else:
            print(schema)
    except Exception as e:
        log(e, "error")
        sys.exit(1)


## CONVERT
@click.command()
@click.argument('dataset', nargs=1)
@click.option(
    '--out', '-o',
    type=click.Path(exists=False),
    help='File to write the GeoParquet file to.',
    required=True
)
@click.option(
    '--cache', '-c',
    type=click.Path(exists=False),
    help='For network requests: Local cache file to store the downloaded file to avoid multiple downloads.',
    default=None
)
@click.option(
    '--source-coop', '-h',
    type=click.STRING,
    help='(Future) URL to the source cooperative repository, will be added to the Collection metadata.',
    default=None
)
@click.option(
    '--collection',
    is_flag=True,
    type=click.BOOL,
    help='Export a Collection JSON alongside the data file.',
    default=False
)
def convert(dataset, out, cache, source_coop, collection):
    """
    Converts existing field boundary datasets to fiboa.
    """
    log(f"fiboa CLI {__version__} - Convert '{dataset}'\n", "success")
    try:
        convert_(dataset, out, cache, source_coop, collection)
    except Exception as e:
        log(e, "error")
        sys.exit(1)


## RENAME EXTENSION
@click.command()
@click.argument('folder', nargs=1, callback=valid_folder_for_cli)
@click.option(
    '--title', '-t',
    type=click.STRING,
    help='Title of the extension, e.g. `Timestamps`',
    required=True
)
@click.option(
    '--slug', '-s',
    type=click.STRING,
    help='Slug of the repository, e.g. for `https://github.com/fiboa/timestamps-extension` it would be `timestamps-extension`',
    required=True
)
@click.option(
    '--org', '-o',
    type=click.STRING,
    help='Slug of the GitHub Organization. Defaults to `fiboa`',
    default="fiboa"
)
@click.option(
    '--prefix', '-p',
    type=click.STRING,
    help='Prefix for the field, e.g. `time` if the fields should be `time:created` or `time:updated`. An empty string removed the prefix, not providing a prefix leaves it as is.',
    default=None
)
def rename_extension(folder, title, slug, org = "fiboa", prefix = None):
    """
    Updates placeholders in an extension folder to the new name.
    """
    log(f"fiboa CLI {__version__} - Rename placeholders in extensions\n", "success")
    try:
        rename_extension_(folder, title, slug, gh_org=org, prefix=prefix)
    except Exception as e:
        log(e, "error")
        sys.exit(1)


cli.add_command(describe)
cli.add_command(validate)
cli.add_command(validate_schema)
cli.add_command(create_geoparquet)
cli.add_command(create_geojson)
cli.add_command(jsonschema)
cli.add_command(convert)
cli.add_command(rename_extension)

if __name__ == '__main__':
    cli()
