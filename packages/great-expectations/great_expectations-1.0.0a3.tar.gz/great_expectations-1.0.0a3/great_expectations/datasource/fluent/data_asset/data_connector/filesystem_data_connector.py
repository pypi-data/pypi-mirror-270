from __future__ import annotations

import logging
import pathlib
import re
from typing import TYPE_CHECKING, Callable, ClassVar, List, Optional, Type

from great_expectations.compatibility import pydantic
from great_expectations.compatibility.typing_extensions import override
from great_expectations.datasource.data_connector.util import (
    get_filesystem_one_level_directory_glob_path_list,
    normalize_directory_path,
)
from great_expectations.datasource.fluent.data_asset.data_connector import (
    FilePathDataConnector,
)

if TYPE_CHECKING:
    from great_expectations.alias_types import PathStr

logger = logging.getLogger(__name__)


class FilesystemOptions(pydantic.BaseModel):
    glob_directive: str = "**/*"


class FilesystemDataConnector(FilePathDataConnector):
    """Extension of FilePathDataConnector used to connect to Filesystem (local, networked file storage (NFS), DBFS, etc.).

    Args:
        datasource_name: The name of the Datasource associated with this DataConnector instance
        data_asset_name: The name of the DataAsset using this DataConnector instance
        batching_regex: A regex pattern for partitioning data references
        base_directory: Relative path to subdirectory containing files of interest
        glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
        data_context_root_directory: Optional GreatExpectations root directory (if installed on filesystem)
        whole_directory_path_override: Treat an entire directory as a single Asset
    """  # noqa: E501

    asset_level_option_keys: ClassVar[tuple[str, ...]] = ("glob_directive",)
    asset_options_type: ClassVar[Type[FilesystemOptions]] = FilesystemOptions

    def __init__(  # noqa: PLR0913
        self,
        datasource_name: str,
        data_asset_name: str,
        batching_regex: re.Pattern,
        base_directory: pathlib.Path,
        glob_directive: str = "**/*",
        data_context_root_directory: Optional[pathlib.Path] = None,
        file_path_template_map_fn: Optional[Callable] = None,
        whole_directory_path_override: PathStr | None = None,
    ) -> None:
        self._base_directory = base_directory
        self._glob_directive: str = glob_directive
        self._data_context_root_directory: Optional[pathlib.Path] = data_context_root_directory

        super().__init__(
            datasource_name=datasource_name,
            data_asset_name=data_asset_name,
            batching_regex=batching_regex,
            file_path_template_map_fn=file_path_template_map_fn,
            whole_directory_path_override=whole_directory_path_override,
        )

    @property
    def base_directory(self) -> pathlib.Path:
        """
        Accessor method for base_directory. If directory is a relative path, interpret it as relative to the
        root directory. If it is absolute, then keep as-is.
        """  # noqa: E501
        return normalize_directory_path(
            dir_path=self._base_directory,
            root_directory_path=self._data_context_root_directory,
        )

    @classmethod
    def build_data_connector(  # noqa: PLR0913
        cls,
        datasource_name: str,
        data_asset_name: str,
        batching_regex: re.Pattern,
        base_directory: pathlib.Path,
        glob_directive: str = "**/*",
        data_context_root_directory: Optional[pathlib.Path] = None,
        file_path_template_map_fn: Optional[Callable] = None,
        whole_directory_path_override: PathStr | None = None,
    ) -> FilesystemDataConnector:
        """Builds "FilesystemDataConnector", which links named DataAsset to filesystem.

        Args:
            datasource_name: The name of the Datasource associated with this "FilesystemDataConnector" instance
            data_asset_name: The name of the DataAsset using this "FilesystemDataConnector" instance
            batching_regex: A regex pattern for partitioning data references
            base_directory: Relative path to subdirectory containing files of interest
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            data_context_root_directory: Optional GreatExpectations root directory (if installed on filesystem)
            file_path_template_map_fn: Format function mapping path to fully-qualified resource on filesystem (optional)
            get_unfiltered_batch_definition_list_fn: Function used to get the batch definition list before filtering

        Returns:
            Instantiated "FilesystemDataConnector" object
        """  # noqa: E501
        return FilesystemDataConnector(
            datasource_name=datasource_name,
            data_asset_name=data_asset_name,
            batching_regex=batching_regex,
            base_directory=base_directory,
            glob_directive=glob_directive,
            data_context_root_directory=data_context_root_directory,
            file_path_template_map_fn=file_path_template_map_fn,
            whole_directory_path_override=whole_directory_path_override,
        )

    @classmethod
    def build_test_connection_error_message(  # noqa: PLR0913
        cls,
        data_asset_name: str,
        batching_regex: re.Pattern,
        base_directory: pathlib.Path,
        glob_directive: str = "**/*",
        data_context_root_directory: Optional[pathlib.Path] = None,
    ) -> str:
        """Builds helpful error message for reporting issues when linking named DataAsset to filesystem.

        Args:
            data_asset_name: The name of the DataAsset using this "FilesystemDataConnector" instance
            batching_regex: A regex pattern for partitioning data references
            base_directory: Relative path to subdirectory containing files of interest
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            data_context_root_directory: Optional GreatExpectations root directory (if installed on filesystem)

        Returns:
            Customized error message
        """  # noqa: E501
        test_connection_error_message_template: str = 'No file at base_directory path "{base_directory}" matched regular expressions pattern "{batching_regex}" and/or glob_directive "{glob_directive}" for DataAsset "{data_asset_name}".'  # noqa: E501
        return test_connection_error_message_template.format(
            **{
                "data_asset_name": data_asset_name,
                "batching_regex": batching_regex.pattern,
                "base_directory": base_directory.resolve(),
                "glob_directive": glob_directive,
                "data_context_root_directory": data_context_root_directory,
            }
        )

    # Interface Method
    @override
    def get_data_references(self) -> List[str]:
        base_directory: pathlib.Path = self.base_directory
        glob_directive: str = self._glob_directive
        path_list: List[str] = get_filesystem_one_level_directory_glob_path_list(
            base_directory_path=base_directory, glob_directive=glob_directive
        )
        return sorted(path_list)

    # Interface Method
    @override
    def _get_full_file_path(self, path: str) -> str:
        return str(self.base_directory.joinpath(path))
