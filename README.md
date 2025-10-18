# 504 Serverless Functions Repository

## Lab Rules
**Lab Chosen:** Bilirubin Classification  
**Rule Implemented:**  
- **Total bilirubin normal range:** 0.1 – 1.2 mg/dL  
- **Direct bilirubin normal range:** < 0.3 mg/dL  
- **Formula / Threshold:**  
  ```text
  if total_bilirubin >= 2.0 → High 
  if direct_bilirubin >= 0.3 → Elevated direct bilirubin
  else → Normal
Citation: Mount Sinai Health System. Bilirubin Test. https://www.mountsinai.org/health-library/tests/bilirubin

## Cloud Environments & Regions
Google Cloud: us-east1

Azure: 

## Deployment Commands / Steps
Google Cloud Functions

Copy code
### Deploy function to GCP
gcloud functions deploy hello_http \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated \
    --region us-central1
### Azure Functions


## URL
GCP: url = "https://total-billirubin-776757242044.us-east1.run.app"
Azure:

## Screenshots
### Google Cloud
<img width="1456" height="853" alt="gcp vs " src="https://github.com/user-attachments/assets/af55a94a-4159-4eec-80dd-a098b9bcb5a1" />
<img width="1454" height="718" alt="gcp google cloud terminal" src="https://github.com/user-attachments/assets/a9547645-5cdc-499a-bf3f-630d62b3ca11" />



### Azure

## Logs / Monitoring
Google Cloud: 

Azure: 

## Cloud Comparison
Google Cloud Functions: Easier to deploy with a single CLI command and straightforward unauthenticated HTTP triggers.
Azure Functions: 


## Recording
URl:

