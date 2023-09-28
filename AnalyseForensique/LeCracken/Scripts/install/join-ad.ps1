param(
    [String]$domain,
    [String]$domainControllerAddress,
    [String]$adminLogin,
    [String]$adminPassword
)

Set-DnsClientServerAddress -ServerAddresses ($domainControllerAddress) -InterfaceAlias 'Ethernet'
Set-DnsClientServerAddress -ServerAddresses ($domainControllerAddress) -InterfaceAlias 'Ethernet 2'

$password = ConvertTo-SecureString $adminPassword -AsPlainText -Force
$credentials = New-Object System.Management.Automation.PSCredential ($adminLogin, $password)
Add-Computer `
    -DomainName $domain `
    -Force `
    -Credential $credentials