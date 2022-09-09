
# AnnouncementApp

### Utility:

You can **create new announcements**.

You can **read all existing announcements from message queue**.

___
### Setup:

1) To run an application you shound have 🐍 ***python*** version => "3.9" installed.
2) Install ***pipenv*** for creating virtual environment `pip install --user pipenv`
3) Run `pip install` in main directory to install requirements from `Pipfile`
4) Create ***AWS SQS*** via `aws console` all info in https://aws.amazon.com/sqs/
5) Create `.env` and set all needed secrets:
  * AWS_ACCESS_KEY_ID=
  * AWS_SECRET_ACCESS_KEY=
  * QUEUE_URL=
6) Start server via `terminal` runnung special script `/set_and_start_server.sh`


## API Reference

#### Create an announcement 

```http
  POST /api/announcement
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. An announcement title |
|`description`|`string`||**Required**. An announcement description |
|`date`|`string (date)`||**Required**. Creation date |

###### Response code -> 201 

#### Get all existing announcements

```http
  GET /api/announcements
```
#### Response example
| Response| Type     | Description                |
| :-------- | :------- | :------------------------- |
| `200` | `JSON` | JSON representation of all existing announcements|
 `200` | `list` | Returns an empty list in case if there are no available announcements|

***Documentation is available on `/docs`***  
