# Overview

This creates a pipeline that can be used to deploy SAM templates.

The pipeline template creates the following resources:

- a bucket to store lambda function code for deployment
- a CodeCommit repository
- a CloudWatch event to monitor changes to the CodeCommit repository and trigger the pipeline
- A CodeBuild job to build the applicaiton based on your buildspec.yaml
- a CodePipeline as follows:

CodeCommit --> CodeBuild --> create CloudFormation changeset --> Execute CloudFormation template

# Creating the pipeline

The template to build the pipeline is code-pipeline.yaml

You can deploy the template via the UI or run the CLI:

*Note:* Edit the ParameterValue to be the name of your project

```
aws cloudformation create-stack --stack-name codepipeline-demo --template-body file://code-pipeline.yaml --parameters ParameterKey=ProjectName,ParameterValue="cjl-codepipeline" --capabilities CAPABILITY_NAMED_IAM
```

# Preparing the CodeCommit repository

- Clone the empty code commit repository to your machine.
- Add your SAM temnplate and buildspec.yaml, making sure you buildspec references the bucket name created during above, it can be seen in the CloudFormation output.
- Commmit the code and push it to master to start the pipeline.

# Example

This repo also contains an example that deploys a step function referencing two step functions. To deploy the sample run the following:

```
./MakeFile <bucket-name>
```

Copy the contents of exampleDeployment to your local repository.

```
cp -R exampleDeployment/* <your repo>
```

Change directory into your repository and run:

```
cd <your repo>
git add -A
git commit -m "example codedeploy pipeline"
git push origin master
```

In the UI you can monitor the status of your application deployment
