import json

# from trophy_contract_interactor import get_metadata


def lambda_handler(event, context):
    print(event)
    
    type = ''
    token_id = ''
    
    if 'pathParameters' in event:
        params = event['pathParameters']

        if 'type' in params:
            type = params['type']
        if 'tokenId' in params:
            token_id = params['tokenId']

    if type == 'metadata':
      result = {
        "image": f"https://1hzjyv5tlg.execute-api.us-west-1.amazonaws.com/trophy/image/{token_id}", 
        "league_name": "The League"
      }
    elif type == 'image':
      result = f"Generating image for token id: {token_id}"
    else:
      result = f"Doing nothing!"

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
