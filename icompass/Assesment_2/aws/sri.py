import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
# logger.setLevel(logging.info)

#define table 
dynamoTable = "sri_crud"
dynamo = boto3.resource('dynamodb')
table = dynamo.Table(dynamoTable)

def main():
    id = 0
    
    # save
    requestbody = {
        'id':id,
        'email':"sri@gmail.com",
        'firstname':'Sridhar',
        'lastname':'S'
    }
    response = saveId(requestbody)
    logger.info(response)
    
    # get
    response = getId(id)
    logger.info(response)

    

    # delete
    # response = delete(id)
    # logger.ifo(response)

    return response

def delete(id):
    response = table.delete_item(
        key = {
            'id':id
        }
    )

    body = {
        'operation':'DELETE',
        'message':'SUCCESS',
        'Item':id
    }

    return body

def saveId(requestbody):

    try:
        table.put_item(Item=requestbody)
        body = {
            'operation':'SAVE',
            'message':'SUCCESS',
            'Item':requestbody
        }
        return body
    
    except:
        logger.exception("Error handling .. ")

def getId(id):
    response = table.get_item(
        key = {
            'id':id
        }
    )

    if 'email' in response:
        return response['email']
    else:
        return {"Msg":f"Email id {id} is not foun"}

main()