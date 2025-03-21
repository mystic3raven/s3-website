Step-by-Step Terraform Planning Process



Understand the Business Goal



**Goal:** Host a static website on AWS with performance, security, and reliability.

### Requirements:

- Static content hosted on **S3**
- Global distribution using **CloudFront**
- **IAM roles/policies** to restrict access and enable integration
- Optional security via **VPC endpoints**
- Scalability, low latency, and cost optimization

### **Break Down the Architecture into Terraform Modules/Files**

Divide the architecture into manageable Terraform units (files):



| Component      | File              | Purpose                        |
| -------------- | ----------------- | ------------------------------ |
| S3 Bucket      | s3_bucket.tf      | Static site + public access    |
| CloudFront     | cloudfront.tf     | CDN + OAI for secure S3 access |
| IAM Roles      | iam_roles.tf`     | Permissions for CloudFront     |
| VPC Endpoints  | vpc_endpoints.tf` | Optional private routing to S3 |
| Providers/Vars | provider.tf       | Optional private routing to S3 |

| Component | File | Purpose |
| --------- | ---- | ------- |

| S3 Bucket | `s3_bucket.tf` | Static site + public access |
| --------- | -------------- | --------------------------- |

| CloudFront | `cloudfront.tf` | CDN + OAI for secure S3 access |
| ---------- | --------------- | ------------------------------ |

| IAM Roles | `iam_roles.tf` | Permissions for CloudFront |
| --------- | -------------- | -------------------------- |

| VPC Endpoints | `vpc_endpoints.tf` | Optional private routing to S3 |
| ------------- | ------------------ | ------------------------------ |

| Providers/Vars | `provider.tf`, `variables.tf`, `outputs.tf` | Config |
| -------------- | ------------------------------------------- | ------ |


