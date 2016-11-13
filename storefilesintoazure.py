from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

def saveFile():
    mykey = "UGMnwCrlJ5IJB9maLEThvKHbU4MkDnoPNXk9LFrJPkXIX5LR47tU7yPAWS6Zh3OC8h1xd/tYetCfpLC/a8fv8g=="
    myaccount = 'reactonfly'
    mycontainer = 'images'
    for i in range(0,5):
        block_blob_service = BlockBlobService(account_name=myaccount, account_key=mykey)
        block_blob_service.create_container(mycontainer, public_access=PublicAccess.Container)
        block_blob_service.create_blob_from_path(mycontainer,'myblockblob'+str(i), 'filename'+str(i)+'.jpg' ,content_settings=ContentSettings(content_type='image/png'))
