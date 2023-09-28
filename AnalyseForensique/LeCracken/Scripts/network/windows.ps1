param(
    [String]$ip,
    [String]$gateway,
    [String]$dns
)

# Remove the IP set by Vagrant
Remove-NetIPAddress `
    -IPAddress $ip `
    -Confirm:$false

New-NetIPAddress `
    -InterfaceAlias "Ethernet 2" `
    -IPAddress $ip `
    -DefaultGateway $gateway `
    -PrefixLength 24 `
    -Confirm:$false

Set-NetIPInterface `
    -InterfaceAlias "Ethernet 2" `
    -Dhcp Disabled

Set-DNSClientServerAddress `
    -InterfaceAlias "Ethernet 2" `
    -ServerAddresses $dns

Set-NetIPInterface -InterfaceAlias Ethernet | Remove-NetRoute -Confirm:$false