from circles_local_aws_s3_storage_python.FileTypeDB import file_type_db
import os
import sys
from circles_local_aws_s3_storage_python.AWSStorage import AwsS3Storage
try:
    # Works when running the tests from this package
    from StorageConstants import *  # noqa: E402
except Exception:
    # Works when importing this module from another package
    from circles_local_aws_s3_storage_python.StorageConstants import *
from dotenv.main import load_dotenv
load_dotenv()
import re   # noqa: E402
from logger_local.Logger import Logger  # noqa: E402
import requests  # noqa: E402
import shutil   # noqa: E402


CLASS_NAME = "CirclesStorage"

# TODO: We should delete this paragraph and use a logger.debug_mode method to check if debug enabled
os_debug = os.getenv('DEBUG')
if (os_debug == 'True' or os_debug == '1'):
    debug = True
else:
    debug = False
if (debug):
    print("storage-local-python-package " + CLASS_NAME + " debug is on.")


class circles_storage:

    def __init__(self, test=False):
        if (debug): print("storage-local-python-package AWS_DEFAULT_REGION:"+str(os.getenv("AWS_DEFAULT_REGION")))
        self.s3 = AwsS3Storage(os.getenv("AWS_DEFAULT_STORAGE_BUCKET_NAME"), os.getenv("AWS_DEFAULT_REGION"))
        self.db = file_type_db()
        self.test = test
        # TODO self.logger = ...
        self.lgrins = Logger.create_logger(object=OBJECT_TO_INSERT_CODE)
        self.lgrins.init({'component_id':"13"})
        self.system_check()

    # returns the folder name from DB according to entity_type_id
    # TODO rename the method to _get_file_type_by_file_type_id(self, file__type_id):
    # TODO Add parameter's types to all methods/functions
    def _get_folder(self, entity_type_id):
        select_stmt = "SELECT file_type FROM storage.file_type_view WHERE file_type_id = %s"
        select_data = (entity_type_id)
        return self.db.select_from_DB(select_stmt, select_data)

    # TODO _get_region_and_folder_by_profile_id_entity_id()
    def _get_region_and_folder(self, profile_id, entity_type_id):
        folder = self._get_folder(entity_type_id)
        # Replace with a new method in user-context: region = user-context.get_effective_region()
        region = os.getenv("AWS_DEFAULT_REGION")
        return [folder, region]

    #
    def put(self, profile_id, entity_type_id, filename, local_file_path):
        """uploads a file from the local computer to S3 and returns the storage_id of the file in the storage DB

        Args:
            profile_id int: user ID
            file_type_id int: type of the file - 
                                1 - Profile Image
                                2 - Coverage Image
                                3 - Personal Introduction Video
                                4 - Scanned Diving License 
                                5 - Scanned Passport
            filename string: file name including extension, i.e test.txt
            local_file_path string: path to the file location, i.e. path/to/file/
        Returns:
            int: ID of the file in the storage DB
        """
        folder_and_region = self._get_region_and_folder(
            profile_id, entity_type_id)
        # TODO I think we should rename file_database_id to storage_id
        file_database_id = self.s3.upload_file(local_file_path, filename,
                                               folder_and_region[0]+'/', profile_id)
        return file_database_id


    # TODO Shall we call it preserve_letters or preserved_string? - Let's be consistent
    def preserve_letters(self,input_string):
        """Preserves only letters and spaces in a given string

        Args:
            input_string string: unmodified string
        """
        # Use a regular expression to match only letters (A-Z and a-z)
        pattern = r"[^a-zA-Z\s]"
        preserved_string = re.sub(pattern, "", input_string)
        return preserved_string


    # TODO destination or target_directory
    def download_by_storage_id(self, storage_id, destination=os.getcwd()):
        """Downlaods file from S3 to the local computer using only storage id

        Args:
            storage_id int: Row number to get information from storage_table
        """
        select_stmt = "SELECT created_user_id, path, filename FROM storage.storage_view WHERE storage_id = %s"
        select_data = (storage_id)
        self.db.cursor.execute(select_stmt, [select_data])
        profile_id, folder, filename = self.db.cursor.fetchall()[0]
        path_local = os.path.join(destination, filename)
        self.s3.download_file(folder + filename, path_local)
        return path_local
        
    def system_check(self):
        """Checking for Credentials-based errors"""
        # TODO replace with logger.start()
        self.lgrins.start()
        if os.getenv("AWS_DEFAULT_STORAGE_BUCKET_NAME") is None:
            self.lgrins.critical("AWS_DEFAULT_STORAGE_BUCKET_NAME not specified in .env, please add")
            sys.exit('storage-local-python-package AWS_DEFAULT_STORAGE_BUCKET_NAME not defined')
        if os.getenv("AWS_DEFAULT_REGION") is None:
            self.lgrins.critical("AWS_DEFAULT_REGION not specified in .env, please add")
            sys.exit('storage-local-python-package AWS_DEFAULT_REGION not defined')
        try:
            cursor = self.db.cursor
        except:
            self.lgrings.critical("Unable to create cursor")
            sys.exit('storage-local-python-package Unable to create cursor')

        try:
            # TODO Is it mandatory to use DESCRIBE? Can we use Sql2Code?
            sql_query = f"DESCRIBE logger.logger_table"
            cursor.execute(sql_query)
            columns_info = cursor.fetchall()
            self.lgrins.info(columns_info)
        except:
            self.lgrins.critical("Unable to access logger.logger_table. Try confirming if user has access")
            sys.exit('storage-local-python-package Unable to create cursor')
        try:
            # TODO Is it mandatory? Can we use Sql2Code
            sql_query = f"DESCRIBE storage.storage_view"
            cursor.execute(sql_query)
            columns_info = cursor.fetchall()
            self.lgrins.info(columns_info)
        except:
           self.lgrins.critical("Unable to access storage.storage_table. Try confirming if user has access")
        self.lgrins.end()

    # TODO change entity_type_id to file_type_id every wheere
    def download(self, profile_id, entity_type_id, filename, local_path):
        """Downlaods file from S3 to local computer

        Args:
            file_type_id int: 1 - Profile Image
                                2 - Coverage Image
                                3 - Personal Introduction Video
                                4 - Scanned Diving License 
                                5 - Scanned Passport
            filename string: file name include extension, i.e test.txt
            local_path string: where to save the file, include file extension,
            i.e path/to/file/downloaded_test.txt
        """
        folder_and_region = self._get_region_and_folder(
            profile_id, entity_type_id)
        remote_file_path = folder_and_region[0]+'/'+filename
        self.s3.download_file(remote_file_path, local_path)

    def save_image_in_storage_by_url(self, image_url, local_filename, profile_id, entity_type_id):
        self.lgrins.start(object={'image_url': image_url, 'local_filename': local_filename, 'profile_id': profile_id,
                                  'entity_type_id': entity_type_id})
        folder_and_region = self._get_region_and_folder(
            profile_id, entity_type_id)
        cwd = os.getcwd()
        local_file_path = os.path.join(cwd, local_filename)
        remote_file_path = folder_and_region[0]+'/'
        response = requests.get(image_url, stream=True)

        # Check if the image was retrieved successfully
        if response.status_code == requests.codes.ok:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            response.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            
            self.s3.upload_file(local_file_path, local_filename, remote_file_path, profile_id, image_url)
            self.lgrins.end(object={'Image successfully downloaded: ': local_filename})
        else:
            self.lgrins.error('Image couldn\'t be retrieved')
