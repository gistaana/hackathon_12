from secret import FIREBASE_ROOT_COLLECTION_NAME

# load in public secrets
from dotenv import load_dotenv
from os import getenv

# connect to database
import firebase_admin 
from firebase_admin import firestore, credentials

# using this to provide type suggestions
from google.cloud.firestore import Client as Firestore
from google.cloud.firestore_v1.document import DocumentSnapshot

from typing import List

class FirebaseConnection():
    """`FirebaseConnection` provides a set of functions to communicate with the predefined database based on app secrets.
    It uses `firestore` to do so. [SYNC] 
    """
    def __init__(self) -> None:
        cred = credentials.Certificate("fb_secrets.json")
        # init firebase connection via secrets file
        firebase_admin.initialize_app(cred)
        # get ref to databse
        db: Firestore = firestore.client()

        if FIREBASE_ROOT_COLLECTION_NAME is None: raise ValueError("FIREBASE_ROOT_COLLECTION_NAME env var is not defined")

        self.email_collection = db.collection(FIREBASE_ROOT_COLLECTION_NAME)


    def get_all_email_data(self):
        collection_docs: List[DocumentSnapshot] = self.email_collection.get()
        
        return [docs.to_dict() for docs in collection_docs]




print(FirebaseConnection().get_all_email_data())