import json
import re
import boto3


hashtags_list=[]
def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('postshashtag')
    
    # TODO implement
    print(event.get('post'))
    print(event.get('post_id'))
    post_id=event.get('post_id')
    post=event.get('post')
    for word in post.split():
        if word[0] == '#':
            hashtags_list.append(word[1:])
    print("h1",hashtags_list)
    item = {
        'post_id': post_id,
        'post': post,
        'hashtag': hashtags_list
    }
    result=table.put_item(Item=item)
    return result
