output "s3_website_url" {
  value = aws_s3_bucket_website_configuration.static_site.website_endpoint
}

output "cloudfront_domain_name" {
  value = aws_cloudfront_distribution.site_distribution.domain_name
}
