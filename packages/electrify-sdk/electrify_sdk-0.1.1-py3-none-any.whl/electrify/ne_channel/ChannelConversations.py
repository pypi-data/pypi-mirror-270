from dotenv import load_dotenv
import os
from electrify.ne_channel.chatwoot_client import ChatwootClient
from electrify.ne_channel.chatwoot_client.definitions.schemas.input_schemas import *

class ChannelConversations:
    def __init__(self):
        load_dotenv()  # Load environment variables
        self.url = os.getenv("CHATWOOT_URL")
        self.user_token = os.getenv("CHATWOOT_USER_TOKEN")
        self.account_id = os.getenv("CHATWOOT_ACCOUNT_ID")
        self.client = ChatwootClient(self.url, self.user_token)

    def fetch_conversations(self, inbox_id, mail_subject, page=1):
        """Fetch conversations filtered by inbox ID and mail subject."""
        payload = {
            "payload": [
                {
                    "attribute_key": "inbox_id",
                    "filter_operator": "equal_to",
                    "values": [inbox_id],
                    "query_operator": "AND"
                },
                {
                    "attribute_key": "mail_subject",
                    "filter_operator": "contains",
                    "values": [mail_subject],
                    "query_operator": None
                }
            ]
        }
        query_params = {"page": page}
        response = self.client.conversations.filter(account_id=self.account_id, query=query_params, payload=payload)
        return response

    def get_attachments(self, inbox_id, mail_subject):
        """Retrieve an array of attachments from all conversations in the specified inbox."""
        response = self.fetch_conversations(inbox_id, mail_subject)
        attachments = []
        if 'payload' in response:
            for conversation in response['payload']:
                for message in conversation['messages']:
                    if 'attachments' in message and message['attachments']:
                        attachments.extend(message['attachments'])
        return attachments
