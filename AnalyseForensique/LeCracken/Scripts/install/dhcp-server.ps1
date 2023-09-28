param(
    [String]$dcName,
    [String]$dhcpServerName,
    [String]$adminLogin,
    [String]$adminPassword
)

Install-WindowsFeature DHCP -IncludeManagementTools

$securePass = ConvertTo-SecureString $adminPassword -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($adminLogin, $securePass)

Write-Output $dnsName

Invoke-Command -Computer $dcName -Credential $credential -ArgumentList $dhcpServerName -ScriptBlock {
    Param (
        [string]$dhcpServerName
    )
    Install-WindowsFeature RSAT-DHCP
    Add-DhcpServerInDC -DnsName $dhcpServerName
}