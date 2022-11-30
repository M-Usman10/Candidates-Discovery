import weaviate
from app.configs.constants import CONFIG_FILE


class Weaviate:

    def connect_weaviate(self):
        """
        Create client of waviate
        Returns:
            client: waviate client
        """
        try:
            waviate_client = weaviate.client(CONFIG_FILE["CLUSTER_URL"])
            print("Successfully created weaviate client")
            return waviate_client
        except Exception as e:
            print("Error while creating connection")
