# Cloud Status Dashboard (AWS Final Project)

Cloud web application deployed in **Asia Pacific (Sydney) `ap-southeast-2`** using **Amazon S3**, **AWS Lambda**, **Amazon API Gateway**, and **AWS IAM**.

## Architecture
```text
[ Browser ] --(HTTP Static Site)--> [ Amazon S3 ]
     |
     +---------(HTTPS GET)---------> [ Amazon API Gateway ] --> [ AWS Lambda (Python 3.12) ]
                                                                       |
                                                               (IAM Execution Role)
