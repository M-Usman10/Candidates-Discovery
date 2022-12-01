import weaviate
from app.configs.constants import CONFIG


class Weaviate:

    def connect_weaviate(self):
        """
        Create client of waviate
        Returns:
            client: waviate client
        """
        try:

            waviate_client = weaviate.Client(CONFIG["CLUSTER_URL"])
            print("Successfully created weaviate client")
            return waviate_client
        except Exception as e:
            print("Error while creating connection")
