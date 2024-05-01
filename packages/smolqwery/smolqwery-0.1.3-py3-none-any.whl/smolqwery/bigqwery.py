from typing import Dict, Iterator, Optional
from unittest.mock import MagicMock

from google.cloud import bigquery
from google.oauth2 import service_account

from ._utils import ChunkIterator
from .config import BaseConfigProvider, default_settings


class MockClient:
    project = "mock"

    create_dataset = MagicMock()

    create_table = MagicMock()

    query = MagicMock()


class BigQwery:
    """
    Utility wrapper around Google's Big Query
    """

    INSERT_CHUNK_SIZE = 1000

    def __init__(self, settings: BaseConfigProvider = None):
        self.settings: BaseConfigProvider = settings if settings else default_settings
        self._client = None

    @property
    def client(self) -> bigquery.Client:
        """
        Generates the client from the credentials and returns/caches it
        """

        if not self._client:
            if getattr(self.settings, "google_mock", False):
                self._client = MockClient()
            else:
                self._client = bigquery.Client(credentials=self.get_credentials())

        return self._client

    def get_credentials(self):
        """
        Generates the credentials from config
        """

        return service_account.Credentials.from_service_account_info(
            self.settings.get_credentials_data()
        )

    def get_dataset_id(self, name: str = "") -> str:
        """
        Generates the ID of the dataset (the default one from settings by
        default, or the specified one instead).

        Parameters
        ----------
        name
            Optional name of the dataset (if not specified, the one from the
            settings will be used).
        """

        if not name:
            name = self.settings.dataset

        return f"{self.client.project}.{name}"

    def get_table_id(self, name: str, dataset_name: str = "") -> str:
        """
        Returns the ID of a table from its name

        Parameters
        ----------
        name
            Name of the table
        dataset_name
            Name of the dataset containing the table
        """

        return f"{self.get_dataset_id(dataset_name)}.{name}"

    def get_delta_view_id(self, table_name: str, dataset_name: str = "") -> str:
        """
        Computes the ID of a "delta view" based on a specific table

        Parameters
        ----------
        table_name
            Name of the table onto which the view is based
        dataset_name
            Name of the dataset holding the table
        """

        return f"{self.get_table_id(table_name, dataset_name)}_delta"

    def insert_rows(
        self,
        table_name: str,
        rows: Iterator[Dict],
        dataset_name: str = "",
        insert_chunk_size: Optional[int] = None,
    ) -> None:
        """
        Inserts some rows into the BigQuery table

        Parameters
        ----------
        table_name
            Name of the table (ID will be computed automatically)
        rows
            Iterator of rows (they will automatically be inserted by batches
            of 1000, unless you change the insert_chunk_size).
        dataset_name
            If set, inserts the data into this dataset instead of the default
            one.
        insert_chunk_size
            Number of rows to insert at once. Default makes sense, change only
            if you reach some limits.
        """

        if insert_chunk_size is None:
            insert_chunk_size = self.INSERT_CHUNK_SIZE

        for chunk in ChunkIterator(rows).chunks(insert_chunk_size):
            errors = self.client.insert_rows_json(
                self.get_table_id(table_name, dataset_name), chunk
            )

            if errors:
                errors_str = f"{errors}"[:1000]

                raise Exception(f"Insertion error: {errors_str}")
