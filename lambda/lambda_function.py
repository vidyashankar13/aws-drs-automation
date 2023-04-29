import json
import boto3
from drs import *
import logging

#Logger Initialization
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Boto3 Client initialization
client = boto3.client('drs')

def lambda_handler(event, context):
    
    #Fetching the inputs:
    Sourceserver = event['SourceId']
    IsDrill = eval(event['IsDrill'])
    
    # Start Recovery
    if event['Snapshot_Id']:
        Snap_Id = event['Snapshot_Id'] # snapshot ID
        logger.info('Getting Sourceserver Id - '+ event['SourceId'])
        logger.info('Is this recovery Drill - ' + event['IsDrill'])
        logger.info('PIT Recovery Snapshot_Id - ' + event['Snapshot_Id'])
        try:
            logger.info('Initialization of DRS Recovery from PIT Snapshot')
            rec = start_recovery_PIT(Sourceserver,IsDrill,Snap_Id)
        except Exception as E :
            logger.error(E)
            return E
        return rec
    logger.info('Getting Sourceserver Id - '+ event['SourceId'])
    logger.info('Is this recovery Drill - '+ event['IsDrill'])
    try:
        logger.info('Initialization of DRS Recovery from latest snapshot')
        rec = start_recovery(Sourceserver,IsDrill)
    except Exception as E:
        logger.error (E)            
        return (E)
    return (rec)
