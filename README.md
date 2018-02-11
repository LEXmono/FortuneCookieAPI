# Fortune Cookie API

This is just a pet project to play with and learn about AWS Chalice, A microservice framework for AWS. More can be found at the Chalice website https://chalice.readthedocs.io/en/latest/#.

## Getting Started

These instructions will get you a copy of the project up and running.

### Prerequisites

To get started, you need to have git, python3.6, and pip3 installed, and then install the modules in requirements.txt.

```
git clone https://github.com/LEXmono/FortuneCookieAPI.git
cd fortunecookie
pip3 -r requirements.txt

```

#### AWS Resources
* Make two DynamoDB tables in a region of your choice. They should be named `fortunecookie-dev` and `fortunecookie-prod` (OR you have to change these values in the config later.)
* Make an IAM user and download the credentials.
* Use `aws configure` to set up these credentials.

### Installing

You will need to create a config file to be able to run the API which lives in the `.chalice` directory which is located in the root of the project.

`/.chalice/config.json`

```
{
  "version": "2.0",
  "app_name": "fortunecookie",
  "environment_variables": {
    "APP_NAME": "fortunecookie",
    "SITE_FALLBACK": "https://yoursite/"
  },
  "stages": {
    "dev": {
      "api_gateway_stage": "dev",
      "region": "us-east-2",
      "environment_variables": {
        "DYNAMO_TABLE": "fortunecookie-dev"
      }
    },
    "prod": {
      "api_gateway_stage": "api",
      "region": "us-east-2",
      "environment_variables": {
        "DYNAMO_TABLE": "fortunecookie-prod"
      }
    }
  }
}
```

You can now deploy the API using `chalice deploy --stage dev` NOTE: Dev here comes from the stage defined in yout config.json. The output should look like the following and return your API URL.

```
(fortunecookie) mhenry: ~/virtualenvs/fortunecookie/fortunecookie
=> chalice deploy --stage dev
Regen deployment package.
Updating IAM policy for role: fortunecookie-dev
Updating lambda function: fortunecookie-dev
API Gateway rest API already found: 2mvwjcenw2
Deploying to API Gateway stage: dev
https://REDACTED.execute-api.us-east-2.amazonaws.com/dev/
```

And if you have fortunes in your DynamoDB table, you should get back a fortune by going to https://REDACTED.execute-api.us-east-2.amazonaws.com/dev/fortune


## Built With

* [Chalice](https://aws.amazon.com/blogs/developer/chalice-1-0-0-ga-release/) - The web framework used
* [DynamoDB](https://aws.amazon.com/dynamodb/) - Key Value Store for fortunes

## Authors

* **Michael Henry** - *Initial work* - [LEXmono](https://github.com/LEXmono)

See also the list of [contributors](https://github.com/LEXmono/FortuneCookieAPI/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

