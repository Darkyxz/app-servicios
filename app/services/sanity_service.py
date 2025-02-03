import requests
from config import Config

class SanityService:
    def __init__(self):
        self.project_id = Config.SANITY_PROJECT_ID
        self.dataset = Config.SANITY_DATASET
        self.token = Config.SANITY_TOKEN
        self.url = f"https://{self.project_id}.api.sanity.io/v1/data/mutate/{self.dataset}"
        self.assets_url = f"https://{self.project_id}.api.sanity.io/v1/assets/images/{self.dataset}"
        self.query_url = f"https://{self.project_id}.api.sanity.io/v1/data/query/{self.dataset}"

    def create_schema_reference(self):
        schema_reference = {
            "_type": "schema_reference",
            "name": "article",
            "fields": [
                {"name": "title", "type": "string"},
                {"name": "description", "type": "text"},
                {"name": "price", "type": "number"},
                {"name": "quantity", "type": "number"},
                {"name": "image_url", "type": "string"},
                {"name": "owner_username", "type": "string"}
            ]
        }

        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        mutation = {
            "mutations": [
                {
                    "create": schema_reference
                }
            ]
        }

        response = requests.post(self.url, json=mutation, headers=headers)
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error creating schema reference: {response.text}")

    def upload_image(self, file):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        files = {'file': file}
        response = requests.post(self.assets_url, files=files, headers=headers)
        if response.status_code == 200:
            return response.json()['url']  # Devuelve la URL de la imagen subida
        else:
            raise Exception(f"Error uploading image: {response.text}")

    def create_article(self, article):
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        mutation = {
            "mutations": [
                {
                    "create": {
                        "_type": "article",
                        **article.to_dict()
                    }
                }
            ]
        }
        response = requests.post(self.url, json=mutation, headers=headers)
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error creating article: {response.text}")

    def get_articles(self):
        query = '*[_type == "article"]{title, description, price, quantity, image_url, owner_username}'
        response = requests.get(
            f"{self.query_url}?query={query}",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if response.status_code == 200:
            return response.json()['result']
        else:
            raise Exception(f"Error fetching articles: {response.text}")

    def get_articles_by_user(self, username):
        query = f'*[_type == "article" && owner_username == "{username}"]{{title, description, price, quantity, image_url}}'
        response = requests.get(
            f"{self.query_url}?query={query}",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if response.status_code == 200:
            return response.json()['result']
        else:
            raise Exception(f"Error fetching articles by user: {response.text}")