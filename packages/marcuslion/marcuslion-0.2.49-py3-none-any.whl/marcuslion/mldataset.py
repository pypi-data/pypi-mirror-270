import pandas as pd

from marcuslion.restcontroller import RestController

IS_BACKEND_PARAM = 'is_backend'


class MlDatasets(RestController):
    """
    MarcusLion User dataset class
    """

    def __init__(self):
        super().__init__("/ml-datasets")

    def list(self, params=None) -> pd.DataFrame:
        """
        Datasets.list()
        """
        if params is None:
            params = {}
        params[IS_BACKEND_PARAM] = True
        data = super().verify_get("", params)
        if data is None:
            return pd.DataFrame()
        return pd.DataFrame(data)

    def download(self, dataset_id, output_path=None) -> any:
        """
        Datasets.download(ref)
        """
        print(f"Downloading ...")
        return super().download_file("/download/" + dataset_id, {
            IS_BACKEND_PARAM: True
        }, output_path)
