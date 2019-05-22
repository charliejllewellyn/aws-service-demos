#import boto3
import pandas as pd
import s3fs

bucket='cjl-temp-dub'
data_key = 'enron_emails/Enron emails.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)

#df = pd.read_csv(data_location, skiprows=1000, nrows=2000)
df = pd.read_csv(data_location)

print(df.shape)

import email
import datetime
import re

pd.set_option('display.max_colwidth', -1)

FromToEmailList = []
EdgeList = []
EmailDetails = []

def cleanEmail(email):
    cleanEmail  = email.replace("'", "")
    cleanEmail = cleanEmail.strip()
    return cleanEmail

def correctDate(dateString):
    try:
        dateTemp = OriginalEmailData['Date'].split()[:-2]
        date = ' '.join(dateTemp)
        correctedDate = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')
        return correctedDate
    except Exception as e:
        return dateString

def getEmailMessage(OriginalEmailData):
    if OriginalEmailData.is_multipart():
        for payload in OriginalEmailData.get_payload():
            return payload.get_payload()
    else:
        return OriginalEmailData.get_payload()

def formEdgeResults(FromObject, ToObject, Label):
    newRecord = {}
    newRecord['~from'] = FromObject
    newRecord['~to'] = ToObject
    newRecord['~label'] = Label
    newRecord['weight:Double'] = '1.0'
    return newRecord

def expandToFieldResults(record):
    ToEmailList = re.split(', |\n',record['To'])
    ToEmailList = filter(None, ToEmailList)
    if len(ToEmailList) <= 1:
        EdgeList.append(formEdgeResults(record['EmailId'], cleanEmail(ToEmailList[0]), 'RecievedEmail'))
    else:
        for ToEmailAddress in ToEmailList:
            EdgeList.append(formEdgeResults(record['EmailId'], cleanEmail(ToEmailAddress), 'RecievedEmail'))

def addFromToEmailEdge(fromEmail, EmailId):
    EdgeList.append(formEdgeResults(cleanEmail(fromEmail), EmailId, 'SentEmail'))

for index, row in df.iterrows():
    OriginalEmailData = email.message_from_string(row["message"])

    EmailToFlow = {}
    EmailToFlow['Date'] = correctDate(OriginalEmailData['Date'])
    EmailToFlow['To'] = OriginalEmailData['To']
    EmailToFlow['EmailId'] = row['file']

    Email = {}
    Email['~id'] = row['file']
    Email['Id:string'] = row['file']
    Email['Message:string'] = getEmailMessage(OriginalEmailData)
    Email['~label'] = 'email'

    if OriginalEmailData['To']:
        EmailDetails.append(Email)
        addFromToEmailEdge(OriginalEmailData['From'], row['file'])
        expandToFieldResults(EmailToFlow)

EdgeDf = pd.DataFrame(EdgeList)
EdgeDf.to_csv('/tmp/edges.csv', header=True, index=True, index_label='~id', columns=['~from', '~to', '~label', 'weight:Double'])

EmailDf = pd.DataFrame(EmailDetails)
#EmailDf.to_csv('/tmp/emails.csv', header=True, index=True, index_label='~id')
EmailDf.to_csv('/tmp/emails.csv', header=True, index=False, columns=['~id', '~label', 'Id:string', 'Message:string'])

ToDf = pd.DataFrame(EdgeDf.loc[EdgeDf['~label'] == "RecievedEmail", '~to'])
#ToDf['~label'] = 'person'
#ToDf.to_csv('/tmp/recievers.csv', header=True, index=True, index_label='~id')

FromDf = pd.DataFrame(EdgeDf.loc[EdgeDf['~label'] == "SentEmail"])
#FromDf['~label'] = 'person'
#FromDf.to_csv('/tmp/senders.csv', header=True, index=True, columns = ['from:string','~label'], index_label='~id')

result = pd.DataFrame(columns=['Person', '~label'])
result['Person'] = ToDf['~to']
result = result.Person.append(FromDf['~from'])
result = result.drop_duplicates()
result = result.to_frame()
result['~label'] = 'person'
result.columns = ['~id', '~label']
result.info()

#result.to_csv('/tmp/people.csv', header=True, index=True, index_label='~id', columns=['~label', 'person:string'])
result.to_csv('/tmp/people.csv', header=True, index=False, columns=['~id', '~label'])


