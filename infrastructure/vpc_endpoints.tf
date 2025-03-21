data "aws_vpc" "default" {
  default = true
}

data "aws_route_table" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

resource "aws_vpc_endpoint" "s3_endpoint" {
  vpc_id            = data.aws_vpc.default.id
  service_name      = "com.amazonaws.${var.region}.s3"
  route_table_ids   = [data.aws_route_table.default.id]
  vpc_endpoint_type = "Gateway"
}
