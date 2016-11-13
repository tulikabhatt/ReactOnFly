from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

def saveFile():
    mykey = "######"
    myaccount = 'reactonfly'
    mycontainer = 'images'
    for i in range(0,5):
        block_blob_service = BlockBlobService(account_name=myaccount, account_key=mykey)
        block_blob_service.create_container(mycontainer, public_access=PublicAccess.Container)
        block_blob_service.create_blob_from_path(mycontainer,'myblockblob'+str(i), 'filename'+str(i)+'.jpg' ,content_settings=ContentSettings(content_type='image/png'))
