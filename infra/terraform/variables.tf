variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}

variable "resource_group_name" {
  description = "Azure Resource Group name"
  type        = string
  default     = "rg-open-data-ai-analytics-lab"
}

variable "vm_admin_username" {
  description = "Admin username for Linux VM"
  type        = string
  default     = "azureuser"
}

variable "vm_size" {
  description = "Azure VM size"
  type        = string
  default     = "Standard_B2s"
}

variable "repo_url" {
  description = "GitHub repository URL with Docker Compose project"
  type        = string
  default     = "https://github.com/RomanSeniv2005/open-data-ai-analytics.git"
}