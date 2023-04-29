import boto3 
client = boto3.client('drs')

def start_recovery_latest(SourceId,IsDrill):
    response = client.start_recovery(
        isDrill= IsDrill,
        sourceServers=[
            {
                'sourceServerID': SourceId
            
            }
        ]
        )
    return (response)
    
def start_recovery_PIT(SourceId,IsDrill,snapshot_Id):
    response = client.start_recovery(
        isDrill= IsDrill,
        sourceServers=[
            {
                'recoverySnapshotID' : snapshot_Id,
                'sourceServerID': SourceId
            
            }
        ]
        )
    return (response)
