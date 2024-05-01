import os
import mysql.connector
from dotenv.main import load_dotenv
load_dotenv()


class StorageDB:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host=os.getenv("RDS_HOSTNAME"),
            user=os.getenv("RDS_USERNAME"),
            password=os.getenv("RDS_PASSWORD"),
            database="storage"
        )
        self.cursor = self.mydb.cursor(buffered=True)

    # TODO Remote created_user_id parameter and use user-context.get_effective_profile_id()
    # TODO Add types to all parameters in all methods/functions.
    def uploadToDatabase(self, file_path, filename,  region, created_user_id, storage_type_id, file_type_id,
                         extension_id, url: str = None) -> int:
        add_storage = ("INSERT INTO storage.storage_table "
                       "(path, filename, region, url, created_user_id, updated_user_id, storage_type_id, file_type_id,"
                       " file_extension_id) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        storage_data = (file_path, filename, region, url, created_user_id,
                        created_user_id, storage_type_id, file_type_id, extension_id)
        # Replace last_insert_id with storage_id evertwhere
        self.cursor.execute(add_storage, storage_data)
        self.mydb.commit()
        select_stmt = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(select_stmt)
        last_insert_id = self.cursor.fetchone()[0]
        return int(last_insert_id)

    def closeConnection(self):
        if (self.mydb != None):
            self.mydb.close

    # TODO: change this method to delete()
    def logicalDelete(self, remote_path, filename, region, updated_user_id) -> int:
        select_stmt = "SELECT storage_id FROM storage.storage_view WHERE path = %s AND filename = %s AND region = %s"
        select_data = (remote_path, filename, region)
        self.cursor.execute(select_stmt, select_data)
        id = self.cursor.fetchone()
        if id is None:
            return None
        id = id[0]
        self.cursor.nextset()
        update_stmt = "UPDATE storage.storage_table SET end_timestamp = NOW(), updated_timestamp = NOW(), " \
                      "updated_user_id = %s WHERE path = %s AND filename = %s AND region = %s"
        update_data = (updated_user_id, remote_path, filename, region)
        self.cursor.execute(update_stmt, update_data)
        self.mydb.commit()
        return int(id)

    def getEndTimeStampFromDB(self, remote_path, filename, region):
        update_stmt = "SELECT end_timestamp FROM storage.storage_view WHERE path = %s AND filename = %s AND region = %s"
        update_data = (remote_path, filename, region)
        self.cursor.execute(update_stmt, update_data)
        return self.cursor.fetchone()

    def getLastId(self) -> int:
        select_stmt = "SELECT storage_id FROM storage.storage_view ORDER BY storage_id DESC LIMIT 1"
        self.cursor.execute(select_stmt)
        last_insert_id = self.cursor.fetchone()[0]
        return int(last_insert_id)
