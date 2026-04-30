output "public_ip" {
  description = "Public IP address of the Azure Linux VM"
  value       = azurerm_public_ip.public_ip.ip_address
}

output "web_url" {
  description = "URL of the deployed web interface"
  value       = "http://${azurerm_public_ip.public_ip.ip_address}:8000"
}

output "resource_group_name" {
  description = "Created Azure Resource Group"
  value       = azurerm_resource_group.rg.name
}

output "vm_name" {
  description = "Created Azure Linux VM name"
  value       = azurerm_linux_virtual_machine.vm.name
}